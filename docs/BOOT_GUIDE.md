# ScottOS 8x Boot Guide

## Overview

ScottOS 8x features a modern, Windows 11-inspired boot experience with:
- Custom GRUB theme
- Animated splash screen
- Progress indicators
- Boot sound effects
- Optimized boot sequence

## Boot Sequence Timeline

```
0ms - Power On
    ↓
100ms - Firmware POST (Power-On Self Test)
    ↓
500ms - GRUB Bootloader
    ↓
2000ms - Kernel Initialization
    ↓
3000ms - Initramfs Boot
    ↓
5000ms - Splash Screen & Animation
    ↓
7000ms - Service Startup
    ↓
10000ms - Desktop Environment Ready
```

## Boot Files Location

```
/boot/
├── grub/
│   ├── grub.cfg              # GRUB configuration
│   ├── themes/              # GRUB themes
│   ├── backgrounds/         # Boot backgrounds
│   └── fonts/               # Boot fonts
├── vmlinuz-scottos          # Kernel image
└── initrd.img-scottos       # Initial ramdisk

/etc/scottos/
├── boot.conf                # Boot configuration
├── kernel-parameters.conf   # Kernel parameters
└── system.conf              # System configuration

/usr/share/scottos/
├── backgrounds/             # Boot splash images
└── sounds/                  # Boot sounds
```

## Boot Parameters

### Common Parameters

- `quiet` - Suppress kernel messages
- `splash` - Show splash screen
- `nomodeset` - Disable kernel mode setting (for GPU issues)
- `systemd.unit=multi-user.target` - Boot to text mode
- `single` - Boot to single-user mode

### Editing Boot Parameters

1. At GRUB menu, press `e` to edit
2. Navigate to linux line
3. Add/modify parameters
4. Press `Ctrl+X` to boot

## Boot Troubleshooting

### Stuck on Splash Screen

```bash
# Boot with verbose output
# Edit GRUB: remove 'quiet' and 'splash'
# Check logs
sudo journalctl -b
```

### Very Slow Boot

```bash
# Analyze boot time
sudo systemd-analyze
sudo systemd-analyze critical-chain

# Check disk usage
df -h
```

### No Splash Screen

```bash
# Regenerate initramfs
sudo /usr/lib/scottos/initramfs-generator.sh

# Reinstall GRUB theme
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

## Performance Optimization

### Parallel Boot

Enable parallel service startup:

```bash
# In /etc/scottos/boot.conf
ParallelBoot = true
```

### Reduce Boot Services

```bash
# Check which services start at boot
sudo systemctl list-unit-files | grep enabled

# Disable unnecessary services
sudo systemctl disable SERVICE_NAME
```

### RAM Disk Optimization

```bash
# Adjust in kernel parameters
initrd_compression=lz4
initrd_size=512M
```

## Boot Customization

### Change Splash Screen

1. Create new image (1920x1080)
2. Copy to `/usr/share/scottos/backgrounds/boot-splash.png`
3. Update `/etc/scottos/boot.conf`

### Change Boot Sound

1. Place sound file in `/usr/share/scottos/sounds/`
2. Update sound manager configuration
3. Test: `paplay /usr/share/scottos/sounds/startup.wav`

### Modify Boot Animation

Edit `src/boot/boot-animation.py` and recompile.

## Safe Mode & Recovery

### Accessing Safe Mode

1. At GRUB menu, select "ScottOS 8x (Safe Mode)"
2. System boots with minimal services
3. Use for troubleshooting

### Recovery Mode

1. At GRUB menu, select "ScottOS 8x (Recovery Mode)"
2. Single-user shell access
3. Can repair filesystems and fix issues

## Advanced Boot Topics

### Secure Boot

```bash
# Check Secure Boot status
bootctl status

# Enable/Disable Secure Boot
# (Requires BIOS/UEFI access)
```

### Encrypting Boot Partition

```bash
# During installation with LUKS encryption
sudo cryptsetup luksFormat /dev/sdXY
sudo cryptsetup luksOpen /dev/sdXY scottos
```

### Custom Kernel

```bash
# Build custom kernel
cd /usr/src/linux-scottos
make menuconfig
make -j$(nproc)
sudo make install
```

## See Also

- GRUB Manual: https://www.gnu.org/software/grub/manual/
- systemd Boot: https://www.freedesktop.org/wiki/Software/systemd/boot/
- Kernel Parameters: https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html
