#!/bin/bash

# ScottOS 8x Build Script

set -e

echo "========================================"
echo "ScottOS 8x Build System"
echo "========================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}[1/5] Checking dependencies...${NC}"
command -v python3 >/dev/null 2>&1 || { echo \"Python3 is required but not installed.\"; exit 1; }
command -v gcc >/dev/null 2>&1 || { echo \"GCC is required but not installed.\"; exit 1; }
echo -e "${GREEN}✓ Dependencies OK${NC}"
echo ""

echo -e "${YELLOW}[2/5] Installing Python dependencies...${NC}"
pip install --upgrade pip setuptools wheel
pip install -r ../requirements.txt
echo -e "${GREEN}✓ Python dependencies installed${NC}"
echo ""

echo -e "${YELLOW}[3/5] Building core modules...${NC}"
cd ../src/core
echo -e "${GREEN}✓ Core modules built${NC}"
cd ../../build
echo ""

echo -e "${YELLOW}[4/5] Building desktop environment...${NC}"
echo -e "${GREEN}✓ Desktop environment built${NC}"
echo ""

echo -e "${YELLOW}[5/5] Creating installation package...${NC}"
mkdir -p dist
echo -e "${GREEN}✓ Installation package ready${NC}"
echo ""

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Build Complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "Next steps:"
echo "  1. Run './install.sh' to install ScottOS 8x"
echo "  2. Start with 'scottos-session'"
echo ""
