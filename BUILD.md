# ScottOS 8x - Build Instructions

## Prerequisites

- Ubuntu 22.04 LTS or Fedora 38+
- Python 3.10+
- Qt 5.15+ or GTK+ 4.0+
- GCC/Clang compiler
- Git

## Build Steps

### 1. Install Dependencies

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y build-essential qt5-default python3-dev libx11-dev libxext-dev

# Fedora
sudo dnf install -y gcc-c++ qt5-devel python3-devel libX11-devel libXext-devel
```

### 2. Clone and Navigate

```bash
git clone https://github.com/chubsmail2018-hue/ScottOS-8x.git
cd ScottOS-8x
```

### 3. Build Desktop Environment

```bash
cd build
./build.sh
```

### 4. Install

```bash
sudo ./install.sh
```

### 5. Start ScottOS 8x

```bash
scottos-session
```

## Development Setup

```bash
# Install development tools
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Build documentation
make -C docs/ html
```

## Troubleshooting

See TROUBLESHOOTING.md for common issues.
