# How to Run ScottOS 8x

## Quick Start Options

There are multiple ways to run ScottOS 8x:

1. **[Option 1: Virtual Machine (Easiest)](#option-1-virtual-machine)** ⭐ Recommended for testing
2. **[Option 2: Docker Container](#option-2-docker-container)** - Quick containerized environment
3. **[Option 3: Development Mode](#option-3-development-mode)** - Run components directly
4. **[Option 4: Live USB/Bootable Media](#option-4-live-usbbootable-media)** - Full OS installation
5. **[Option 5: Bare Metal Installation](#option-5-bare-metal-installation)** - Direct hardware install

---

## Option 1: Virtual Machine

### Prerequisites
- VirtualBox or VMware installed
- At least 4GB RAM available
- 20GB disk space
- Ubuntu 22.04 or Fedora 38+ ISO

### Method A: Using VirtualBox (Recommended)

#### Step 1: Download and Install VirtualBox
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y virtualbox virtualbox-ext-pack

# Fedora
sudo dnf install -y VirtualBox

# macOS
brew install virtualbox
```

#### Step 2: Create Virtual Machine

1. Open VirtualBox
2. Click **New**
3. Configure:
   - **Name**: ScottOS 8x
   - **Type**: Linux
   - **Version**: Ubuntu (64-bit) or Fedora (64-bit)
   - **RAM**: 4GB (4096 MB) minimum, 8GB recommended
   - **Storage**: 30GB dynamic allocation

#### Step 3: Install Base OS

```bash
# Download Ubuntu 22.04 LTS
wget https://releases.ubuntu.com/22.04/ubuntu-22.04.3-desktop-amd64.iso

# Or Fedora 38
wget https://download.fedoraproject.org/pub/fedora/linux/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso
```

1. Right-click VM → **Settings** → **Storage**
2. Add ISO to CD/DVD drive
3. Boot and install OS
4. Complete standard installation

#### Step 4: Install ScottOS 8x

Once base OS is installed and running:

```bash
# Clone the repository
git clone https://github.com/chubsmail2018-hue/ScottOS-8x.git
cd ScottOS-8x

# Run installation script
sudo bash build/install.sh

# Start ScottOS 8x desktop
scottos-session
```

#### Step 5: Reboot

```bash
sudo reboot
```

✅ ScottOS 8x should now boot with Windows 11-style splash screen!

---

## Option 2: Docker Container

### Prerequisites
- Docker installed
- Docker Compose (optional)

### Quick Start

#### Step 1: Create Dockerfile

```bash
cd ScottOS-8x
cat > Dockerfile << 'EOF'
FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    git build-essential \
    qt5-default libx11-dev \
    --no-install-recommends

# Copy ScottOS
COPY . /opt/scottos
WORKDIR /opt/scottos

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create startup script
RUN echo '#!/bin/bash' > /start.sh && \
    echo 'python3 /opt/scottos/src/boot/splash-screen.py' >> /start.sh && \
    chmod +x /start.sh

ENTRYPOINT ["/bin/bash"]
EOF
```

#### Step 2: Build Docker Image

```bash
docker build -t scottos-8x:latest .
```

#### Step 3: Run Container

```bash
# Interactive mode
docker run -it scottos-8x:latest

# With X11 display forwarding (Linux)
docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix scottos-8x:latest
```

#### Step 4: Inside Container

```bash
# Install more components
pip install PyQt5

# Run boot splash
python3 /opt/scottos/src/boot/splash-screen.py

# Start desktop environment
python3 /opt/scottos/src/desktop-environment/session-manager.py
```

---

## Option 3: Development Mode

Run ScottOS 8x components directly on your current Linux system.

### Prerequisites
```bash
# Ubuntu/Debian
sudo apt-get install -y python3 python3-pip git
pip install -r requirements.txt

# Fedora
sudo dnf install -y python3 python3-pip git
pip install -r requirements.txt
```

### Step 1: Clone Repository

```bash
git clone https://github.com/chubsmail2018-hue/ScottOS-8x.git
cd ScottOS-8x
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development
```

### Step 3: Run Components

#### Run Boot Splash Screen
```bash
python3 src/boot/splash-screen.py
```

#### Run Boot Manager
```bash
python3 src/boot/boot-manager.py
```

#### Run Boot Animation
```bash
python3 src/boot/boot-animation.py
```

#### Run Desktop Session Manager
```bash
python3 src/desktop-environment/session-manager.py
```

#### Run Taskbar
```bash
python3 src/taskbar/taskbar.py
```

#### Run Sound Manager
```bash
python3 src/sounds/sound-manager.py
```

#### Run Theme Manager
```bash
python3 src/themes/theme-manager.py
```

#### Run File Explorer
```bash
python3 src/system-apps/file-explorer.py
```

#### Run Settings App
```bash
python3 src/system-apps/settings.py
```

#### Run AI Assistant
```bash
python3 src/ai/ai-assistant.py
```

#### Run Chrome Integration
```bash
python3 src/chrome-integration/chrome-integration.py
```

### Step 4: Run All Components Together

```bash
#!/bin/bash
# save as run-scottos.sh

echo "Starting ScottOS 8x Components..."

# Start services in background
python3 src/boot/boot-manager.py &
python3 src/sounds/sound-manager.py &
python3 src/themes/theme-manager.py &
python3 src/desktop-environment/session-manager.py &
python3 src/taskbar/taskbar.py &

echo "All components started!"
echo "Press Ctrl+C to stop"

wait
```

```bash
chmod +x run-scottos.sh
./run-scottos.sh
```

---

## Option 4: Live USB/Bootable Media

### Prerequisites
- USB drive (8GB+)
- Linux system with `dd` or GNOME Disks
- ScottOS 8x ISO image

### Step 1: Create ISO Image

```bash
# First, build the ISO (from project root)
cd build
./build-iso.sh
# Creates: scottos-8x-v1.0.iso
```

### Step 2: Write to USB

#### Method A: Using dd (Linux/macOS)
```bash
# Find USB device
lsblk
# or
dfisk -l

# Unmount (if mounted)
sudo umount /dev/sdX*

# Write ISO
sudo dd if=scottos-8x-v1.0.iso of=/dev/sdX bs=4M status=progress
sync
```

#### Method B: Using GNOME Disks (GUI)
1. Open **Disks**
2. Insert USB drive
3. Right-click device → **Restore Disk Image**
4. Select `scottos-8x-v1.0.iso`
5. Click **Start Restoring**

#### Method C: Using Etcher (All Platforms)
```bash
# Download Balena Etcher
https://www.balena.io/etcher/

# Or install via package manager
sudo apt-get install balena-etcher-electron  # Ubuntu/Debian
sudo dnf install balena-etcher                # Fedora

# Run GUI and select ISO + USB drive
balena-etcher-electron
```

### Step 3: Boot from USB

1. Restart computer
2. Press boot key during startup:
   - **F2, F10, F12** - Dell, Lenovo, HP
   - **Esc** - ASUS
   - **Delete** - Most others
3. Select USB drive from boot menu
4. Follow installation wizard

---

## Option 5: Bare Metal Installation

### Prerequisites
- Spare computer or partition
- USB drive with ScottOS 8x ISO
- Backup important data

### Step 1: Boot from USB

- Create bootable USB (see Option 4)
- Boot from USB
- Select "Install ScottOS 8x"

### Step 2: Installation Wizard

```
1. Select Language: English
2. Select Keyboard Layout
3. Network Configuration
4. Partition Disk
   - Auto-partition (recommended)
   - Or manual for advanced users
5. Create User Account
6. Set Hostname: "ScottOS-8x"
7. Set Root Password
8. Select Components
9. Install (15-30 minutes)
```

### Step 3: Post-Installation

```bash
# Login with user credentials
# Update system
sudo apt-get update && sudo apt-get upgrade -y

# Install additional drivers
sudo apt-get install -y linux-firmware linux-headers-generic

# Install ScottOS enhancements
sudo apt-get install -y python3-pyqt5 google-chrome-stable

# Apply ScottOS customizations
cd ScottOS-8x
sudo bash build/install.sh

# Reboot
sudo reboot
```

---

## Troubleshooting

### Issue: Boot splash doesn't show

```bash
# Check logs
sudo journalctl -b

# Run with verbose output
python3 src/boot/splash-screen.py --verbose
```

### Issue: Desktop environment won't start

```bash
# Check session manager
python3 src/desktop-environment/session-manager.py

# Check dependencies
pip list | grep PyQt5
```

### Issue: Very slow boot

```bash
# Analyze boot time
sudo systemd-analyze

# Check disk space
df -h

# Disable unnecessary services
sudo systemctl list-unit-files | grep enabled
sudo systemctl disable SERVICE_NAME
```

### Issue: Sound not working

```bash
# Test sound
python3 src/sounds/sound-manager.py

# Check audio device
alsamixer

# Check PulseAudio
pacmd list-sinks
```

---

## Performance Tips

### Improve Boot Speed

```bash
# Enable parallel boot
sudo sed -i 's/ParallelBoot = false/ParallelBoot = true/' /etc/scottos/boot.conf

# Disable unnecessary services
sudo systemctl disable cups.service
sudo systemctl disable bluetooth.service

# Use SSD TRIM
sudo systemctl enable fstrim.timer
```

### Improve Runtime Performance

```bash
# Increase file descriptors
ulimit -n 65536

# Enable swap
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Optimize I/O scheduler
echo "mq-deadline" | sudo tee /sys/block/sda/queue/scheduler
```

---

## System Requirements

| Component | Minimum | Recommended | Ideal |
|-----------|---------|-------------|-------|
| **CPU** | 2 cores | 4 cores | 8+ cores |
| **RAM** | 2GB | 4GB | 8GB+ |
| **Storage** | 15GB | 30GB | 60GB+ |
| **Display** | 1024x768 | 1920x1080 | 4K |
| **GPU** | Integrated | Discrete | High-end |

---

## Getting Help

- 📖 **Documentation**: [docs/](docs/)
- 🐛 **Issues**: https://github.com/chubsmail2018-hue/ScottOS-8x/issues
- 💬 **Discussions**: https://github.com/chubsmail2018-hue/ScottOS-8x/discussions
- 📧 **Email**: chubsmail2018@gmail.com

---

**Happy Computing! 🚀**
