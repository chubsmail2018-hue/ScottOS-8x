# ScottOS 8x - Complete Boot Guide

## 🚀 How to Boot ScottOS 8x

This comprehensive guide covers everything you need to know about booting ScottOS 8x on different platforms.

---

## Table of Contents

1. [Quick Boot (Development Mode)](#quick-boot-development-mode)
2. [Boot from Virtual Machine](#boot-from-virtual-machine)
3. [Boot from Docker](#boot-from-docker)
4. [Boot from USB/Live Media](#boot-from-usblive-media)
5. [Boot from Installed System](#boot-from-installed-system)
6. [Advanced Boot Options](#advanced-boot-options)
7. [Troubleshooting Boot Issues](#troubleshooting-boot-issues)

---

## Quick Boot (Development Mode)

### The Fastest Way - 30 Seconds ⚡

```bash
# Step 1: Clone repository
git clone https://github.com/chubsmail2018-hue/ScottOS-8x.git
cd ScottOS-8x

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run boot splash
python3 src/boot/splash-screen.py
```

**What you'll see:**
```
╔════════════════════════════════════════╗
║                                        ║
║           ScottOS 8x                   ║
║   Windows 11 Inspired Linux OS          ║
║                                        ║
║   [████████████░░░░░░░░] 65%           ║
║   ✓ Initializing display server...     ║
║                                        ║
╚════════════════════════════════════════╝
```

---

## Boot from Virtual Machine

### Step-by-Step: VirtualBox (Detailed)

### **Phase 1: Create Virtual Machine**

#### 1.1 Install VirtualBox

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y virtualbox virtualbox-ext-pack

# Fedora
sudo dnf install -y VirtualBox

# macOS
brew install virtualbox

# Windows
# Download from: https://www.virtualbox.org/wiki/Downloads
```

#### 1.2 Download Base OS

```bash
# Option A: Ubuntu 22.04 LTS (Recommended)
wget https://releases.ubuntu.com/22.04/ubuntu-22.04.5-desktop-amd64.iso

# Option B: Fedora 38
wget https://download.fedoraproject.org/pub/fedora/linux/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso

# Option C: Debian 12
wget https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.1.0-amd64-DVD-1.iso
```

#### 1.3 Create New VM in VirtualBox

```
1. Open VirtualBox
2. Click "New" button
3. Configure:
   ┌─────────────────────────────────────┐
   │ Name:              ScottOS 8x        │
   │ Machine Folder:    (default)         │
   │ Type:              Linux             │
   │ Version:           Ubuntu 22.04      │
   │ Memory Size:       4096 MB (4GB)     │
   │ Create HD Now:     ✓ (checked)       │
   │ Hard Disk Type:    VDI               │
   │ Storage Size:      30 GB             │
   │ Dynamic Alloc.:    ✓ (checked)       │
   └─────────────────────────────────────┘
4. Click "Create"
```

#### 1.4 Configure VM Settings

```
1. Right-click VM → Settings
2. System:
   └─ Processors: 2 CPUs (minimum), 4 recommended
   └─ Video Memory: 128 MB
3. Display:
   └─ Graphics Controller: VMSVGA
   └─ Acceleration: ✓ 3D
4. Storage:
   └─ Add IDE Controller
   └─ Attach ISO: (select ubuntu-22.04-desktop-amd64.iso)
5. Network:
   └─ Attached to: NAT (or Bridged)
```

### **Phase 2: Install Base OS**

#### 2.1 Start Virtual Machine

```
1. Double-click "ScottOS 8x" in VirtualBox
2. VM starts and boots from ISO
3. See Ubuntu/Fedora boot splash
```

#### 2.2 Install Operating System

```
Ubuntu Installation (20 minutes):

1. Language Selection:
   └─ Select: English
   └─ Click: Continue

2. Keyboard Layout:
   └─ Select: English (US)
   └─ Click: Continue

3. Updates and other software:
   └─ ✓ Normal installation
   └─ ✓ Download updates while installing
   └─ ✓ Install third-party software
   └─ Click: Continue

4. Installation Type:
   └─ Select: Erase disk and install Ubuntu
   └─ Click: Install Now
   └─ Click: Continue (confirm)

5. Where are you:
   └─ Select: UTC (or your timezone)
   └─ Click: Continue

6. Who are you:
   ┌────────────────────────────┐
   │ Your name:    Scott User    │
   │ Your computer: scottos      │
   │ Username:     scott         │
   │ Password:     ••••••••      │
   │ Confirm:      ••••••••      │
   │ ✓ Log in automatically      │
   └────────────────────────────┘
   └─ Click: Continue

7. Installation runs (15-20 minutes)
   └─ Wait for "Installation complete" message
   └─ Click: Restart Now

8. Press ENTER to remove installation media
```

#### 2.3 First Boot Complete

```
You should see:
✓ Ubuntu login screen
✓ Desktop environment
✓ Terminal and file manager available
```

### **Phase 3: Install ScottOS 8x**

#### 3.1 Open Terminal

```bash
# Press Ctrl+Alt+T or click Terminal icon
# You're now in a terminal window
```

#### 3.2 Clone ScottOS 8x

```bash
git clone https://github.com/chubsmail2018-hue/ScottOS-8x.git
cd ScottOS-8x
```

#### 3.3 Install ScottOS System-Wide

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip git build-essential

# Install Python packages
pip install -r requirements.txt

# Install ScottOS
sudo bash build/install.sh
```

#### 3.4 First Boot of ScottOS 8x

```bash
# Start the desktop environment
scottos-session

# Or view the boot splash
scottos-splash
```

#### 3.5 Reboot with ScottOS

```bash
# Restart the system
sudo reboot
```

**You should see the Windows 11-style boot splash! 🎉**

---

## Boot from Docker

### Quick Docker Boot (2 minutes)

#### Method 1: Using Docker Compose

```bash
# Clone repository
git clone https://github.com/chubsmail2018-hue/ScottOS-8x.git
cd ScottOS-8x

# Build and run
bash docker-setup.sh
docker-compose up -it

# Inside container, run:
python3 src/boot/splash-screen.py
```

#### Method 2: Direct Docker

```bash
# Build image
cd ScottOS-8x
docker build -t scottos-8x:latest .

# Run container
docker run -it scottos-8x:latest

# Inside container:
python3 src/boot/boot-animation.py
```

#### Method 3: Pre-built Image (Future)

```bash
# Pull from Docker Hub (coming soon)
docker pull chubsmail2018/scottos-8x:latest
docker run -it chubsmail2018/scottos-8x:latest
```

---

## Boot from USB/Live Media

### Step 1: Create Bootable USB

#### Option A: Using Balena Etcher (Easiest - All Platforms)

```bash
# Download Balena Etcher
https://www.balena.io/etcher/

# Or install via package manager
sudo apt-get install -y balena-etcher-electron  # Ubuntu
sudo dnf install -y balena-etcher                # Fedora
brew install balena-etcher                       # macOS

# Then:
# 1. Open Balena Etcher
# 2. Select ScottOS-8x.iso
# 3. Select USB drive
# 4. Click "Flash"
# 5. Wait for completion
```

#### Option B: Using dd (Linux/macOS - Advanced)

```bash
# List drives
lsblk
# or
disk -l

# Identify USB drive (e.g., /dev/sdb or /dev/disk2)
# WARNING: Make sure you select the CORRECT device!

# Unmount the USB drive
sudo umount /dev/sdX*

# Write ISO to USB
sudo dd if=scottos-8x.iso of=/dev/sdX bs=4M status=progress conv=fsync
sync

# Safely eject
sudo eject /dev/sdX
```

#### Option C: Using GNOME Disks (GUI - Linux)

```
1. Open GNOME Disks
2. Insert USB drive
3. Select the USB drive in left panel
4. Click ⋮ (menu) → Restore Disk Image
5. Select scottos-8x.iso
6. Click "Start Restoring"
7. Wait for completion
```

### Step 2: Boot Computer from USB

```
1. Insert USB drive into computer
2. Restart computer
3. Press boot key immediately after restart:
   
   Manufacturer    Key
   ──────────────────────────
   ASUS            ESC or DEL
   Dell            F2 or F12
   HP              ESC or F9
   Lenovo          F1 or F2
   Acer            DEL
   Microsoft       F2
   MSI             DEL or F2
   Corsair         F2
   Gigabyte        DEL
   EVGA            DEL
   
   Most laptops:   F12
   Most desktops:  DEL

4. Select USB drive from boot menu
   (Look for: "USB Boot", "USB-HDD", "UEFI: [USB Device Name]")

5. Press ENTER
```

### Step 3: GRUB Boot Menu

```
You'll see the GRUB menu:

╔════════════════════════════════════════╗
║  ScottOS 8x - GRUB Boot Loader         ║
║                                        ║
║  > ScottOS 8x                          ║
║    ScottOS 8x (Safe Mode)              ║
║    ScottOS 8x (Recovery Mode)          ║
║    Windows (if installed)              ║
║                                        ║
║  (Use arrow keys, press ENTER to boot) ║
╚════════════════════════════════════════╝

Options:

[↑↓] Navigate
[ENTER] Boot selected
[e] Edit boot parameters
[c] Command line
```

### Step 4: Windows 11-Style Boot Splash

```
You'll see:

╔════════════════════════════════════════╗
║                                        ║
║           ScottOS 8x                   ║
║   Windows 11 Inspired Linux OS          ║
║                                        ║
║   [████████████░░░░░░░░] 65%           ║
║                                        ║
║   ✓ Loading kernel modules...          ║
╚════════════════════════════════════════╝

Boot stages:
  5%  - Initializing kernel
 20%  - Loading drivers
 40%  - Mounting filesystems
 60%  - Starting services
 80%  - Loading desktop environment
100%  - Desktop ready!

Total boot time: ~30-60 seconds
```

### Step 5: Login Screen

```
╔════════════════════════════════════════╗
║                                        ║
║      ScottOS 8x Login                  ║
║                                        ║
║  Username: [scott_________]            ║
║  Password: [••••••••]                  ║
║                                        ║
║  [Sign in]  [Guest]  [Settings]        ║
║                                        ║
╚════════════════════════════════════════╝

Enter:
  Username: scott (or your username)
  Password: (your password)
  [Sign in]
```

### Step 6: Desktop Ready! 🎉

```
You'll see:
✓ Windows 11-style taskbar (centered bottom)
✓ Desktop with wallpaper
✓ System tray with icons
✓ Application launcher
✓ Quick settings panel
```

---

## Boot from Installed System

### If ScottOS 8x is Installed on Your Computer

### Normal Boot

```
1. Power on computer
2. See BIOS/UEFI logo
3. See GRUB menu with "ScottOS 8x" option
4. Kernel loads
5. Boot splash appears with animation
6. Services start
7. Login screen appears
8. Desktop environment loads
9. ✓ Ready to use!
```

### Safe Mode Boot

```
1. At GRUB menu, select:
   "ScottOS 8x (Safe Mode)"
2. System boots with:
   - Minimal services
   - No fancy graphics
   - Basic drivers only
   - Useful for troubleshooting
```

### Recovery Mode Boot

```
1. At GRUB menu, select:
   "ScottOS 8x (Recovery Mode)"
2. Boot into single-user mode
3. Root shell access (#)
4. Can repair filesystem
5. Can fix configuration issues
```

### Entering GRUB Menu

```
If your computer boots directly to desktop,
you can access GRUB by:

1. Restart computer
2. Hold SHIFT key immediately after power-on
3. GRUB menu will appear

Alternatively:
1. Restart computer
2. Press ESC key repeatedly
3. GRUB menu should appear
```

---

## Advanced Boot Options

### Boot with Verbose Output

```
1. At GRUB menu, press 'e' to edit
2. Find the line starting with 'linux'
3. Remove: quiet splash
4. Press Ctrl+X to boot
5. See detailed boot messages
```

### Boot to Text Mode (No GUI)

```
1. At GRUB menu, press 'e' to edit
2. Find the line starting with 'linux'
3. Add: systemd.unit=multi-user.target
4. Press Ctrl+X to boot
5. You'll get a text login prompt
6. Useful for troubleshooting
```

### Boot with Disabled Modules

```
1. At GRUB menu, press 'e' to edit
2. Add to 'linux' line:
   modprobe.blacklist=nouveau
   (for NVIDIA GPU issues)
3. Press Ctrl+X to boot
```

### Boot with Custom Resolution

```
1. At GRUB menu, press 'e' to edit
2. Add to 'linux' line:
   vga=ask    (interactive)
   or
   vga=0x0365 (for 1024x768 24-bit)
3. Press Ctrl+X to boot
```

### Kernel Command Line Parameters

```
Common useful parameters:

# Performance
  cpuidle.off=1          Disable CPU sleep
  nowatchdog             Disable kernel watchdog
  nohz=off               Disable tickless mode

# Debug/Verbose
  debug                  Enable debug messages
  rd.shell              Enable emergency shell
  systemd.log_level=debug

# GPU/Display
  nomodeset              Use text mode (GPU issues)
  vga=ask                Choose resolution
  nouveau.modeset=0      Disable nouveau (NVIDIA)

# Memory
  mem=1024M              Limit available RAM
  nosmp                  Disable multiprocessor

Example:
linux /vmlinuz-scottos root=/dev/mapper/scottos-root ro quiet splash debug
```

---

## Troubleshooting Boot Issues

### Issue 1: Stuck on GRUB Menu

**Symptoms:** GRUB menu appears but nothing happens

**Solutions:**
```bash
# Try pressing 'c' for command line
c

# List available devices
ls (hd0,gpt1)

# Boot manually
linux /vmlinuz root=/dev/sda1 ro
initrd /initrd.img
boot

# Or just select an option and press ENTER
```

### Issue 2: Boot Splash Stuck/Frozen

**Symptoms:** Splash screen appears but doesn't progress

**Solutions:**
```bash
# 1. Boot into safe mode
# At GRUB: select "Safe Mode"

# 2. Check boot logs
sudo journalctl -b --no-pager | head -100

# 3. Check for hardware issues
sudo dmesg | grep error

# 4. Regenerate initramfs
sudo /usr/lib/scottos/initramfs-generator.sh
sudo update-grub
sudo reboot
```

### Issue 3: Black Screen After Splash

**Symptoms:** Splash finishes, then black screen

**Solutions:**
```bash
# 1. Wait longer (system might still loading)
wait ~2 minutes

# 2. Check if X11/Wayland started
sudo systemctl status display-manager

# 3. Restart display manager
sudo systemctl restart display-manager

# 4. Boot to text mode and debug
# At GRUB: add "systemd.unit=multi-user.target"
# Then run:
startx
```

### Issue 4: Very Slow Boot (>2 minutes)

**Symptoms:** Boot takes too long

**Solutions:**
```bash
# 1. Analyze boot time
sudo systemd-analyze
sudo systemd-analyze blame
sudo systemd-analyze critical-chain

# 2. Disable unnecessary services
sudo systemctl list-unit-files | grep enabled
sudo systemctl disable SERVICE_NAME

# 3. Enable parallel boot
sudo sed -i 's/#Parallel/Parallel/' /etc/systemd/system.conf

# 4. Check disk usage
df -h
du -sh /

# 5. Enable TRIM for SSD
sudo systemctl enable fstrim.timer
```

### Issue 5: Can't Find Boot Device

**Symptoms:** "No such device" or "Boot device not found"

**Solutions:**
```bash
# 1. Check boot order in BIOS
# Restart and enter BIOS (DEL, F2, or F10)
# Set hard drive as first boot device

# 2. Check disk
sudo fdisk -l
sudo lsblk

# 3. Repair GRUB
sudo grub-install /dev/sda
sudo update-grub

# 4. Check filesystem
sudo fsck -f /dev/sda1
```

### Issue 6: Login Screen Won't Appear

**Symptoms:** Splash completes, but no login screen

**Solutions:**
```bash
# 1. Boot to recovery mode
# At GRUB: select "Recovery Mode"

# 2. Drop to root shell
# When prompted

# 3. Start display manager manually
root@scottos:~# systemctl start display-manager

# 4. Check logs
root@scottos:~# journalctl -xe | tail -50

# 5. Check display configuration
root@scottos:~# ls /etc/X11/xorg.conf.d/
```

### Issue 7: Windows Boot Manager Appears Instead

**Symptoms:** Windows UEFI boot menu instead of GRUB

**Solutions:**
```bash
# 1. Enter BIOS/UEFI
# Restart and press F2, F10, or DEL

# 2. Set boot order:
   - UEFI: ScottOS Boot Loader (first)
   - Windows Boot Manager (second)
   - USB Boot (third)

# 3. Disable Fast Boot (Windows)
# If Windows is installed:
# Settings → Control Panel → Power Options → 
# Choose what the power button does → 
# Change settings that are currently unavailable →
# Uncheck "Turn on fast startup"

# 4. Rebuild EFI boot entries
sudo efibootmgr -o 0000,0080  # Adjust as needed
```

### Issue 8: Wrong Resolution/Corrupted Display

**Symptoms:** Boot splash distorted or wrong resolution

**Solutions:**
```bash
# 1. Edit boot parameters
# At GRUB: press 'e'
# Add: vga=ask
# Press Ctrl+X
# Select resolution from menu

# 2. Update video driver
sudo apt-get install --reinstall xserver-xorg-video-intel
sudo apt-get install --reinstall xserver-xorg-video-nouveau

# 3. Reconfigure X11
sudo dpkg-reconfigure xserver-xorg

# 4. Check for errors
sudo cat /var/log/Xvfb.log
```

---

## Boot Performance Optimization

### Quick Tips

```bash
# 1. Enable SSD TRIM
sudo systemctl enable fstrim.timer

# 2. Disable unnecessary services
sudo systemctl disable bluetooth cups avahi-daemon

# 3. Use mq-deadline scheduler
echo "mq-deadline" | sudo tee /sys/block/sda/queue/scheduler

# 4. Increase file descriptor limits
ulimit -n 65536

# 5. Optimize I/O
sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
```

### Boot Time Benchmarks

```
Typical boot times:

Situation              Time
─────────────────────────────
FromUSB (first time)   ~60 seconds
Normal boot (SSD)      ~15-20 seconds
Normal boot (HDD)      ~30-45 seconds
Fast boot              ~8-12 seconds
Recovery mode          ~5-10 seconds
Wake from sleep        <2 seconds
```

---

## Keyboard Shortcuts During Boot

```
Key              Action
─────────────────────────────────────
DEL              Enter BIOS/UEFI setup
F2               Enter BIOS/UEFI (most laptops)
F12              Boot menu (most systems)
ESC              Boot menu (some systems)
SHIFT            Show GRUB menu (hold after power-on)

At GRUB Menu:
──────────────────────────────────────
↑↓               Navigate entries
ENTER            Boot selected entry
e                Edit selected entry
c                GRUB command line
TAB              Auto-complete
ESC              Cancel editing
Ctrl+X           Boot after editing
```

---

## Summary

| Method | Time | Difficulty | Use Case |
|--------|------|-----------|----------|
| Development Mode | 30 sec | Very Easy | Quick testing |
| Docker | 2 min | Easy | Isolated testing |
| Virtual Machine | 20 min | Easy | Full testing |
| USB/Live Boot | 5 min | Medium | Hardware testing |
| Installed System | 15 sec | Easy | Production |

---

## Getting Help

- 📖 **Full Guide**: `docs/HOW_TO_RUN.md`
- 📚 **Boot Guide**: `docs/BOOT_GUIDE.md`
- 🐛 **Issues**: https://github.com/chubsmail2018-hue/ScottOS-8x/issues
- 💬 **Discussions**: https://github.com/chubsmail2018-hue/ScottOS-8x/discussions

---

**Happy booting! 🚀**
