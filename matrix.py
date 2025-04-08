"""Core Matrix rain animation logic."""

import curses
import random
from typing import List, Dict

from config import DEFAULT_CONFIG, DEFAULT_CHARS
from utils import (
    get_random_char,
    get_random_stream_length,
    get_random_speed_multiplier,
    get_terminal_size,
)

class RainDrop:
    """Represents a single falling character stream."""
    
    def __init__(self, x: int, height: int, config: Dict):
        self.x = x
        self.y = random.randint(-height // 2, 0)  # Start above screen
        self.speed = config['speed'] * get_random_speed_multiplier(
            config.get('min_speed_variation', 0.5),
            config.get('max_speed_variation', 2.0)
        )
        self.length = get_random_stream_length(
            config['min_stream_length'],
            config['max_stream_length']
        )
        self.chars = [get_random_char(DEFAULT_CHARS) for _ in range(self.length)]
        self.active = True
        self.position = 0.0  # Floating point position for smooth movement

    def update(self, height: int):
        """Update raindrop position and characters."""
        self.position += self.speed
        self.y = int(self.position)
        
        # Regenerate characters occasionally
        if random.random() < 0.1:
            idx = random.randint(0, self.length - 1)
            self.chars[idx] = get_random_char(DEFAULT_CHARS)
        
        # Check if the stream has moved entirely off screen
        if self.y - self.length > height:
            self.active = False

    def draw(self, stdscr):
        """Draw the raindrop on the screen."""
        height, _ = get_terminal_size(stdscr)
        
        for i in range(self.length):
            y = self.y - i
            if 0 <= y < height:
                # Calculate brightness based on position in stream
                if i == 0:
                    attr = curses.color_pair(5) | curses.A_BOLD  # Head is brightest
                elif i < 3:
                    attr = curses.color_pair(4)
                elif i < 6:
                    attr = curses.color_pair(3)
                else:
                    attr = curses.color_pair(2)
                
                try:
                    stdscr.addch(y, self.x, self.chars[i], attr)
                except curses.error:
                    pass  # Ignore errors from writing to bottom-right corner

class MatrixRain:
    """Main class for managing the Matrix rain effect."""
    
    def __init__(self, config: Dict = None):
        self.config = config or DEFAULT_CONFIG
        self.raindrops: List[RainDrop] = []
        self.running = True

    def initialize_streams(self, width: int, height: int):
        """Initialize rain streams based on density configuration."""
        num_streams = int(width * self.config['density'])
        columns = random.sample(range(width), num_streams)
        
        for x in columns:
            self.raindrops.append(RainDrop(x, height, self.config))

    def update(self, height: int):
        """Update all active raindrops and create new ones as needed."""
        # Update existing raindrops
        self.raindrops = [drop for drop in self.raindrops if drop.active]
        for drop in self.raindrops:
            drop.update(height)
        
        # Create new raindrops to maintain density
        if random.random() < 0.1:  # Occasional new drops
            for drop in self.raindrops:
                if not drop.active:
                    drop.y = random.randint(-height // 2, 0)
                    drop.position = float(drop.y)
                    drop.active = True
                    break

    def draw(self, stdscr):
        """Draw the current frame."""
        stdscr.erase()
        for drop in self.raindrops:
            drop.draw(stdscr)
        stdscr.refresh()

    def handle_input(self, stdscr) -> bool:
        """Handle user input. Returns False if the animation should stop."""
        try:
            key = stdscr.getch()
            if key == ord('q'):
                return False
            # Add more controls here as needed
        except curses.error:
            pass
        return True
