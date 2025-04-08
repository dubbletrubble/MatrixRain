"""Utility functions for the Matrix CLI Rain Visualizer."""

import random
import curses
import time

def get_random_char(charset):
    """Return a random character from the given charset."""
    return random.choice(charset)

def get_random_stream_length(min_length, max_length):
    """Generate a random stream length within the specified range."""
    return random.randint(min_length, max_length)

def get_random_speed_multiplier(min_var, max_var):
    """Generate a random speed multiplier for stream variation."""
    return random.uniform(min_var, max_var)

def init_color_pairs():
    """Initialize color pairs for curses if color is supported."""
    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()
        # Initialize color pairs for different brightness levels
        for i in range(1, 6):
            curses.init_pair(i, curses.COLOR_GREEN, -1)

def calculate_frame_delay(target_fps):
    """Calculate the frame delay needed to maintain target FPS."""
    return 1.0 / target_fps

class FPSController:
    """Simple FPS controller to maintain consistent frame rate."""
    
    def __init__(self, target_fps):
        self.frame_delay = calculate_frame_delay(target_fps)
        self.last_frame_time = time.time()
    
    def wait_for_next_frame(self):
        """Wait until it's time for the next frame."""
        current_time = time.time()
        elapsed = current_time - self.last_frame_time
        if elapsed < self.frame_delay:
            time.sleep(self.frame_delay - elapsed)
        self.last_frame_time = time.time()

def get_terminal_size(stdscr):
    """Get the current terminal size."""
    height, width = stdscr.getmaxyx()
    return height, width
