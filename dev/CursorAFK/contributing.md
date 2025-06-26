# Contributing to CursorAFK

Thank you for your interest in contributing to CursorAFK! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Git
- Basic knowledge of Python and GUI applications

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/cursorafk.git
   cd cursorafk
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If we add dev dependencies
   ```

## 🐛 Reporting Issues

### Before Submitting an Issue
- Check existing issues to avoid duplicates
- Test with the latest version
- Gather system information (OS version, Python version)

### Issue Template
When reporting bugs, please include:
- **Description**: Clear description of the issue
- **Steps to Reproduce**: Numbered steps to recreate the problem
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **System Info**: OS, Python version, dependency versions
- **Screenshots**: If applicable

## 💡 Suggesting Features

We welcome feature suggestions! Please:
- Check if the feature already exists or is planned
- Explain the use case and benefits
- Consider if it fits the project's scope
- Provide mockups or examples if helpful

## 🔧 Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise

### Code Structure
```
cursorafk/
├── cursorafk.py           # Main application
├── requirements.txt        # Dependencies
├── README.md              # Documentation
├── LICENSE                # License file
└── tests/                 # Test files (future)
```

### Commit Messages
Use clear, descriptive commit messages:
```
feat: add new nudge interval configuration
fix: resolve area selection on high-DPI displays
docs: update installation instructions
refactor: simplify icon update logic
```

## 🧪 Testing

Currently, testing is manual. We welcome contributions to add automated testing!

### Manual Testing Checklist
- [ ] Application starts without errors
- [ ] System tray icon appears correctly
- [ ] Area selection works on different screen resolutions
- [ ] Nudging works with various applications
- [ ] Menu options function correctly
- [ ] Application exits cleanly

## 📝 Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, documented code
   - Test your changes thoroughly
   - Update documentation if needed

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: description of your changes"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Submit a pull request**
   - Use a clear, descriptive title
   - Explain what your changes do
   - Reference any related issues
   - Add screenshots for UI changes

### Pull Request Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Testing
- [ ] Tested on Windows 10/11
- [ ] Tested with multiple applications
- [ ] No new errors in console

## Screenshots
If applicable, add screenshots
```

## 🏗️ Architecture Overview

### Key Components
- **CursorAFK Class**: Main application controller
- **AreaSelector Class**: Handles visual area selection
- **System Tray Integration**: Uses pystray for tray icon and menu
- **Threading**: Separate threads for UI and nudging operations

### Key Libraries
- `pystray`: System tray functionality
- `pyautogui`: Screen interaction and automation
- `tkinter`: Area selection overlay
- `PIL`: Image processing for icons

## 🎯 Areas for Contribution

### High Priority
- Cross-platform support (macOS, Linux)
- Automated testing framework
- Configuration file support
- Better error handling and user feedback

### Medium Priority
- Multiple area selection
- Custom nudge messages
- Scheduling (different intervals for different times)
- Application-specific presets

### Low Priority
- Plugin system
- Remote control via web interface
- Statistics and logging
- Themes and customization

## 📚 Resources

- [Python Documentation](https://docs.python.org/)
- [pystray Documentation](https://pystray.readthedocs.io/)
- [pyautogui Documentation](https://pyautogui.readthedocs.io/)
- [tkinter Tutorial](https://docs.python.org/3/library/tkinter.html)

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Email**: Contact maintainers for sensitive issues

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Special thanks in documentation

Thank you for helping make CursorAFK better for everyone! 🚀