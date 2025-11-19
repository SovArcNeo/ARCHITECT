#!/usr/bin/env python3
"""
ARCHITECT SYSTEM v3.0 - ENHANCED SCI-FI GUI (PART 2)
Advanced Visualization Panels
Neural Network Graphs, Threat Maps, Network Topology
"""

import tkinter as tk
from tkinter import Canvas, Frame, Label, Scrollbar
import math
import random
from typing import List, Dict, Tuple, Optional
from collections import deque
from datetime import datetime

# Import Part 1 components
import sys
sys.path.insert(0, '/home/cdavenport795/ARCHITECT SYSTEM')
from ARCHITECT_SA_v3_0_ENHANCED_GUI_PART1 import EnhancedSciFiTheme

# ============================================================================
# NEURAL NETWORK VISUALIZATION
# ============================================================================

class NeuralNetworkVisualization(Canvas):
    """Visual representation of neural network architecture"""

    def __init__(self, parent, layers=[20, 64, 32, 8], width=600, height=400, **kwargs):
        super().__init__(parent, width=width, height=height,
                        bg=EnhancedSciFiTheme.BG_BLACK,
                        highlightthickness=0, **kwargs)

        self.layers = layers
        self.width = width
        self.height = height
        self.neuron_positions = []
        self.activation_values = {}
        self.animation_frame = 0

        self.calculate_positions()
        self.draw_network()
        self.start_animation()

    def calculate_positions(self):
        """Calculate neuron positions"""
        self.neuron_positions = []

        num_layers = len(self.layers)
        layer_spacing = self.width / (num_layers + 1)

        for layer_idx, num_neurons in enumerate(self.layers):
            layer_positions = []
            x = (layer_idx + 1) * layer_spacing

            # Limit displayed neurons for large layers
            display_neurons = min(num_neurons, 16)
            neuron_spacing = self.height / (display_neurons + 1)

            for neuron_idx in range(display_neurons):
                y = (neuron_idx + 1) * neuron_spacing
                layer_positions.append((x, y))

            self.neuron_positions.append(layer_positions)

    def draw_network(self):
        """Draw the neural network"""
        self.delete('all')

        # Draw connections
        for layer_idx in range(len(self.neuron_positions) - 1):
            current_layer = self.neuron_positions[layer_idx]
            next_layer = self.neuron_positions[layer_idx + 1]

            for i, (x1, y1) in enumerate(current_layer):
                for j, (x2, y2) in enumerate(next_layer):
                    # Simulate activation strength
                    activation = self.activation_values.get((layer_idx, i, j), 0.3)

                    # Color based on activation
                    if activation > 0.7:
                        color = EnhancedSciFiTheme.GREEN_BRIGHT
                        width = 2
                    elif activation > 0.4:
                        color = EnhancedSciFiTheme.GREEN_MEDIUM
                        width = 1
                    else:
                        color = EnhancedSciFiTheme.GREEN_DARK
                        width = 1

                    self.create_line(x1, y1, x2, y2, fill=color,
                                   width=width, tags='connection')

        # Draw neurons
        for layer_idx, layer in enumerate(self.neuron_positions):
            for neuron_idx, (x, y) in enumerate(layer):
                # Get activation value
                activation = self.activation_values.get((layer_idx, neuron_idx), 0.5)

                # Color based on activation
                if activation > 0.8:
                    fill_color = EnhancedSciFiTheme.GREEN_BRIGHT
                    outline_color = EnhancedSciFiTheme.GREEN_BRIGHT
                elif activation > 0.5:
                    fill_color = EnhancedSciFiTheme.GREEN_MEDIUM
                    outline_color = EnhancedSciFiTheme.GREEN_GLOW
                else:
                    fill_color = EnhancedSciFiTheme.BG_DARK
                    outline_color = EnhancedSciFiTheme.GREEN_DIM

                radius = 8
                self.create_oval(x - radius, y - radius,
                               x + radius, y + radius,
                               fill=fill_color, outline=outline_color,
                               width=2, tags='neuron')

        # Draw layer labels
        for layer_idx, num_neurons in enumerate(self.layers):
            x = self.neuron_positions[layer_idx][0][0]
            label = f"L{layer_idx}\n({num_neurons})"
            self.create_text(x, 20, text=label,
                           fill=EnhancedSciFiTheme.GREEN_GLOW,
                           font=EnhancedSciFiTheme.FONT_MONO_SMALL)

    def start_animation(self):
        """Start network activity animation"""
        self._animate_activity()

    def _animate_activity(self):
        """Simulate neural network activity"""
        # Randomize some activations to show "thinking"
        for layer_idx in range(len(self.layers)):
            for neuron_idx in range(min(self.layers[layer_idx], 16)):
                # Use sine wave for smooth animation
                base = math.sin(self.animation_frame * 0.1 + neuron_idx * 0.3)
                activation = (base + 1) / 2  # Normalize to 0-1
                self.activation_values[(layer_idx, neuron_idx)] = activation

        # Randomize connections
        for layer_idx in range(len(self.layers) - 1):
            for i in range(min(self.layers[layer_idx], 16)):
                for j in range(min(self.layers[layer_idx + 1], 16)):
                    if random.random() < 0.1:  # 10% chance to update
                        self.activation_values[(layer_idx, i, j)] = random.random()

        self.draw_network()
        self.animation_frame += 1
        self.after(100, self._animate_activity)

    def set_activations(self, layer_activations: Dict):
        """Set specific activation values from real neural network"""
        self.activation_values.update(layer_activations)
        self.draw_network()

# ============================================================================
# THREAT MAP VISUALIZATION
# ============================================================================

class ThreatMapVisualization(Canvas):
    """Visual threat map showing IP addresses and threat levels"""

    def __init__(self, parent, width=800, height=600, **kwargs):
        super().__init__(parent, width=width, height=height,
                        bg=EnhancedSciFiTheme.BG_BLACK,
                        highlightthickness=0, **kwargs)

        self.width = width
        self.height = height
        self.threats = []  # List of (x, y, level, ip) tuples
        self.radar_angle = 0

        self.draw_map()
        self.start_radar()

    def add_threat(self, ip_address: str, threat_level: int, x: Optional[int] = None,
                   y: Optional[int] = None):
        """Add a threat to the map"""
        if x is None:
            x = random.randint(50, self.width - 50)
        if y is None:
            y = random.randint(50, self.height - 50)

        self.threats.append({
            'ip': ip_address,
            'x': x,
            'y': y,
            'level': threat_level,
            'pulse': 0
        })

        # Limit threat history
        if len(self.threats) > 100:
            self.threats.pop(0)

    def draw_map(self):
        """Draw the threat map"""
        self.delete('threats')

        # Draw grid
        grid_spacing = 50
        for x in range(0, self.width, grid_spacing):
            self.create_line(x, 0, x, self.height,
                           fill=EnhancedSciFiTheme.GREEN_DARK,
                           width=1, tags='grid')

        for y in range(0, self.height, grid_spacing):
            self.create_line(0, y, self.width, y,
                           fill=EnhancedSciFiTheme.GREEN_DARK,
                           width=1, tags='grid')

        # Draw threats
        for threat in self.threats:
            x, y = threat['x'], threat['y']
            level = threat['level']
            ip = threat['ip']

            # Color based on threat level
            if level >= 6:  # Critical
                color = EnhancedSciFiTheme.THREAT_CRITICAL
                radius = 15
            elif level >= 4:  # High
                color = EnhancedSciFiTheme.THREAT_HIGH
                radius = 12
            elif level >= 2:  # Medium
                color = EnhancedSciFiTheme.THREAT_MEDIUM
                radius = 10
            else:  # Low
                color = EnhancedSciFiTheme.THREAT_LOW
                radius = 8

            # Pulsing effect
            pulse_offset = threat['pulse'] % 10
            pulse_radius = radius + pulse_offset

            # Draw pulse rings
            self.create_oval(x - pulse_radius, y - pulse_radius,
                           x + pulse_radius, y + pulse_radius,
                           outline=color, width=1, tags='threats')

            # Draw threat marker
            self.create_oval(x - radius, y - radius,
                           x + radius, y + radius,
                           fill=color, outline=EnhancedSciFiTheme.GREEN_BRIGHT,
                           width=2, tags='threats')

            # Draw IP label
            self.create_text(x, y - radius - 10, text=ip,
                           fill=color, font=EnhancedSciFiTheme.FONT_MONO_SMALL,
                           tags='threats')

            threat['pulse'] += 1

    def start_radar(self):
        """Start radar sweep animation"""
        self._animate_radar()

    def _animate_radar(self):
        """Animate radar sweep"""
        self.delete('radar')

        cx = self.width // 2
        cy = self.height // 2
        max_radius = min(self.width, self.height) // 2 - 20

        # Draw radar circles
        for r in range(max_radius // 4, max_radius, max_radius // 4):
            self.create_oval(cx - r, cy - r, cx + r, cy + r,
                           outline=EnhancedSciFiTheme.CYAN_DIM,
                           width=1, tags='radar')

        # Draw radar sweep line
        angle = math.radians(self.radar_angle)
        x2 = cx + max_radius * math.cos(angle)
        y2 = cy + max_radius * math.sin(angle)

        self.create_line(cx, cy, x2, y2,
                        fill=EnhancedSciFiTheme.CYAN_BRIGHT,
                        width=2, tags='radar')

        # Draw fading arc
        self.create_arc(cx - max_radius, cy - max_radius,
                       cx + max_radius, cy + max_radius,
                       start=self.radar_angle - 30, extent=30,
                       outline=EnhancedSciFiTheme.CYAN_DIM,
                       width=1, style=tk.ARC, tags='radar')

        self.radar_angle = (self.radar_angle + 2) % 360
        self.draw_map()
        self.after(50, self._animate_radar)

# ============================================================================
# NETWORK TOPOLOGY VISUALIZATION
# ============================================================================

class NetworkTopologyVisualization(Canvas):
    """Network topology graph visualization"""

    def __init__(self, parent, width=800, height=600, **kwargs):
        super().__init__(parent, width=width, height=height,
                        bg=EnhancedSciFiTheme.BG_BLACK,
                        highlightthickness=0, **kwargs)

        self.width = width
        self.height = height
        self.nodes = {}  # {ip: {'x': x, 'y': y, 'connections': []}}
        self.packets = []  # Animated packets traveling between nodes

        self.draw_topology()
        self.start_packet_animation()

    def add_node(self, ip_address: str, node_type: str = 'host',
                 x: Optional[int] = None, y: Optional[int] = None):
        """Add a node to the topology"""
        if ip_address not in self.nodes:
            if x is None or y is None:
                x = random.randint(100, self.width - 100)
                y = random.randint(100, self.height - 100)

            self.nodes[ip_address] = {
                'x': x,
                'y': y,
                'type': node_type,
                'connections': [],
                'active': True,
                'threat_level': 0
            }

    def add_connection(self, ip1: str, ip2: str):
        """Add connection between nodes"""
        if ip1 in self.nodes and ip2 in self.nodes:
            if ip2 not in self.nodes[ip1]['connections']:
                self.nodes[ip1]['connections'].append(ip2)

            # Create animated packet
            self.packets.append({
                'from': ip1,
                'to': ip2,
                'progress': 0.0,
                'color': EnhancedSciFiTheme.GREEN_BRIGHT
            })

    def draw_topology(self):
        """Draw the network topology"""
        self.delete('topology')

        # Draw connections
        for ip, node in self.nodes.items():
            x1, y1 = node['x'], node['y']

            for connected_ip in node['connections']:
                if connected_ip in self.nodes:
                    connected_node = self.nodes[connected_ip]
                    x2, y2 = connected_node['x'], connected_node['y']

                    # Draw connection line
                    self.create_line(x1, y1, x2, y2,
                                   fill=EnhancedSciFiTheme.GREEN_DIM,
                                   width=1, tags='topology')

        # Draw nodes
        for ip, node in self.nodes.items():
            x, y = node['x'], node['y']
            node_type = node['type']
            threat_level = node.get('threat_level', 0)

            # Size and color based on type and threat
            if node_type == 'server':
                radius = 20
                shape = 'square'
            elif node_type == 'router':
                radius = 18
                shape = 'diamond'
            else:  # host
                radius = 15
                shape = 'circle'

            # Color based on threat level
            if threat_level > 5:
                color = EnhancedSciFiTheme.THREAT_CRITICAL
            elif threat_level > 3:
                color = EnhancedSciFiTheme.THREAT_HIGH
            elif threat_level > 1:
                color = EnhancedSciFiTheme.THREAT_MEDIUM
            else:
                color = EnhancedSciFiTheme.GREEN_GLOW

            # Draw node shape
            if shape == 'circle':
                self.create_oval(x - radius, y - radius,
                               x + radius, y + radius,
                               fill=EnhancedSciFiTheme.BG_MEDIUM,
                               outline=color, width=3, tags='topology')
            elif shape == 'square':
                self.create_rectangle(x - radius, y - radius,
                                    x + radius, y + radius,
                                    fill=EnhancedSciFiTheme.BG_MEDIUM,
                                    outline=color, width=3, tags='topology')
            elif shape == 'diamond':
                points = [x, y - radius, x + radius, y,
                         x, y + radius, x - radius, y]
                self.create_polygon(points, fill=EnhancedSciFiTheme.BG_MEDIUM,
                                  outline=color, width=3, tags='topology')

            # Draw IP label
            self.create_text(x, y + radius + 15, text=ip,
                           fill=color, font=EnhancedSciFiTheme.FONT_MONO_SMALL,
                           tags='topology')

    def draw_packets(self):
        """Draw animated packets"""
        self.delete('packets')

        packets_to_remove = []

        for i, packet in enumerate(self.packets):
            from_ip = packet['from']
            to_ip = packet['to']

            if from_ip in self.nodes and to_ip in self.nodes:
                from_node = self.nodes[from_ip]
                to_node = self.nodes[to_ip]

                # Calculate packet position
                progress = packet['progress']
                x = from_node['x'] + (to_node['x'] - from_node['x']) * progress
                y = from_node['y'] + (to_node['y'] - from_node['y']) * progress

                # Draw packet
                radius = 5
                self.create_oval(x - radius, y - radius,
                               x + radius, y + radius,
                               fill=packet['color'],
                               outline=EnhancedSciFiTheme.GREEN_BRIGHT,
                               tags='packets')

                # Update progress
                packet['progress'] += 0.02

                if packet['progress'] >= 1.0:
                    packets_to_remove.append(i)

        # Remove completed packets
        for i in reversed(packets_to_remove):
            self.packets.pop(i)

    def start_packet_animation(self):
        """Start packet animation"""
        self._animate_packets()

    def _animate_packets(self):
        """Animate network packets"""
        self.draw_packets()
        self.draw_topology()
        self.after(50, self._animate_packets)

# ============================================================================
# REAL-TIME GRAPH WIDGET
# ============================================================================

class RealTimeGraph(Canvas):
    """Real-time scrolling graph for metrics"""

    def __init__(self, parent, title="METRIC", max_points=100,
                 min_val=0, max_val=100, width=400, height=200, **kwargs):
        super().__init__(parent, width=width, height=height,
                        bg=EnhancedSciFiTheme.BG_BLACK,
                        highlightthickness=0, **kwargs)

        self.title = title
        self.max_points = max_points
        self.min_val = min_val
        self.max_val = max_val
        self.data_points = deque(maxlen=max_points)
        self.width = width
        self.height = height

        # Initialize with zeros
        for _ in range(max_points):
            self.data_points.append(0)

        self.draw_graph()

    def add_data_point(self, value: float):
        """Add a new data point"""
        self.data_points.append(value)
        self.draw_graph()

    def draw_graph(self):
        """Draw the graph"""
        self.delete('all')

        # Draw title
        self.create_text(self.width // 2, 15, text=self.title,
                        fill=EnhancedSciFiTheme.GREEN_GLOW,
                        font=EnhancedSciFiTheme.FONT_MONO_BOLD)

        # Draw grid
        graph_top = 40
        graph_bottom = self.height - 30
        graph_height = graph_bottom - graph_top

        # Horizontal grid lines
        for i in range(5):
            y = graph_top + (graph_height * i // 4)
            self.create_line(30, y, self.width - 10, y,
                           fill=EnhancedSciFiTheme.GREEN_DARK,
                           width=1)

            # Y-axis label
            value = self.max_val - (self.max_val - self.min_val) * i / 4
            self.create_text(15, y, text=f"{value:.0f}",
                           fill=EnhancedSciFiTheme.GREEN_MEDIUM,
                           font=EnhancedSciFiTheme.FONT_MONO_SMALL)

        # Draw data line
        if len(self.data_points) > 1:
            points = []
            graph_width = self.width - 40

            for i, value in enumerate(self.data_points):
                x = 30 + (i * graph_width / self.max_points)

                # Normalize value
                normalized = (value - self.min_val) / (self.max_val - self.min_val)
                normalized = max(0, min(1, normalized))

                y = graph_bottom - (normalized * graph_height)

                points.extend([x, y])

            if len(points) >= 4:
                self.create_line(points, fill=EnhancedSciFiTheme.GREEN_BRIGHT,
                               width=2, smooth=True)

                # Fill area under curve
                fill_points = [30, graph_bottom] + points + [self.width - 10, graph_bottom]
                self.create_polygon(fill_points,
                                  fill=EnhancedSciFiTheme.GREEN_DARK,
                                  outline='', stipple='gray25')

        # Draw axes
        self.create_line(30, graph_top, 30, graph_bottom,
                        fill=EnhancedSciFiTheme.GREEN_GLOW, width=2)
        self.create_line(30, graph_bottom, self.width - 10, graph_bottom,
                        fill=EnhancedSciFiTheme.GREEN_GLOW, width=2)

# ============================================================================
# MATRIX RAIN BACKGROUND
# ============================================================================

class MatrixRainBackground(Canvas):
    """Full Matrix digital rain background effect"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg=EnhancedSciFiTheme.BG_BLACK,
                        highlightthickness=0, **kwargs)

        self.streams = []
        self.chars = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン01"
        self.running = False

        self.bind('<Configure>', self._on_resize)

    def start(self):
        """Start matrix rain"""
        self.running = True
        self._initialize_streams()
        self._animate()

    def stop(self):
        """Stop matrix rain"""
        self.running = False

    def _on_resize(self, event):
        """Handle resize"""
        if self.running:
            self._initialize_streams()

    def _initialize_streams(self):
        """Initialize rain streams"""
        w = self.winfo_width() or 800
        num_streams = w // 20

        self.streams = []
        for i in range(num_streams):
            self.streams.append({
                'x': i * 20,
                'y': random.randint(-500, 0),
                'speed': random.randint(2, 5),
                'length': random.randint(10, 30)
            })

    def _animate(self):
        """Animate matrix rain"""
        if not self.running:
            return

        self.delete('rain')

        h = self.winfo_height() or 600

        for stream in self.streams:
            stream['y'] += stream['speed']

            if stream['y'] > h + 100:
                stream['y'] = -100
                stream['speed'] = random.randint(2, 5)
                stream['length'] = random.randint(10, 30)

            # Draw characters
            for i in range(stream['length']):
                y = stream['y'] - (i * 20)

                if 0 <= y <= h:
                    # Brightness gradient
                    if i == 0:
                        color = EnhancedSciFiTheme.GREEN_BRIGHT
                    elif i < 5:
                        color = EnhancedSciFiTheme.GREEN_GLOW
                    elif i < 10:
                        color = EnhancedSciFiTheme.GREEN_MEDIUM
                    else:
                        color = EnhancedSciFiTheme.GREEN_DIM

                    char = random.choice(self.chars)
                    self.create_text(stream['x'], y, text=char,
                                   fill=color, font=EnhancedSciFiTheme.FONT_MONO,
                                   tags='rain')

        self.after(50, self._animate)

# Test components
if __name__ == "__main__":
    print("ARCHITECT v3.0 Enhanced GUI - Part 2: Advanced Visualization Panels")
    print("Components created:")
    print("  ✓ NeuralNetworkVisualization")
    print("  ✓ ThreatMapVisualization")
    print("  ✓ NetworkTopologyVisualization")
    print("  ✓ RealTimeGraph")
    print("  ✓ MatrixRainBackground")
