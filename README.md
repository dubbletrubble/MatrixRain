# Matrix Rain

A visual implementation of the iconic Matrix digital rain effect in your terminal.

## Description
This project creates a mesmerizing Matrix-style digital rain animation effect that runs directly in your terminal. Features include:
- Customizable animation speed and density
- Configurable FPS cap
- Color support with varying brightness levels
- Interactive controls

## Requirements
- Python 3.7 or higher
- Terminal with color support

## Quick Start

### Windows Users
1. Make sure Python 3.7+ is installed
2. Double-click `start_matrix.bat`
   - This will automatically create a virtual environment
   - Install all required dependencies
   - Start the Matrix rain effect

### Unix/Mac Users
```bash
# Install dependencies
pip3 install -r requirements.txt

# Run the program
python3 main.py
```

## Usage Options
You can customize the animation with these command-line options:

```bash
python main.py --speed 0.02    # Animation speed (default: 0.03)
python main.py --density 0.8    # Rain density (default: 0.7)
python main.py --fps 60         # Frame rate cap (default: 30)
python main.py --duration 60    # Run duration in seconds (default: 0 for infinite)
```

## Controls
- Press 'q' to quit the program

## Troubleshooting

### Windows
If you encounter any issues:
1. Make sure Python is added to your PATH
2. Try running the program from Command Prompt or PowerShell
3. Check that you have administrator rights when installing packages

### Unix/Mac
If you encounter terminal errors:
1. Make sure your terminal supports curses
2. Try running with: `TERM=xterm-256color python3 main.py`

## License
MIT License
