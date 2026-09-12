#!/bin/bash

# ScottOS 8x Docker Compose Setup
# Quick start with Docker Compose

echo "ScottOS 8x - Docker Compose Setup"
echo "==================================="
echo ""

# Create docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  scottos-8x:
    image: scottos-8x:latest
    build:
      context: .
      dockerfile: Dockerfile
    container_name: scottos-8x-dev
    
    environment:
      - DISPLAY=${DISPLAY}
      - QT_X11_GL_INTEGRATION=glvnd
    
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
      - ${HOME}/.Xauthority:/home/user/.Xauthority:rw
      - ./:/opt/scottos
    
    stdin_open: true
    tty: true
    
    networks:
      - scottos-network
    
    # Resource limits
    mem_limit: 4g
    cpus: 2

networks:
  scottos-network:
    driver: bridge
EOF

echo "✓ docker-compose.yml created"
echo ""

# Create Dockerfile
cat > Dockerfile << 'EOF'
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install base packages
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    git build-essential \
    qt5-default libx11-dev libxext-dev \
    fonts-liberation xfonts-75dpi xfonts-100dpi \
    x11-apps x11-common \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -s /bin/bash user

# Copy ScottOS 8x
COPY . /opt/scottos
WORKDIR /opt/scottos

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create startup script
RUN echo '#!/bin/bash' > /start.sh && \
    echo 'echo "ScottOS 8x - Docker Container"' >> /start.sh && \
    echo 'echo "=============================="' >> /start.sh && \
    echo 'echo ""' >> /start.sh && \
    echo 'echo "Available commands:"' >> /start.sh && \
    echo 'echo "  - python3 src/boot/splash-screen.py"' >> /start.sh && \
    echo 'echo "  - python3 src/boot/boot-animation.py"' >> /start.sh && \
    echo 'echo "  - python3 src/desktop-environment/session-manager.py"' >> /start.sh && \
    echo 'echo "  - python3 src/taskbar/taskbar.py"' >> /start.sh && \
    echo 'echo "  - bash quick-start.sh"' >> /start.sh && \
    echo 'echo ""' >> /start.sh && \
    echo '/bin/bash' >> /start.sh && \
    chmod +x /start.sh

USER user
ENTRYPOINT ["/start.sh"]
EOF

echo "✓ Dockerfile created"
echo ""

# Build image
echo "Building Docker image..."
docker-compose build

echo ""
echo "✓ Docker setup complete!"
echo ""
echo "To start ScottOS 8x in Docker:"
echo "  docker-compose up -it"
echo ""
echo "Or run a specific component:"
echo "  docker-compose run scottos-8x python3 src/boot/splash-screen.py"
echo ""
