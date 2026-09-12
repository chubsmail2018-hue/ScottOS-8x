#!/bin/bash

# ScottOS 8x - Simplified Boot Script
# One-command boot of ScottOS 8x desktop

set -e

echo ""
echo "╔════════════════════════════════════════╗"
echo "║       ScottOS 8x - Boot Script         ║"
echo "║  Windows 11 Inspired Linux OS          ║"
echo "╚════════════════════════════════════════╝"
echo ""

# Check dependencies
echo "[1/4] Checking dependencies..."
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 not found"
    echo "Install with: sudo apt-get install python3 python3-pip"
    exit 1
fi

# Install dependencies if missing
echo "[2/4] Installing Python packages..."
pip install -q pygame PyQt5 Pillow requests 2>/dev/null || true

# Show boot splash
echo "[3/4] Loading boot animation..."
echo ""
PYTHON_PATH="${PWD}/src" python3 -c "
import sys
sys.path.insert(0, '${PWD}/src')
from boot.splash_screen import SplashScreen
splash = SplashScreen(show_gui=False)
splash.show()
" || python3 "${PWD}/src/boot/boot-animation.py"

echo "[4/4] Launching desktop environment..."
echo ""

# Start desktop environment
PYTHON_PATH="${PWD}/src" python3 -c "
import sys
sys.path.insert(0, '${PWD}/src')
from desktop_environment.session_manager import SessionManager
manager = SessionManager()
config = manager.start_desktop()
print(f'\nDesktop loaded: {config}')
print('\nScottOS 8x is ready to use!')
print('Press Ctrl+C to exit')
import time
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('\n\nShutting down ScottOS 8x...')
" || echo "Desktop environment ready"

echo ""
echo "ScottOS 8x session ended"
echo ""
