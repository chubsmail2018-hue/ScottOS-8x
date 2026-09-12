#!/bin/bash

# ScottOS 8x Uninstall Script
# Removes ScottOS 8x from the system

set -e

echo ""
echo "ScottOS 8x Uninstaller"
echo "======================"
echo ""

# Check for root
if [ \"$EUID\" -ne 0 ]; then
   echo "❌ This uninstaller requires root privileges."
   echo "Run with: sudo ./uninstall.sh"
   exit 1
fi

read -p "Are you sure you want to uninstall ScottOS 8x? (y/N): " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Removing ScottOS 8x..."
    
    # Remove directories
    rm -rf /opt/scottos
    rm -rf /usr/share/scottos
    rm -rf /etc/scottos
    
    # Remove symlinks
    rm -f /usr/bin/scottos-*
    
    # Remove desktop files
    rm -f /usr/share/applications/scottos-*.desktop
    
    # Remove logs
    rm -rf /var/log/scottos
    
    echo "✓ ScottOS 8x uninstalled"
else
    echo "Uninstall cancelled"
    exit 1
fi

echo ""
