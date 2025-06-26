# 🎯 CursorAFK - AI Assistant Auto-Nudger

Keep your AI assistant awake and responsive with automatic periodic nudges! No more frozen conversations or stalled responses.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🤖 What Does This Do?

CursorAFK is a system tray application that prevents AI assistants (like Claude, ChatGPT, Cursor, etc.) from going idle by automatically sending periodic "nudges" to keep the conversation active. Perfect for long research sessions, automated workflows, or when you need your AI to stay responsive while you're away.

## ✨ Features

- **🎯 Visual Area Selection**: Click and drag to select exactly where your chat input is located
- **🟢 Smart Status Icons**: 
  - 🔴 Red = No area selected
  - 🟡 Yellow = Area selected, inactive
  - 🟢 Green = Active and nudging
- **⏰ Automatic Nudging**: Sends a keystroke every 90 seconds to keep your AI assistant active
- **🖥️ System Tray Integration**: Runs quietly in the background
- **🎮 Easy Controls**: Right-click menu for all operations

## 🚀 Quick Start

### Prerequisites

- Windows 10/11
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/cursorafk.git
   cd cursorafk
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python cursorafk.py
   ```

## 📋 Step-by-Step Usage Guide

### Step 1: Launch CursorAFK
```bash
python cursorafk.py
```
- Look for a **red square icon** in your system tray (bottom-right corner)
- The red color means no chat area has been selected yet

### Step 2: Open Your AI Assistant
- Open your AI assistant (Claude, ChatGPT, Cursor, etc.) in a window
- Make sure the chat interface is visible and accessible

### Step 3: Select Chat Input Area
1. **Right-click** the red tray icon
2. Click **"Select Chat Area"**
3. Your screen will dim with a semi-transparent overlay
4. **Click and drag** to draw a rectangle around your chat input box
5. The rectangle will turn **green** when you release the mouse
6. Press **ENTER** to confirm or **ESC** to cancel
7. The tray icon turns **yellow** (area selected, but not active yet)

### Step 4: Start Autonomous Mode
1. **Right-click** the yellow tray icon
2. Click **"Start Autonomous Mode"**
3. The icon turns **green** - you're now active!
4. Every 90 seconds, CursorAFK will:
   - Click your selected chat area
   - Type the letter "g"
   - Press Enter

### Step 5: Monitor and Control
- **Green icon** = Active nudging
- Check console output for nudge confirmations
- Right-click anytime to:
  - Stop autonomous mode
  - Change chat area
  - Exit application

## 🛠️ Configuration

### Changing Nudge Interval
Edit `cursorafk.py` line with `self.stop_event.wait(90)` and change `90` to your desired seconds.

### Changing Nudge Message
Edit the `pyautogui.write('g')` line to send different text.

## 🐛 Troubleshooting

### Common Issues

**"No chat area selected" error**
- Make sure you've completed Step 3 (selecting the chat area)
- The tray icon should be yellow or green, not red

**Nudges not working**
- Verify your selected area covers the chat input box
- Try reselecting the area if the interface has moved
- Ensure the AI assistant window isn't minimized

**Can't see the tray icon**
- Check if it's hidden in the system tray overflow
- Click the "^" arrow in the system tray to show hidden icons

**Selection overlay not appearing**
- Make sure no other applications are in fullscreen mode
- Try running as administrator if needed

### Debug Mode
Run with console output visible to see detailed logs:
```bash
python cursorafk.py
```
Keep the terminal window open to monitor nudge activity.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built to keep Claude, Cursor and other AI assistants active and responsive
- Inspired by the need for uninterrupted AI conversations
- Thanks to the Python community for excellent libraries like `pystray` and `pyautogui`

## ⭐ Star This Project!

If CursorAFK helps keep your AI conversations flowing, give it a star! It helps others discover this tool and keeps AI assistants everywhere happy and responsive.

---

**Made with ❤️ for the AI community**