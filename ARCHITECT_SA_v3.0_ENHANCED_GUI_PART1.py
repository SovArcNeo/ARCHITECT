#!/usr/bin/env python3
"""
ARCHITECT SYSTEM v3.0 - ENHANCED SCI-FI GUI (PART 1)
Enhanced Theme System and Animated Widgets
This module contains the advanced visual components
"""

import tkinter as tk
from tkinter import ttk, Canvas, Frame, Label
import time
import math
from typing import Optional, Callable, List
from datetime import datetime

# ============================================================================
# ENHANCED SCI-FI THEME SYSTEM
# ============================================================================

class EnhancedSciFiTheme:
    """Enhanced Sci-Fi theme with multiple color schemes"""

    # Base colors
    BG_BLACK = "#000000"
    BG_DARK = "#001100"
    BG_MEDIUM = "#002200"
    BG_LIGHT = "#003300"

    # Primary palette (Matrix Green)
    GREEN_GLOW = "#00ff00"
    GREEN_BRIGHT = "#00ff41"
    GREEN_MEDIUM = "#00cc33"
    GREEN_DIM = "#008800"
    GREEN_DARK = "#004400"

    # Secondary palette (Cyan)
    CYAN_BRIGHT = "#00ffff"
    CYAN_MEDIUM = "#00cccc"
    CYAN_DIM = "#008888"

    # Accent colors
    MAGENTA = "#ff00ff"
    PURPLE = "#8800ff"
    ORANGE = "#ff8800"
    BLUE = "#0088ff"

    # Status colors
    STATUS_ONLINE = "#00ff00"
    STATUS_WARNING = "#ffff00"
    STATUS_CRITICAL = "#ff0000"
    STATUS_INFO = "#00ffff"

    # Threat level colors
    THREAT_BENIGN = "#00ff00"
    THREAT_LOW = "#88ff00"
    THREAT_MEDIUM = "#ffff00"
    THREAT_HIGH = "#ff8800"
    THREAT_CRITICAL = "#ff0000"
    THREAT_EMERGENCY = "#ff00ff"

    # UI element colors
    BORDER_PRIMARY = "#00ff00"
    BORDER_SECONDARY = "#00ffff"
    BORDER_ACCENT = "#ff00ff"

    TEXT_PRIMARY = "#00ff00"
    TEXT_SECONDARY = "#00ffff"
    TEXT_TERTIARY = "#ffffff"
    TEXT_DIM = "#888888"

    # Fonts
    FONT_MONO_SMALL = ("Courier New", 8)
    FONT_MONO = ("Courier New", 10)
    FONT_MONO_BOLD = ("Courier New", 10, "bold")
    FONT_MONO_LARGE = ("Courier New", 12, "bold")
    FONT_TITLE = ("Courier New", 18, "bold")
    FONT_HEADER = ("Courier New", 14, "bold")
    FONT_SUBHEADER = ("Courier New", 12, "bold")

    # Border widths
    BORDER_THIN = 1
    BORDER_MEDIUM = 2
    BORDER_THICK = 3

    # Animation speeds (ms)
    ANIM_FAST = 50
    ANIM_MEDIUM = 100
    ANIM_SLOW = 200

    # Glow intensity levels
    GLOW_LEVELS = [
        "#00ff00", "#00ee00", "#00dd00", "#00cc00",
        "#00bb00", "#00cc00", "#00dd00", "#00ee00"
    ]

# ============================================================================
# ANIMATED BORDER FRAME
# ============================================================================

class AnimatedBorderFrame(Frame):
    """Frame with animated glowing border"""

    def __init__(self, parent, border_color=EnhancedSciFiTheme.BORDER_PRIMARY,
                 animation_speed=EnhancedSciFiTheme.ANIM_MEDIUM, **kwargs):
        super().__init__(parent, **kwargs)

        self.border_color = border_color
        self.animation_speed = animation_speed
        self.animation_state = 0
        self.animating = False

        # Create canvas for border
        self.canvas = Canvas(self, bg=EnhancedSciFiTheme.BG_BLACK,
                            highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Inner frame for content
        self.inner_frame = Frame(self.canvas, bg=EnhancedSciFiTheme.BG_DARK)
        self.canvas.create_window(0, 0, window=self.inner_frame, anchor=tk.NW)

        # Bind resize
        self.canvas.bind('<Configure>', self._on_resize)

    def start_animation(self):
        """Start border animation"""
        self.animating = True
        self._animate_border()

    def stop_animation(self):
        """Stop border animation"""
        self.animating = False

    def _animate_border(self):
        """Animate the border glow"""
        if not self.animating:
            return

        self.canvas.delete('border')
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()

        # Calculate glow intensity
        glow_index = self.animation_state % len(EnhancedSciFiTheme.GLOW_LEVELS)
        color = EnhancedSciFiTheme.GLOW_LEVELS[glow_index]

        # Draw animated border
        thickness = 3
        self.canvas.create_rectangle(0, 0, w, h, outline=color,
                                     width=thickness, tags='border')

        # Draw corner accents
        corner_size = 20
        self.canvas.create_line(0, 0, corner_size, 0, fill=color,
                               width=thickness, tags='border')
        self.canvas.create_line(0, 0, 0, corner_size, fill=color,
                               width=thickness, tags='border')

        self.animation_state += 1
        self.after(self.animation_speed, self._animate_border)

    def _on_resize(self, event):
        """Handle resize event"""
        self.canvas.itemconfig(self.inner_frame, width=event.width, height=event.height)

# ============================================================================
# SCANLINE EFFECT CANVAS
# ============================================================================

class ScanlineCanvas(Canvas):
    """Canvas with CRT scanline effect"""

    def __init__(self, parent, scanline_speed=3, **kwargs):
        super().__init__(parent, **kwargs)

        self.scanline_speed = scanline_speed
        self.scanline_pos = 0
        self.scanline_enabled = True

        self.start_scanlines()

    def start_scanlines(self):
        """Start scanline animation"""
        self.scanline_enabled = True
        self._animate_scanlines()

    def stop_scanlines(self):
        """Stop scanline animation"""
        self.scanline_enabled = False

    def _animate_scanlines(self):
        """Animate CRT scanlines"""
        if not self.scanline_enabled:
            return

        self.delete('scanline')

        h = self.winfo_height()
        if h <= 1:
            self.after(50, self._animate_scanlines)
            return

        # Draw scanline
        y = self.scanline_pos % h
        self.create_line(0, y, self.winfo_width(), y,
                        fill=EnhancedSciFiTheme.GREEN_BRIGHT,
                        width=2, tags='scanline')

        # Draw fading trail
        for i in range(1, 5):
            trail_y = (y - i * 10) % h
            opacity = 255 - (i * 50)
            if opacity > 0:
                trail_color = f"#{opacity:02x}{opacity:02x}{opacity:02x}"
                self.create_line(0, trail_y, self.winfo_width(), trail_y,
                               fill=EnhancedSciFiTheme.GREEN_DIM,
                               width=1, tags='scanline')

        self.scanline_pos += self.scanline_speed
        self.after(30, self._animate_scanlines)

# ============================================================================
# DATA STREAM WIDGET
# ============================================================================

class DataStreamWidget(Canvas):
    """Animated data stream display (Matrix-style)"""

    def __init__(self, parent, stream_count=10, **kwargs):
        super().__init__(parent, bg=EnhancedSciFiTheme.BG_BLACK,
                        highlightthickness=0, **kwargs)

        self.stream_count = stream_count
        self.streams = []
        self.running = False

        # Character pool for data stream
        self.chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノ"

        self.start_stream()

    def start_stream(self):
        """Start data stream animation"""
        self.running = True
        # Wait a bit for the widget to be properly sized
        self.after(100, self._initialize_streams)

    def _initialize_streams(self):
        """Initialize stream positions after widget is sized"""
        # Initialize streams with proper width
        w = self.winfo_width()
        if w <= 1:
            w = 400  # Default width

        # Clear any existing streams
        self.streams = []

        # Calculate stream spacing to center them
        stream_spacing = w / (self.stream_count + 1)

        for i in range(self.stream_count):
            x = int(stream_spacing * (i + 1))
            self.streams.append({
                'x': x,
                'y': -50 - (i * 30),  # Stagger initial positions
                'speed': 2 + (i % 3),
                'length': 10 + (i % 10),
                'chars': []
            })

        self._animate_stream()

    def stop_stream(self):
        """Stop data stream"""
        self.running = False

    def _animate_stream(self):
        """Animate the data streams"""
        if not self.running:
            return

        self.delete('stream')

        h = self.winfo_height() or 300

        for stream in self.streams:
            # Update position
            stream['y'] += stream['speed']

            # Reset if off screen
            if stream['y'] > h + 100:
                stream['y'] = -50

            # Draw stream
            for i in range(stream['length']):
                y = stream['y'] - (i * 15)
                if 0 <= y <= h:
                    # Calculate color (fade from bright to dark)
                    if i == 0:
                        color = EnhancedSciFiTheme.GREEN_BRIGHT
                    elif i < 3:
                        color = EnhancedSciFiTheme.GREEN_MEDIUM
                    else:
                        color = EnhancedSciFiTheme.GREEN_DIM

                    # Random character
                    char = self.chars[int(time.time() * 1000 + i) % len(self.chars)]

                    self.create_text(stream['x'], y, text=char,
                                   fill=color, font=EnhancedSciFiTheme.FONT_MONO,
                                   tags='stream')

        self.after(50, self._animate_stream)

# ============================================================================
# GLOWING BUTTON
# ============================================================================

class GlowButton(Canvas):
    """Button with glowing effect"""

    def __init__(self, parent, text="BUTTON", command=None,
                 width=150, height=40, **kwargs):
        super().__init__(parent, width=width, height=height,
                        bg=EnhancedSciFiTheme.BG_DARK,
                        highlightthickness=0, **kwargs)

        self.text = text
        self.command = command
        self.glow_state = 0
        self.is_pressed = False
        self.is_hovered = False

        self.draw_button()

        # Bind events
        self.bind('<Button-1>', self._on_press)
        self.bind('<ButtonRelease-1>', self._on_release)
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)

        # Start glow animation
        self._animate_glow()

    def draw_button(self):
        """Draw the button"""
        self.delete('all')

        w = self.winfo_width() or 150
        h = self.winfo_height() or 40

        # Determine colors based on state
        if self.is_pressed:
            bg_color = EnhancedSciFiTheme.GREEN_BRIGHT
            text_color = EnhancedSciFiTheme.BG_BLACK
            border_color = EnhancedSciFiTheme.GREEN_BRIGHT
        elif self.is_hovered:
            bg_color = EnhancedSciFiTheme.BG_LIGHT
            text_color = EnhancedSciFiTheme.GREEN_BRIGHT
            border_color = EnhancedSciFiTheme.GREEN_BRIGHT
        else:
            bg_color = EnhancedSciFiTheme.BG_MEDIUM
            text_color = EnhancedSciFiTheme.GREEN_GLOW
            # Use glow animation
            glow_index = self.glow_state % len(EnhancedSciFiTheme.GLOW_LEVELS)
            border_color = EnhancedSciFiTheme.GLOW_LEVELS[glow_index]

        # Draw background
        self.create_rectangle(2, 2, w-2, h-2, fill=bg_color,
                            outline=border_color, width=2, tags='bg')

        # Draw corner decorations
        corner_size = 8
        self.create_line(2, 2, corner_size, 2, fill=border_color, width=3)
        self.create_line(2, 2, 2, corner_size, fill=border_color, width=3)

        self.create_line(w-2, 2, w-corner_size, 2, fill=border_color, width=3)
        self.create_line(w-2, 2, w-2, corner_size, fill=border_color, width=3)

        # Draw text
        self.create_text(w//2, h//2, text=self.text,
                        fill=text_color, font=EnhancedSciFiTheme.FONT_MONO_BOLD,
                        tags='text')

    def _animate_glow(self):
        """Animate button glow"""
        if not self.is_pressed:
            self.glow_state += 1
            self.draw_button()

        self.after(150, self._animate_glow)

    def _on_press(self, event):
        """Handle button press"""
        self.is_pressed = True
        self.draw_button()

    def _on_release(self, event):
        """Handle button release"""
        self.is_pressed = False
        self.draw_button()

        if self.command and self.is_hovered:
            self.command()

    def _on_enter(self, event):
        """Handle mouse enter"""
        self.is_hovered = True
        self.draw_button()

    def _on_leave(self, event):
        """Handle mouse leave"""
        self.is_hovered = False
        self.is_pressed = False
        self.draw_button()

# ============================================================================
# HEX DISPLAY PANEL
# ============================================================================

class HexDisplayPanel(Frame):
    """Hexadecimal data display panel"""

    def __init__(self, parent, width=400, height=200, **kwargs):
        super().__init__(parent, bg=EnhancedSciFiTheme.BG_BLACK, **kwargs)

        self.canvas = Canvas(self, bg=EnhancedSciFiTheme.BG_BLACK,
                            highlightthickness=0, width=width, height=height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.data_offset = 0
        self.scrolling = True

        self.start_scroll()

    def start_scroll(self):
        """Start scrolling hex data"""
        self.scrolling = True
        self._animate_hex()

    def stop_scroll(self):
        """Stop scrolling"""
        self.scrolling = False

    def _generate_hex_line(self, offset):
        """Generate a line of hex data"""
        hex_data = f"{offset:08X}  "

        # Generate 16 bytes of "data"
        for i in range(16):
            hex_data += f"{((offset + i) * 37) % 256:02X} "

        return hex_data

    def _animate_hex(self):
        """Animate scrolling hex dump"""
        if not self.scrolling:
            return

        self.canvas.delete('hex')

        h = self.canvas.winfo_height() or 200
        line_height = 15
        num_lines = h // line_height + 2

        y_offset = -(self.data_offset % line_height)

        for i in range(num_lines):
            y = y_offset + (i * line_height)
            offset = ((self.data_offset // line_height) + i) * 16

            hex_line = self._generate_hex_line(offset)

            # Alternate colors for readability
            color = EnhancedSciFiTheme.GREEN_GLOW if i % 2 == 0 else EnhancedSciFiTheme.GREEN_MEDIUM

            self.canvas.create_text(5, y, text=hex_line, anchor=tk.NW,
                                  fill=color, font=EnhancedSciFiTheme.FONT_MONO_SMALL,
                                  tags='hex')

        self.data_offset += 1
        self.after(50, self._animate_hex)

# ============================================================================
# CIRCULAR GAUGE WIDGET
# ============================================================================

class CircularGauge(Canvas):
    """Circular gauge for displaying metrics"""

    def __init__(self, parent, label="METRIC", min_val=0, max_val=100,
                 size=150, **kwargs):
        super().__init__(parent, width=size, height=size,
                        bg=EnhancedSciFiTheme.BG_DARK,
                        highlightthickness=0, **kwargs)

        self.label = label
        self.min_val = min_val
        self.max_val = max_val
        self.current_val = 0
        self.target_val = 0
        self.size = size

        self.draw_gauge()
        self._animate_value()

    def set_value(self, value):
        """Set gauge value with smooth animation"""
        self.target_val = max(self.min_val, min(self.max_val, value))

    def draw_gauge(self):
        """Draw the gauge"""
        self.delete('all')

        cx = self.size // 2
        cy = self.size // 2
        radius = self.size // 2 - 20

        # Draw outer circle
        self.create_oval(cx - radius, cy - radius,
                        cx + radius, cy + radius,
                        outline=EnhancedSciFiTheme.GREEN_DIM,
                        width=2)

        # Draw inner circle
        inner_radius = radius - 10
        self.create_oval(cx - inner_radius, cy - inner_radius,
                        cx + inner_radius, cy + inner_radius,
                        outline=EnhancedSciFiTheme.GREEN_DARK,
                        width=1)

        # Calculate arc for current value
        percentage = (self.current_val - self.min_val) / (self.max_val - self.min_val)
        arc_extent = percentage * 270  # 270 degrees max

        # Determine color based on value
        if percentage < 0.5:
            color = EnhancedSciFiTheme.GREEN_GLOW
        elif percentage < 0.75:
            color = EnhancedSciFiTheme.STATUS_WARNING
        else:
            color = EnhancedSciFiTheme.STATUS_CRITICAL

        # Draw value arc
        if arc_extent > 0:
            self.create_arc(cx - radius, cy - radius,
                          cx + radius, cy + radius,
                          start=135, extent=arc_extent,
                          outline=color, width=4, style=tk.ARC)

        # Draw tick marks
        for i in range(0, 280, 30):
            angle = math.radians(135 + i)
            x1 = cx + (radius - 5) * math.cos(angle)
            y1 = cy + (radius - 5) * math.sin(angle)
            x2 = cx + radius * math.cos(angle)
            y2 = cy + radius * math.sin(angle)

            self.create_line(x1, y1, x2, y2,
                           fill=EnhancedSciFiTheme.GREEN_MEDIUM, width=2)

        # Draw value text
        self.create_text(cx, cy - 10, text=f"{self.current_val:.1f}",
                        fill=color, font=EnhancedSciFiTheme.FONT_MONO_LARGE)

        # Draw label
        self.create_text(cx, cy + 15, text=self.label,
                        fill=EnhancedSciFiTheme.GREEN_MEDIUM,
                        font=EnhancedSciFiTheme.FONT_MONO_SMALL)

    def _animate_value(self):
        """Animate value change"""
        # Smooth transition to target
        if abs(self.current_val - self.target_val) > 0.1:
            diff = self.target_val - self.current_val
            self.current_val += diff * 0.1
            self.draw_gauge()

        self.after(50, self._animate_value)

# Save indicator that part 1 is complete
if __name__ == "__main__":
    print("ARCHITECT v3.0 Enhanced GUI - Part 1: Theme and Animated Widgets")
    print("Components created:")
    print("  ✓ EnhancedSciFiTheme")
    print("  ✓ AnimatedBorderFrame")
    print("  ✓ ScanlineCanvas")
    print("  ✓ DataStreamWidget")
    print("  ✓ GlowButton")
    print("  ✓ HexDisplayPanel")
    print("  ✓ CircularGauge")
