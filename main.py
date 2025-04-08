#!/usr/bin/env python3
"""Matrix CLI Rain Visualizer - Main entry point."""

import curses
import argparse
import sys
from typing import Dict

from matrix import MatrixRain
from utils import init_color_pairs, FPSController, get_terminal_size
from config import DEFAULT_CONFIG

def parse_args() -> Dict:
    """Parse command line arguments and return config dict."""
    parser = argparse.ArgumentParser(description='Matrix CLI Rain Visualizer')
    parser.add_argument('--speed', type=float, default=DEFAULT_CONFIG['speed'],
                      help='Animation speed (default: 0.03)')
    parser.add_argument('--density', type=float, default=DEFAULT_CONFIG['density'],
                      help='Density of rain drops (0.0-1.0)')
    parser.add_argument('--fps', type=int, default=DEFAULT_CONFIG['fps_cap'],
                      help='Target frames per second')
    parser.add_argument('--duration', type=int, default=DEFAULT_CONFIG['duration'],
                      help='Duration in seconds (0 for infinite)')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not 0.0 <= args.density <= 1.0:
        parser.error('Density must be between 0.0 and 1.0')
    if args.fps <= 0:
        parser.error('FPS must be positive')
    if args.speed <= 0:
        parser.error('Speed must be positive')
    
    return vars(args)

def main(stdscr):
    """Main function that runs the Matrix rain animation."""
    # Hide the cursor and disable input echoing
    curses.curs_set(0)
    stdscr.nodelay(1)
    
    # Initialize colors
    init_color_pairs()
    
    # Get configuration
    config = DEFAULT_CONFIG.copy()
    config.update(parse_args())
    
    # Initialize the rain effect
    rain = MatrixRain(config)
    height, width = get_terminal_size(stdscr)
    rain.initialize_streams(width, height)
    
    # Initialize FPS controller
    fps_controller = FPSController(config['fps_cap'])
    
    # Main animation loop
    start_time = sys.maxsize if config['duration'] == 0 else curses.time.time()
    
    while rain.running:
        if not rain.handle_input(stdscr):
            break
            
        rain.update(height)
        rain.draw(stdscr)
        
        fps_controller.wait_for_next_frame()
        
        # Check duration
        if curses.time.time() - start_time > config['duration']:
            break

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        sys.exit(0)
