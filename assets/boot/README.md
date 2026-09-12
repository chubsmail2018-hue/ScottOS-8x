# ScottOS 8x Boot Assets

This directory contains all boot-related assets including splash screens, animations, and GRUB themes.

## Files

- `boot-splash.svg` - Main boot splash screen (SVG format for scalability)
- `boot-splash.png` - Pre-rendered boot splash screen (1920x1080)
- `grub-theme/` - GRUB bootloader theme files
- `fonts/` - Boot screen fonts
- `icons/` - Boot screen icons

## Boot Sequence

1. **GRUB Bootloader** (grub-config.cfg)
   - Displays GRUB menu
   - Applies GRUB theme
   - Loads kernel and initramfs

2. **Kernel Boot** (kernel-parameters.conf)
   - Initializes hardware
   - Mounts filesystems
   - Loads kernel modules

3. **Initramfs** (initramfs-generator.sh)
   - Early-stage boot process
   - Device detection
   - Filesystem mounting

4. **Splash Screen** (splash-screen.py)
   - Shows boot animation
   - Displays progress bar
   - Plays boot sound

5. **Service Startup** (boot-manager.py)
   - Loads system services
   - Initializes components
   - Starts desktop environment

## Creating Boot Media

```bash
# Create bootable USB
sudo dd if=scottos-8x.iso of=/dev/sdX bs=4M status=progress
sync

# Or use GNOME Disks
gnome-disks
```

## Customization

To customize boot assets:

1. Edit `boot-splash.svg` with Inkscape or any SVG editor
2. Export to PNG at 1920x1080 resolution
3. Place in `/usr/share/scottos/backgrounds/`
4. Update boot configuration in `/etc/scottos/boot.conf`
