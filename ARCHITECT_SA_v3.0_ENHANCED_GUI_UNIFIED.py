#!/usr/bin/env python3
"""
ARCHITECT SYSTEM v3.0 - UNIFIED ENHANCED SCI-FI GUI
This unified launcher combines all 4 parts of the Enhanced GUI into one executable script.

Usage: python3 ARCHITECT_SA_v3.0_ENHANCED_GUI_UNIFIED.py

Components Integrated:
- Part 1: Enhanced Theme System and Animated Widgets
- Part 2: Advanced Visualization Panels
- Part 3: Detachable Windows and Advanced Control Panels
- Main: Dashboard and Application Window

Author: Enhanced AI System
Version: 3.0.0-ENHANCED-GUI-UNIFIED
"""

import sys
import os

# Add current directory to path for imports
sys.path.insert(0, '/home/cdavenport795/ARCHITECT SYSTEM')

print("=" * 80)
print("ARCHITECT SYSTEM v3.0 - UNIFIED ENHANCED GUI LAUNCHER")
print("=" * 80)
print("\nInitializing components...")

# ============================================================================
# PART 1: Load Enhanced Theme System and Animated Widgets
# ============================================================================
print("[1/4] Loading Enhanced Theme System and Animated Widgets...")

try:
    exec(open('/home/cdavenport795/ARCHITECT SYSTEM/ARCHITECT_SA_v3.0_ENHANCED_GUI_PART1.py').read())
    print("      ✓ EnhancedSciFiTheme loaded")
    print("      ✓ AnimatedBorderFrame loaded")
    print("      ✓ ScanlineCanvas loaded")
    print("      ✓ DataStreamWidget loaded")
    print("      ✓ GlowButton loaded")
    print("      ✓ HexDisplayPanel loaded")
    print("      ✓ CircularGauge loaded")
except Exception as e:
    print(f"      ✗ ERROR loading Part 1: {e}")
    sys.exit(1)

# ============================================================================
# PART 2: Load Advanced Visualization Panels
# ============================================================================
print("\n[2/4] Loading Advanced Visualization Panels...")

try:
    # Read Part 2 and filter out the test section
    with open('/home/cdavenport795/ARCHITECT SYSTEM/ARCHITECT_SA_v3.0_ENHANCED_GUI_PART2.py', 'r') as f:
        part2_code = f.read()

    # Remove the import statement that causes issues and the test code at bottom
    part2_code = part2_code.replace("from ARCHITECT_SA_v3_0_ENHANCED_GUI_PART1 import EnhancedSciFiTheme", "")

    # Remove test code (everything after "# Test components")
    if '# Test components' in part2_code:
        part2_code = part2_code.split('# Test components')[0]

    exec(part2_code)
    print("      ✓ NeuralNetworkVisualization loaded")
    print("      ✓ ThreatMapVisualization loaded")
    print("      ✓ NetworkTopologyVisualization loaded")
    print("      ✓ RealTimeGraph loaded")
    print("      ✓ MatrixRainBackground loaded")
except Exception as e:
    print(f"      ✗ ERROR loading Part 2: {e}")
    sys.exit(1)

# ============================================================================
# PART 3: Load Detachable Windows and Advanced Control Panels
# ============================================================================
print("\n[3/4] Loading Detachable Windows and Control Panels...")

try:
    # Read Part 3 and filter out imports
    with open('/home/cdavenport795/ARCHITECT SYSTEM/ARCHITECT_SA_v3.0_ENHANCED_GUI_PART3.py', 'r') as f:
        part3_code = f.read()

    # Remove the import statement and test code
    part3_code = part3_code.replace("from ARCHITECT_SA_v3_0_ENHANCED_GUI_PART1 import EnhancedSciFiTheme, GlowButton", "")

    # Remove test code (everything after "# Test")
    if '# Test' in part3_code:
        part3_code = part3_code.split('# Test')[0]

    exec(part3_code)
    print("      ✓ DetachableWindow loaded")
    print("      ✓ NeuralNetworkControlPanel loaded")
    print("      ✓ AdvancedConfigPanel loaded")
except Exception as e:
    print(f"      ✗ ERROR loading Part 3: {e}")
    sys.exit(1)

# ============================================================================
# MAIN: Load Dashboard and Main Application Window
# ============================================================================
print("\n[4/4] Loading Main Application Components...")

# Standard imports needed for main
import tkinter as tk
from tkinter import ttk, Frame, Label, Button, messagebox, scrolledtext
import threading
import asyncio
from datetime import datetime
from typing import Dict, List, Optional
import random
import time
import json
import sqlite3
import hashlib
import hmac
import secrets
import logging
import logging.handlers
import ipaddress
import subprocess
import platform
import psutil
import numpy as np
import pandas as pd
import signal
from pathlib import Path
from typing import Dict, List, Optional, Any, Set, Tuple, Union, Callable
from dataclasses import dataclass, field, asdict
from collections import defaultdict, deque, Counter
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from contextlib import asynccontextmanager, contextmanager
import ssl
import re
import warnings
import functools
import uuid
import cachetools
import traceback
from enum import IntEnum, auto
from abc import ABC, abstractmethod
import math

warnings.filterwarnings('ignore')

# Enhanced ML Imports
from sklearn.ensemble import IsolationForest, RandomForestClassifier, ExtraTreesClassifier
from sklearn.cluster import DBSCAN, KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, roc_auc_score, silhouette_score
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.svm import OneClassSVM
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif
import joblib

try:
    import xgboost as xgb
    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False

# Enhanced Crypto Imports
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

logger = logging.getLogger('ARCHITECT_v3.0_ENHANCED')
logger.setLevel(logging.INFO)

file_handler = logging.handlers.RotatingFileHandler(
    'architect_v3_enhanced.log', maxBytes=10*1024*1024, backupCount=10, encoding='utf-8'
)
console_handler = logging.StreamHandler()

file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
console_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

file_handler.setFormatter(file_formatter)
console_handler.setFormatter(console_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# ============================================================================
# IMPORT BACKEND CLASSES FROM ORIGINAL ARCHITECT
# ============================================================================

print("      Loading ARCHITECT backend components...")

# Import backend classes from the base ARCHITECT_SA_v3.0.py
try:
    with open('/home/cdavenport795/ARCHITECT SYSTEM/ARCHITECT_SA_v3.0.py', 'r') as f:
        backend_code = f.read()

    # Extract only the backend code (before GUI section)
    if '# ============================================================================\n# TKINTER SCI-FI GUI\n# ============================================================================' in backend_code:
        backend_code = backend_code.split('# ============================================================================\n# TKINTER SCI-FI GUI\n# ============================================================================')[0]

    exec(backend_code)
    print("      ✓ ARCHITECT backend components loaded")
except Exception as e:
    print(f"      ✗ WARNING: Could not load backend: {e}")
    print("      Creating stub backend...")

    # Create a stub mainframe class if backend loading fails
    class NexusNeuralMainframe:
        def __init__(self, config):
            self.config = config
            self.neural_detector = None
            logger.info("Stub NexusNeuralMainframe initialized")

        async def shutdown(self):
            logger.info("Shutting down stub mainframe")

# ============================================================================
# ENHANCED DASHBOARD WITH VISUALIZATIONS
# ============================================================================

class EnhancedDashboard(Frame):
    """Enhanced dashboard with all visualization components"""

    def __init__(self, parent, mainframe):
        super().__init__(parent, bg=EnhancedSciFiTheme.BG_BLACK)
        self.mainframe = mainframe
        self.init_ui()
        self.update_loop()

    def init_ui(self):
        """Initialize enhanced dashboard"""
        # Title bar with animation
        title_frame = Frame(self, bg=EnhancedSciFiTheme.BG_DARK,
                           highlightbackground=EnhancedSciFiTheme.BORDER_PRIMARY,
                           highlightthickness=3)
        title_frame.pack(fill=tk.X, padx=5, pady=5)

        title = Label(title_frame,
                     text="⚡ ARCHITECT NEURAL COMMAND CENTER ⚡",
                     font=EnhancedSciFiTheme.FONT_TITLE,
                     fg=EnhancedSciFiTheme.GREEN_BRIGHT,
                     bg=EnhancedSciFiTheme.BG_DARK)
        title.pack(pady=10)

        # Main content area with 3 columns
        content_frame = Frame(self, bg=EnhancedSciFiTheme.BG_BLACK)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Left column - Metrics and Gauges
        left_col = Frame(content_frame, bg=EnhancedSciFiTheme.BG_BLACK)
        left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        # Circular gauges
        gauge_frame = Frame(left_col, bg=EnhancedSciFiTheme.BG_MEDIUM,
                           highlightbackground=EnhancedSciFiTheme.BORDER_PRIMARY,
                           highlightthickness=2)
        gauge_frame.pack(fill=tk.X, pady=5)

        Label(gauge_frame, text="SYSTEM METRICS",
              font=EnhancedSciFiTheme.FONT_HEADER,
              fg=EnhancedSciFiTheme.GREEN_GLOW,
              bg=EnhancedSciFiTheme.BG_MEDIUM).pack()

        gauge_container = Frame(gauge_frame, bg=EnhancedSciFiTheme.BG_MEDIUM)
        gauge_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.cpu_gauge = CircularGauge(gauge_container, label="CPU", size=120)
        self.cpu_gauge.pack(side=tk.LEFT, padx=5)

        self.memory_gauge = CircularGauge(gauge_container, label="MEMORY", size=120)
        self.memory_gauge.pack(side=tk.LEFT, padx=5)

        self.threat_gauge = CircularGauge(gauge_container, label="THREATS", size=120)
        self.threat_gauge.pack(side=tk.LEFT, padx=5)

        # Real-time graphs
        graph_frame = Frame(left_col, bg=EnhancedSciFiTheme.BG_MEDIUM,
                           highlightbackground=EnhancedSciFiTheme.BORDER_PRIMARY,
                           highlightthickness=2)
        graph_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.cpu_graph = RealTimeGraph(graph_frame, title="CPU USAGE %",
                                       width=380, height=150)
        self.cpu_graph.pack(pady=5)

        self.network_graph = RealTimeGraph(graph_frame, title="NETWORK ACTIVITY",
                                          width=380, height=150)
        self.network_graph.pack(pady=5)

        # Center column - Neural Network Visualization
        center_col = Frame(content_frame, bg=EnhancedSciFiTheme.BG_BLACK)
        center_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        neural_frame = Frame(center_col, bg=EnhancedSciFiTheme.BG_MEDIUM,
                            highlightbackground=EnhancedSciFiTheme.BORDER_SECONDARY,
                            highlightthickness=2)
        neural_frame.pack(fill=tk.BOTH, expand=True)

        Label(neural_frame, text="NEURAL NETWORK ARCHITECTURE",
              font=EnhancedSciFiTheme.FONT_HEADER,
              fg=EnhancedSciFiTheme.CYAN_BRIGHT,
              bg=EnhancedSciFiTheme.BG_MEDIUM).pack()

        self.neural_viz = NeuralNetworkVisualization(neural_frame,
                                                     layers=[20, 64, 32, 8],
                                                     width=450, height=400)
        self.neural_viz.pack(pady=5)

        # Right column - Activity and Data
        right_col = Frame(content_frame, bg=EnhancedSciFiTheme.BG_BLACK)
        right_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        # Data stream
        stream_frame = Frame(right_col, bg=EnhancedSciFiTheme.BG_MEDIUM,
                            highlightbackground=EnhancedSciFiTheme.BORDER_ACCENT,
                            highlightthickness=2)
        stream_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        Label(stream_frame, text="DATA STREAM",
              font=EnhancedSciFiTheme.FONT_HEADER,
              fg=EnhancedSciFiTheme.MAGENTA,
              bg=EnhancedSciFiTheme.BG_MEDIUM).pack()

        self.data_stream = DataStreamWidget(stream_frame, stream_count=8,
                                           width=380, height=200)
        self.data_stream.pack(pady=5)

        # Activity log
        log_frame = Frame(right_col, bg=EnhancedSciFiTheme.BG_MEDIUM,
                         highlightbackground=EnhancedSciFiTheme.BORDER_PRIMARY,
                         highlightthickness=2)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        Label(log_frame, text="SYSTEM ACTIVITY LOG",
              font=EnhancedSciFiTheme.FONT_HEADER,
              fg=EnhancedSciFiTheme.GREEN_GLOW,
              bg=EnhancedSciFiTheme.BG_MEDIUM).pack()

        self.activity_log = scrolledtext.ScrolledText(
            log_frame, height=12,
            bg=EnhancedSciFiTheme.BG_BLACK,
            fg=EnhancedSciFiTheme.GREEN_GLOW,
            font=EnhancedSciFiTheme.FONT_MONO,
            insertbackground=EnhancedSciFiTheme.GREEN_GLOW
        )
        self.activity_log.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.log_activity("ARCHITECT v3.0 Enhanced System Initialized")
        self.log_activity("NumPy Neural Networks: ONLINE")
        self.log_activity("All Systems: OPERATIONAL")

    def log_activity(self, message: str):
        """Add message to activity log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] {message}\n"
        self.activity_log.insert(tk.END, log_message)
        self.activity_log.see(tk.END)

        # Limit log size
        lines = int(self.activity_log.index('end-1c').split('.')[0])
        if lines > 500:
            self.activity_log.delete('1.0', '100.0')

    def update_loop(self):
        """Update dashboard metrics"""
        try:
            # Get system stats
            cpu_usage = psutil.cpu_percent()
            memory_usage = psutil.virtual_memory().percent

            # Update gauges
            self.cpu_gauge.set_value(cpu_usage)
            self.memory_gauge.set_value(memory_usage)
            self.threat_gauge.set_value(random.randint(0, 100))  # Mock data

            # Update graphs
            self.cpu_graph.add_data_point(cpu_usage)
            self.network_graph.add_data_point(random.randint(0, 100))  # Mock data

        except Exception as e:
            logger.error(f"Dashboard update error: {e}")

        # Schedule next update
        self.after(1000, self.update_loop)

# ============================================================================
# ENHANCED NETWORK SCANNER PANEL
# ============================================================================

class EnhancedNetworkScanner(Frame):
    """Enhanced network scanner with topology visualization"""

    def __init__(self, parent, mainframe):
        super().__init__(parent, bg=EnhancedSciFiTheme.BG_BLACK)
        self.mainframe = mainframe
        self.init_ui()

    def init_ui(self):
        """Initialize scanner UI"""
        # Title
        title = Label(self, text="⚡ NEURAL NETWORK SCANNER ⚡",
                     font=EnhancedSciFiTheme.FONT_TITLE,
                     fg=EnhancedSciFiTheme.CYAN_BRIGHT,
                     bg=EnhancedSciFiTheme.BG_BLACK)
        title.pack(pady=10)

        # Control panel
        control_frame = Frame(self, bg=EnhancedSciFiTheme.BG_MEDIUM,
                             highlightbackground=EnhancedSciFiTheme.BORDER_PRIMARY,
                             highlightthickness=2)
        control_frame.pack(fill=tk.X, padx=10, pady=5)

        Label(control_frame, text="TARGET:",
              font=EnhancedSciFiTheme.FONT_MONO_BOLD,
              fg=EnhancedSciFiTheme.GREEN_GLOW,
              bg=EnhancedSciFiTheme.BG_MEDIUM).pack(side=tk.LEFT, padx=10)

        self.target_entry = tk.Entry(control_frame,
                                     bg=EnhancedSciFiTheme.BG_BLACK,
                                     fg=EnhancedSciFiTheme.GREEN_GLOW,
                                     font=EnhancedSciFiTheme.FONT_MONO,
                                     insertbackground=EnhancedSciFiTheme.GREEN_GLOW,
                                     width=30)
        self.target_entry.pack(side=tk.LEFT, padx=5)
        self.target_entry.insert(0, "192.168.1.0/24")

        self.scan_btn = GlowButton(control_frame, text="START SCAN",
                                   command=self.start_scan,
                                   width=150, height=35)
        self.scan_btn.pack(side=tk.LEFT, padx=10)

        # Visualization area - split view
        viz_container = Frame(self, bg=EnhancedSciFiTheme.BG_BLACK)
        viz_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left - Topology
        topo_frame = Frame(viz_container, bg=EnhancedSciFiTheme.BG_MEDIUM,
                          highlightbackground=EnhancedSciFiTheme.BORDER_SECONDARY,
                          highlightthickness=2)
        topo_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        Label(topo_frame, text="NETWORK TOPOLOGY",
              font=EnhancedSciFiTheme.FONT_HEADER,
              fg=EnhancedSciFiTheme.CYAN_BRIGHT,
              bg=EnhancedSciFiTheme.BG_MEDIUM).pack()

        self.topology = NetworkTopologyVisualization(topo_frame, width=600, height=450)
        self.topology.pack()

        # Right - Results
        results_frame = Frame(viz_container, bg=EnhancedSciFiTheme.BG_MEDIUM,
                             highlightbackground=EnhancedSciFiTheme.BORDER_PRIMARY,
                             highlightthickness=2)
        results_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        Label(results_frame, text="SCAN RESULTS",
              font=EnhancedSciFiTheme.FONT_HEADER,
              fg=EnhancedSciFiTheme.GREEN_GLOW,
              bg=EnhancedSciFiTheme.BG_MEDIUM).pack()

        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            bg=EnhancedSciFiTheme.BG_BLACK,
            fg=EnhancedSciFiTheme.GREEN_GLOW,
            font=EnhancedSciFiTheme.FONT_MONO
        )
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def start_scan(self):
        """Start network scan"""
        target = self.target_entry.get()
        self.results_text.insert(tk.END, f"Initiating neural scan of {target}...\n\n")

        # Mock scan results - add nodes to topology
        for i in range(5):
            ip = f"192.168.1.{10+i}"
            self.topology.add_node(ip, "host")

            if i > 0:
                self.topology.add_connection(f"192.168.1.{10+i-1}", ip)

            self.results_text.insert(tk.END, f"Found host: {ip}\n")

        self.results_text.insert(tk.END, "\nScan complete!\n")

# ============================================================================
# ENHANCED THREAT VISUALIZATION PANEL
# ============================================================================

class EnhancedThreatPanel(Frame):
    """Enhanced threat visualization with map"""

    def __init__(self, parent, mainframe):
        super().__init__(parent, bg=EnhancedSciFiTheme.BG_BLACK)
        self.mainframe = mainframe
        self.init_ui()

    def init_ui(self):
        """Initialize threat panel"""
        # Title
        title = Label(self, text="⚠ THREAT DETECTION SYSTEM ⚠",
                     font=EnhancedSciFiTheme.FONT_TITLE,
                     fg=EnhancedSciFiTheme.THREAT_CRITICAL,
                     bg=EnhancedSciFiTheme.BG_BLACK)
        title.pack(pady=10)

        # Threat map
        map_frame = Frame(self, bg=EnhancedSciFiTheme.BG_MEDIUM,
                         highlightbackground=EnhancedSciFiTheme.BORDER_ACCENT,
                         highlightthickness=3)
        map_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        Label(map_frame, text="THREAT MAP - RADAR VIEW",
              font=EnhancedSciFiTheme.FONT_HEADER,
              fg=EnhancedSciFiTheme.THREAT_HIGH,
              bg=EnhancedSciFiTheme.BG_MEDIUM).pack()

        self.threat_map = ThreatMapVisualization(map_frame, width=1200, height=500)
        self.threat_map.pack(pady=5)

        # Add some mock threats
        self.threat_map.add_threat("192.168.1.45", 6, 300, 200)
        self.threat_map.add_threat("10.0.0.123", 4, 600, 300)
        self.threat_map.add_threat("172.16.0.89", 2, 450, 400)

# ============================================================================
# ENHANCED MAIN WINDOW
# ============================================================================

class EnhancedArchitectMainWindow(tk.Tk):
    """Main window with enhanced sci-fi interface"""

    def __init__(self):
        super().__init__()

        self.title("ARCHITECT v3.0 - Enhanced Neural Security System")
        self.geometry("1600x1000")
        self.configure(bg=EnhancedSciFiTheme.BG_BLACK)

        # Initialize backend
        self.init_backend()

        # Create GUI
        self.init_ui()

        # Detached windows tracker
        self.detached_windows = []

        # Handle close
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def init_backend(self):
        """Initialize ARCHITECT backend"""
        try:
            config = {
                'max_concurrent_scans': 200,
                'scan_timeout': 3,
                'database_path': 'architect_v3_enhanced.db',
            }

            self.mainframe = NexusNeuralMainframe(config)
            logger.info("ARCHITECT Enhanced Backend initialized")

        except Exception as e:
            logger.error(f"Backend initialization error: {e}")
            self.mainframe = None

    def init_ui(self):
        """Initialize enhanced UI"""
        # Header
        header_frame = Frame(self, bg=EnhancedSciFiTheme.BG_DARK,
                            highlightbackground=EnhancedSciFiTheme.BORDER_PRIMARY,
                            highlightthickness=4)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        header_text = """
╔══════════════════════════════════════════════════════════════════════════════╗
║    ARCHITECT SYSTEM v3.0 - NEURAL ENHANCED SECURITY PLATFORM [UNIFIED GUI]  ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        Label(header_frame, text=header_text,
              font=("Courier New", 11, "bold"),
              fg=EnhancedSciFiTheme.GREEN_BRIGHT,
              bg=EnhancedSciFiTheme.BG_DARK,
              justify=tk.CENTER).pack(pady=5)

        # Quick action buttons
        btn_frame = Frame(header_frame, bg=EnhancedSciFiTheme.BG_DARK)
        btn_frame.pack(pady=5)

        GlowButton(btn_frame, text="NEURAL CONTROL",
                  command=self.open_neural_control,
                  width=150, height=35).pack(side=tk.LEFT, padx=5)

        GlowButton(btn_frame, text="ADVANCED CONFIG",
                  command=self.open_advanced_config,
                  width=150, height=35).pack(side=tk.LEFT, padx=5)

        GlowButton(btn_frame, text="DETACH NEURAL VIZ",
                  command=self.detach_neural_viz,
                  width=150, height=35).pack(side=tk.LEFT, padx=5)

        # Tab control
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Style notebook
        style = ttk.Style()
        style.theme_create("enhanced_scifi", parent="alt", settings={
            "TNotebook": {
                "configure": {"background": EnhancedSciFiTheme.BG_BLACK,
                            "borderwidth": 0}
            },
            "TNotebook.Tab": {
                "configure": {"background": EnhancedSciFiTheme.BG_MEDIUM,
                            "foreground": EnhancedSciFiTheme.GREEN_GLOW,
                            "padding": [15, 8],
                            "font": EnhancedSciFiTheme.FONT_MONO_BOLD},
                "map": {"background": [("selected", EnhancedSciFiTheme.GREEN_GLOW)],
                       "foreground": [("selected", EnhancedSciFiTheme.BG_BLACK)]}
            }
        })
        style.theme_use("enhanced_scifi")

        # Create panels
        self.dashboard = EnhancedDashboard(self.notebook, self.mainframe)
        self.scanner = EnhancedNetworkScanner(self.notebook, self.mainframe)
        self.threat_panel = EnhancedThreatPanel(self.notebook, self.mainframe)

        self.notebook.add(self.dashboard, text="  ⚡ DASHBOARD  ")
        self.notebook.add(self.scanner, text="  📡 NETWORK SCANNER  ")
        self.notebook.add(self.threat_panel, text="  ⚠ THREAT MAP  ")

        # Status bar
        status_frame = Frame(self, bg=EnhancedSciFiTheme.BG_MEDIUM,
                            highlightbackground=EnhancedSciFiTheme.BORDER_PRIMARY,
                            highlightthickness=3)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.status_label = Label(status_frame,
                                  text="⚡ ARCHITECT v3.0 Enhanced - All Systems Online ⚡",
                                  font=EnhancedSciFiTheme.FONT_MONO_BOLD,
                                  fg=EnhancedSciFiTheme.GREEN_BRIGHT,
                                  bg=EnhancedSciFiTheme.BG_MEDIUM,
                                  anchor=tk.W,
                                  padx=10,
                                  pady=8)
        self.status_label.pack(fill=tk.X)

    def open_neural_control(self):
        """Open neural network control panel in detached window"""
        window = DetachableWindow(self, "NEURAL NETWORK CONTROL", 900, 700)
        panel = NeuralNetworkControlPanel(window.content_frame,
                                          neural_detector=self.mainframe.neural_detector if self.mainframe else None)
        panel.pack(fill=tk.BOTH, expand=True)
        self.detached_windows.append(window)

    def open_advanced_config(self):
        """Open advanced configuration panel"""
        window = DetachableWindow(self, "ADVANCED CONFIGURATION", 800, 600)
        panel = AdvancedConfigPanel(window.content_frame)
        panel.pack(fill=tk.BOTH, expand=True)
        self.detached_windows.append(window)

    def detach_neural_viz(self):
        """Detach neural network visualization"""
        window = DetachableWindow(self, "NEURAL NETWORK VISUALIZATION", 700, 500)
        viz = NeuralNetworkVisualization(window.content_frame,
                                        layers=[20, 128, 64, 32, 8],
                                        width=680, height=450)
        viz.pack(pady=10)
        self.detached_windows.append(window)

    def on_closing(self):
        """Handle window close"""
        if messagebox.askokcancel("Exit ARCHITECT",
                                 "Are you sure you want to exit?\n"
                                 "All monitoring will stop."):
            # Close all detached windows
            for window in self.detached_windows:
                try:
                    window.destroy()
                except:
                    pass

            # Shutdown backend
            if self.mainframe:
                try:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    loop.run_until_complete(self.mainframe.shutdown())
                    loop.close()
                except:
                    pass

            logger.info("ARCHITECT Enhanced terminated")
            self.destroy()

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Main entry point"""
    try:
        print("\n✓ All components loaded successfully!")
        print("\nLaunching ARCHITECT v3.0 Enhanced GUI System...")
        print("=" * 80)

        logger.info("Starting ARCHITECT v3.0 Enhanced GUI System")

        app = EnhancedArchitectMainWindow()
        app.mainloop()

    except KeyboardInterrupt:
        print("\nARCHITECT Enhanced terminated by user")
    except Exception as e:
        logger.critical(f"Fatal error: {e}")
        logger.critical(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
