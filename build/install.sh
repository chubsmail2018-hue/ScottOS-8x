#!/bin/bash

# ScottOS 8x Installation Script
# Installs ScottOS 8x components to the system

set -e

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     ScottOS 8x Installation - Windows 11 Inspired Linux         ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check for root
if [ \"$EUID\" -ne 0 ]; then
   echo "❌ This installer requires root privileges."
   echo "Run with: sudo ./install.sh"
   exit 1
fi

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${YELLOW}[1/6] Creating directories...${NC}"
mkdir -p /opt/scottos
mkdir -p /usr/share/scottos/backgrounds
mkdir -p /usr/share/scottos/sounds
mkdir -p /usr/share/scottos/icons
mkdir -p /usr/share/applications
mkdir -p /etc/scottos
mkdir -p /var/log/scottos
echo -e "${GREEN}✓ Directories created${NC}"
echo ""

echo -e "${YELLOW}[2/6] Installing files...${NC}"
cp -r $(dirname \"$0\")/../src /opt/scottos/
cp -r $(dirname \"$0\")/../assets/* /usr/share/scottos/ 2>/dev/null || true
cp -r $(dirname \"$0\")/../config/* /etc/scottos/ 2>/dev/null || true
echo -e "${GREEN}✓ Files installed${NC}"
echo ""

echo -e "${YELLOW}[3/6] Creating symlinks...${NC}"
ln -sf /opt/scottos/src/boot/splash-screen.py /usr/bin/scottos-splash
ln -sf /opt/scottos/src/boot/boot-manager.py /usr/bin/scottos-boot
ln -sf /opt/scottos/src/core/kernel.py /usr/bin/scottos-kernel
ln -sf /opt/scottos/src/desktop-environment/session-manager.py /usr/bin/scottos-session
ln -sf /opt/scottos/src/taskbar/taskbar.py /usr/bin/scottos-taskbar
ln -sf /opt/scottos/src/system-apps/file-explorer.py /usr/bin/scottos-files
ln -sf /opt/scottos/src/system-apps/settings.py /usr/bin/scottos-settings
echo -e "${GREEN}✓ Symlinks created${NC}"
echo ""

echo -e "${YELLOW}[4/6] Setting permissions...${NC}"
chmod -R 755 /opt/scottos
chmod -R 755 /usr/share/scottos
chmod 755 /usr/bin/scottos-*
echo -e "${GREEN}✓ Permissions set${NC}"
echo ""

echo -e "${YELLOW}[5/6] Installing Python dependencies...${NC}"
cd $(dirname \"$0\")/..
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
echo -e "${GREEN}✓ Python dependencies installed${NC}"
echo ""

echo -e "${YELLOW}[6/6] Creating desktop shortcuts...${NC}"

# Create desktop files
cat > /usr/share/applications/scottos-session.desktop << 'DESK'
[Desktop Entry]
Version=1.0
Type=Application
Name=ScottOS 8x
Comment=Windows 11 Inspired Linux Desktop Environment
Exec=scottos-session
Icon=scottos
Categories=System;
Terminal=false
DESK

cat > /usr/share/applications/scottos-files.desktop << 'DESK'
[Desktop Entry]
Version=1.0
Type=Application
Name=File Explorer
Comment=ScottOS File Manager
Exec=scottos-files
Icon=folder
Categories=System;Utility;
Terminal=false
DESK

cat > /usr/share/applications/scottos-settings.desktop << 'DESK'
[Desktop Entry]
Version=1.0
Type=Application
Name=Settings
Comment=ScottOS System Settings
Exec=scottos-settings
Icon=preferences-system
Categories=System;Settings;
Terminal=false
DESK

echo -e "${GREEN}✓ Desktop shortcuts created${NC}"
echo ""

echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ ScottOS 8x Installation Complete!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Quick Start Commands:"
echo ""
echo "  Start desktop environment:"
echo -e "    ${YELLOW}scottos-session${NC}"
echo ""
echo "  Start boot splash:"
echo -e "    ${YELLOW}scottos-splash${NC}"
echo ""
echo "  Start taskbar:"
echo -e "    ${YELLOW}scottos-taskbar${NC}"
echo ""
echo "  File Explorer:"
echo -e "    ${YELLOW}scottos-files${NC}"
echo ""
echo "  Settings:"
echo -e "    ${YELLOW}scottos-settings${NC}"
echo ""
echo "For more info, see: docs/HOW_TO_RUN.md"
echo ""
