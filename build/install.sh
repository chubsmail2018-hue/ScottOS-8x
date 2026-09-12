#!/bin/bash

# ScottOS 8x Installation Script

set -e

echo "========================================"
echo "ScottOS 8x Installation"
echo "========================================"
echo ""

# Check for root privileges
if [ \"$EUID\" -ne 0 ]; then
   echo \"This installer requires root privileges.\"
   echo \"Please run: sudo ./install.sh\"
   exit 1
fi

echo \"Installing ScottOS 8x...\"

# Create directories
mkdir -p /opt/scottos
mkdir -p /usr/share/scottos
mkdir -p /usr/share/applications
mkdir -p /etc/scottos

# Copy files
echo \"Copying files...\"
cp -r ../src /opt/scottos/
cp -r ../assets /usr/share/scottos/
cp -r ../config/* /etc/scottos/

# Create symlinks
echo \"Creating symlinks...\"
ln -sf /opt/scottos/src/taskbar/taskbar.py /usr/bin/scottos-taskbar
ln -sf /opt/scottos/src/core/kernel.py /usr/bin/scottos-kernel
ln -sf /opt/scottos/src/desktop-environment/session-manager.py /usr/bin/scottos-session

echo \"Installation complete!\"
echo \"Start ScottOS 8x with: scottos-session\"
