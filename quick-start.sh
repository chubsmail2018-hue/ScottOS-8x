#!/bin/bash

# ScottOS 8x Quick Start Script
# Run this to start ScottOS 8x in development mode

set -e

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          ScottOS 8x - Windows 11 Inspired Linux OS             ║"
echo "║                  Quick Start Script                             ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check Python
echo -e "${YELLOW}[1/5] Checking Python installation...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 is not installed${NC}"
    echo "Install with: sudo apt-get install python3 python3-pip"
    exit 1
fi
PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo -e "${GREEN}✓ Python ${PYTHON_VERSION} found${NC}"
echo ""

# Check dependencies
echo -e "${YELLOW}[2/5] Checking dependencies...${NC}"
MISSING_DEPS=0

for package in pygame PyQt5 PIL requests; do
    if python3 -c "import ${package,,}" 2>/dev/null; then
        echo -e "${GREEN}✓ ${package} installed${NC}"
    else
        echo -e "${YELLOW}⚠ ${package} not installed${NC}"
        MISSING_DEPS=$((MISSING_DEPS + 1))
    fi
done

if [ $MISSING_DEPS -gt 0 ]; then
    echo ""
    echo -e "${YELLOW}Installing missing dependencies...${NC}"
    pip install -q -r requirements.txt
    echo -e "${GREEN}✓ Dependencies installed${NC}"
fi
echo ""

# Display menu
echo -e "${BLUE}[3/5] Select what to run:${NC}"
echo ""
echo "  1) Boot Splash Screen"
echo "  2) Boot Animation"
echo "  3) Desktop Session Manager"
echo "  4) Taskbar Demo"
echo "  5) Theme Manager"
echo "  6) File Explorer"
echo "  7) Settings Application"
echo "  8) AI Assistant"
echo "  9) Sound Manager"
echo "  10) Chrome Integration"
echo "  11) Full Desktop Environment (All components)"
echo "  12) Exit"
echo ""

read -p "Enter your choice (1-12): " choice
echo ""

case $choice in
    1)
        echo -e "${GREEN}Starting Boot Splash Screen...${NC}"
        python3 src/boot/splash-screen.py
        ;;
    2)
        echo -e "${GREEN}Starting Boot Animation...${NC}"
        python3 src/boot/boot-animation.py
        ;;
    3)
        echo -e "${GREEN}Starting Desktop Session Manager...${NC}"
        python3 src/desktop-environment/session-manager.py
        ;;
    4)
        echo -e "${GREEN}Starting Taskbar Demo...${NC}"
        python3 src/taskbar/taskbar.py
        ;;
    5)
        echo -e "${GREEN}Starting Theme Manager...${NC}"
        python3 src/themes/theme-manager.py
        ;;
    6)
        echo -e "${GREEN}Starting File Explorer...${NC}"
        python3 src/system-apps/file-explorer.py
        ;;
    7)
        echo -e "${GREEN}Starting Settings Application...${NC}"
        python3 src/system-apps/settings.py
        ;;
    8)
        echo -e "${GREEN}Starting AI Assistant...${NC}"
        python3 src/ai/ai-assistant.py
        ;;
    9)
        echo -e "${GREEN}Starting Sound Manager...${NC}"
        python3 src/sounds/sound-manager.py
        ;;
    10)
        echo -e "${GREEN}Starting Chrome Integration...${NC}"
        python3 src/chrome-integration/chrome-integration.py
        ;;
    11)
        echo -e "${GREEN}Starting Full Desktop Environment...${NC}"
        echo ""
        echo -e "${BLUE}Launching all ScottOS 8x components...${NC}"
        echo ""
        
        # Start services in background
        python3 src/boot/boot-manager.py > /tmp/scottos-boot-manager.log 2>&1 &
        sleep 1
        python3 src/boot/splash-screen.py > /tmp/scottos-splash.log 2>&1 &
        sleep 2
        python3 src/sounds/sound-manager.py > /tmp/scottos-sound-manager.log 2>&1 &
        python3 src/themes/theme-manager.py > /tmp/scottos-theme-manager.log 2>&1 &
        python3 src/desktop-environment/session-manager.py > /tmp/scottos-session.log 2>&1 &
        python3 src/taskbar/taskbar.py > /tmp/scottos-taskbar.log 2>&1 &
        python3 src/ai/ai-assistant.py > /tmp/scottos-ai.log 2>&1 &
        
        echo -e "${GREEN}✓ All components started!${NC}"
        echo ""
        echo "Log files:"
        echo "  - Boot Manager: /tmp/scottos-boot-manager.log"
        echo "  - Splash Screen: /tmp/scottos-splash.log"
        echo "  - Sound Manager: /tmp/scottos-sound-manager.log"
        echo "  - Theme Manager: /tmp/scottos-theme-manager.log"
        echo "  - Session Manager: /tmp/scottos-session.log"
        echo "  - Taskbar: /tmp/scottos-taskbar.log"
        echo "  - AI Assistant: /tmp/scottos-ai.log"
        echo ""
        echo -e "${YELLOW}Press Ctrl+C to stop all services${NC}"
        echo ""
        
        # Wait for user interrupt
        wait
        ;;
    12)
        echo -e "${YELLOW}Exiting...${NC}"
        exit 0
        ;;
    *)
        echo -e "${RED}Invalid choice. Please try again.${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}✓ ScottOS 8x session completed${NC}"
echo ""
