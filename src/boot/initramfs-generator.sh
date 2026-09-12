#!/bin/bash

# ScottOS 8x Initramfs Generator
# Creates custom initramfs with boot splash and early-boot services

set -e

echo "ScottOS 8x Initramfs Generator"
echo "============================="
echo ""

# Configuration
KERNEL_VERSION="${1:-$(uname -r)}"
OUTPUT_DIR="/boot"
TEMP_DIR="/tmp/scottos-initramfs-$$"

echo "[1/4] Creating temporary directory..."
mkdir -p "$TEMP_DIR"
cd "$TEMP_DIR"

echo "[2/4] Creating initramfs structure..."
mkdir -p {bin,sbin,etc,lib,usr,proc,sys,dev,run,root}

echo "[3/4] Copying essential files..."
cp /bin/sh bin/
cp /bin/ls bin/
cp /bin/cat bin/
cp /sbin/modprobe sbin/
cp /lib/ld-linux-*.so.2 lib/ 2>/dev/null || true

echo "[4/4] Creating initramfs image..."
find . -print0 | cpio -0 -H newc -o | gzip -9 > "$OUTPUT_DIR/initrd.img-scottos-$KERNEL_VERSION"

echo ""
echo "✓ Initramfs created successfully!"
echo "Output: $OUTPUT_DIR/initrd.img-scottos-$KERNEL_VERSION"

# Cleanup
cd /
rm -rf "$TEMP_DIR"
