import pystray
import pyautogui
from PIL import Image, ImageDraw
import threading
import time
import sys
import tkinter as tk
from tkinter import messagebox

class AreaSelector:
    def __init__(self, callback):
        self.callback = callback
        self.start_x = None
        self.start_y = None
        self.rect_id = None
        self.selecting = False
        
        # Create full-screen transparent window for selection
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)
        self.root.attributes('-topmost', True)
        self.root.configure(bg='black')
        self.root.cursor = 'crosshair'
        
        # Create canvas for drawing selection rectangle
        self.canvas = tk.Canvas(self.root, highlightthickness=0, bg='black')
        self.canvas.pack(fill='both', expand=True)
        
        # Bind mouse events
        self.canvas.bind('<Button-1>', self.start_selection)
        self.canvas.bind('<B1-Motion>', self.update_selection)
        self.canvas.bind('<ButtonRelease-1>', self.end_selection)
        self.canvas.bind('<Escape>', self.cancel_selection)
        
        # Bind keyboard events
        self.root.bind('<Escape>', self.cancel_selection)
        self.root.bind('<Return>', self.confirm_selection)
        
        self.root.focus_set()
        
        # Add instruction text
        instruction = "Click and drag to select the chat input area. Press ENTER to confirm or ESC to cancel."
        self.canvas.create_text(
            self.root.winfo_screenwidth() // 2, 50,
            text=instruction,
            fill='white',
            font=('Arial', 16, 'bold')
        )
    
    def start_selection(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.selecting = True
        
        # Clear previous rectangle
        if self.rect_id:
            self.canvas.delete(self.rect_id)
    
    def update_selection(self, event):
        if self.selecting and self.start_x is not None:
            # Clear previous rectangle
            if self.rect_id:
                self.canvas.delete(self.rect_id)
            
            # Draw new rectangle
            self.rect_id = self.canvas.create_rectangle(
                self.start_x, self.start_y, event.x, event.y,
                outline='red', width=3, fill='', dash=(5, 5)
            )
            
            # Show coordinates
            coord_text = f"Area: ({self.start_x}, {self.start_y}) to ({event.x}, {event.y})"
            self.canvas.delete('coords')
            self.canvas.create_text(
                self.root.winfo_screenwidth() // 2, 100,
                text=coord_text,
                fill='yellow',
                font=('Arial', 12),
                tags='coords'
            )
    
    def end_selection(self, event):
        if self.selecting:
            self.selecting = False
            
            # Calculate rectangle bounds
            x1, y1 = min(self.start_x, event.x), min(self.start_y, event.y)
            x2, y2 = max(self.start_x, event.x), max(self.start_y, event.y)
            
            # Ensure minimum size
            if abs(x2 - x1) < 10 or abs(y2 - y1) < 10:
                self.canvas.create_text(
                    self.root.winfo_screenwidth() // 2, 150,
                    text="Selection too small! Try again.",
                    fill='red',
                    font=('Arial', 12, 'bold'),
                    tags='error'
                )
                return
            
            # Change rectangle to green to indicate ready for confirmation
            if self.rect_id:
                self.canvas.delete(self.rect_id)
            
            self.rect_id = self.canvas.create_rectangle(
                x1, y1, x2, y2,
                outline='green', width=3, fill='', dash=()
            )
            
            # Show confirmation message
            self.canvas.delete('coords')
            self.canvas.create_text(
                self.root.winfo_screenwidth() // 2, 100,
                text=f"Selected area: ({x1}, {y1}) to ({x2}, {y2})",
                fill='green',
                font=('Arial', 12, 'bold'),
                tags='coords'
            )
            
            self.canvas.create_text(
                self.root.winfo_screenwidth() // 2, 130,
                text="Press ENTER to confirm this selection or ESC to cancel",
                fill='white',
                font=('Arial', 12),
                tags='confirm'
            )
            
            self.selected_area = (x1, y1, x2, y2)
    
    def confirm_selection(self, event=None):
        if hasattr(self, 'selected_area'):
            self.callback(self.selected_area)
            self.root.destroy()
    
    def cancel_selection(self, event=None):
        self.callback(None)
        self.root.destroy()
    
    def show(self):
        self.root.mainloop()

class CursorAFK:
    def __init__(self):
        self.is_active = False
        self.nudge_thread = None
        self.stop_event = threading.Event()
        self.chat_area = None  # Will store (x1, y1, x2, y2) coordinates
        
        # Disable pyautogui failsafe for smoother operation
        pyautogui.FAILSAFE = False
        
        # Create the system tray icon
        self.update_menu()
    
    def update_menu(self):
        """Update the system tray menu based on current state"""
        menu_items = []
        
        if self.chat_area is None:
            menu_items.append(pystray.MenuItem("Select Chat Area", self.select_chat_area))
        else:
            area_text = f"Area Set: ({self.chat_area[0]}, {self.chat_area[1]}) to ({self.chat_area[2]}, {self.chat_area[3]})"
            menu_items.append(pystray.MenuItem(area_text, None, enabled=False))
            menu_items.append(pystray.MenuItem("Change Chat Area", self.select_chat_area))
            
            if not self.is_active:
                menu_items.append(pystray.MenuItem("Start Autonomous Mode", self.start_autonomous_mode))
            else:
                menu_items.append(pystray.MenuItem("Stop Autonomous Mode", self.stop_autonomous_mode))
        
        menu_items.append(pystray.MenuItem("Exit", self.quit_application))
        
        # Create or update the icon
        if hasattr(self, 'icon'):
            self.icon.menu = pystray.Menu(*menu_items)
        else:
            self.icon = pystray.Icon(
                "autonomizer",
                self.create_icon(),
                "Autonomizer - AI Assistant Nudger",
                menu=pystray.Menu(*menu_items)
            )
    
    def create_icon(self):
        """Create a colored square icon - green when active and area set, yellow when area set but inactive, red when no area set"""
        # Create a 64x64 image
        image = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        # Choose color based on state
        if self.chat_area is None:
            color = (255, 0, 0, 255)  # Red - no area set
        elif self.is_active:
            color = (0, 255, 0, 255)  # Green - active
        else:
            color = (255, 255, 0, 255)  # Yellow - area set but inactive
        
        # Draw a filled square with some padding
        draw.rectangle([8, 8, 56, 56], fill=color)
        
        return image
    
    def update_icon(self):
        """Update the tray icon to reflect current state"""
        self.icon.icon = self.create_icon()
        self.update_menu()
    
    def select_chat_area(self, icon=None, item=None):
        """Open area selection dialog"""
        def area_selected(area):
            if area:
                self.chat_area = area
                print(f"Chat area set to: {area}")
            else:
                print("Area selection cancelled")
            
            self.update_icon()
        
        # Stop autonomous mode if running
        if self.is_active:
            self.stop_autonomous_mode()
        
        # Show area selector
        selector = AreaSelector(area_selected)
        # Run selector in a separate thread to avoid blocking the tray
        threading.Thread(target=selector.show, daemon=True).start()
    
    def click_chat_area(self):
        """Click in the center of the selected chat area"""
        if not self.chat_area:
            print("No chat area selected!")
            return False
        
        try:
            # Calculate center of the selected area
            x1, y1, x2, y2 = self.chat_area
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2
            
            # Click to focus the chat input area
            pyautogui.click(center_x, center_y)
            time.sleep(0.2)  # Wait for click to register
            
            return True
            
        except Exception as e:
            print(f"Error clicking chat area: {e}")
            return False
    
    def send_nudge(self):
        """Send the nudge keystroke sequence (g + Enter) to the selected area"""
        try:
            # First click the chat area to ensure focus
            if not self.click_chat_area():
                return
            
            # Type 'g' and press Enter
            pyautogui.write('g')
            time.sleep(0.1)
            pyautogui.press('enter')
            print(f"Nudge sent to chat area at {time.strftime('%H:%M:%S')}")
            
        except Exception as e:
            print(f"Error sending nudge: {e}")
    
    def nudge_worker(self):
        """Background thread that performs the nudging every 90 seconds"""
        print("Autonomous mode started - nudging every 90 seconds")
        
        while not self.stop_event.is_set():
            # Wait for 90 seconds or until stop event is set
            if self.stop_event.wait(90):
                break
            
            # Perform the nudge sequence
            self.send_nudge()
        
        print("Autonomous mode stopped")
    
    def start_autonomous_mode(self, icon=None, item=None):
        """Start the autonomous nudging process"""
        if not self.chat_area:
            print("Cannot start autonomous mode: No chat area selected!")
            return
        
        if not self.is_active:
            self.is_active = True
            self.stop_event.clear()
            
            # Update icon and menu
            self.update_icon()
            
            # Start the nudging thread
            self.nudge_thread = threading.Thread(target=self.nudge_worker, daemon=True)
            self.nudge_thread.start()
            
            print("Autonomous mode activated")
    
    def stop_autonomous_mode(self, icon=None, item=None):
        """Stop the autonomous nudging process"""
        if self.is_active:
            self.is_active = False
            self.stop_event.set()
            
            # Update icon and menu
            self.update_icon()
            
            # Wait for thread to finish
            if self.nudge_thread and self.nudge_thread.is_alive():
                self.nudge_thread.join(timeout=1)
            
            print("Autonomous mode deactivated")
    
    def quit_application(self, icon, item):
        """Exit the application completely"""
        print("Shutting down CursorAFK...")
        
        # Stop autonomous mode if active
        if self.is_active:
            self.stop_autonomous_mode(icon, item)
        
        # Stop the tray icon
        icon.stop()
        sys.exit(0)
    
    def run(self):
        """Start the system tray application"""
        print("Starting CursorAFK...")
        print("Right-click the tray icon to access menu options")
        print("You must first select the chat input area before starting autonomous mode")
        
        # Run the tray icon (this blocks until the application exits)
        self.icon.run()

def main():
    """Main entry point"""
    try:
        app = CursorAFK()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()