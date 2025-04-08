"""Configuration settings for the Matrix CLI Rain Visualizer."""

import string

# Default configuration
DEFAULT_CONFIG = {
    'speed': 0.03,           # Base frame delay in seconds
    'density': 0.7,          # Percentage of columns with active streams
    'fps_cap': 30,          # Maximum frames per second
    'duration': 0,          # Run indefinitely by default
    'min_stream_length': 5,  # Minimum length of character streams
    'max_stream_length': 15, # Maximum length of character streams
}

# Character sets
ASCII_CHARS = string.ascii_letters + string.digits
SPECIAL_CHARS = '!@#$%^&*()_+-=<>?'
DEFAULT_CHARS = ASCII_CHARS + SPECIAL_CHARS

# Color configuration
COLORS = {
    'default': {
        'stream': (0, 255, 0),      # Regular green
        'head': (200, 255, 200),    # Bright green for leading character
        'tail': (0, 128, 0),        # Darker green for tail effect
    }
}

# Performance settings
BUFFER_LINES = 5  # Extra lines to render above screen
MAX_SPEED_VARIATION = 2.0  # Maximum random speed multiplier
MIN_SPEED_VARIATION = 0.5  # Minimum random speed multiplier
