# ScottOS 8x Dockerfile
FROM ubuntu:22.04

LABEL maintainer="ScottOS Contributors"
LABEL description="ScottOS 8x - Windows 11 Inspired Linux OS"

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Install base packages
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-dev \
    git build-essential cmake \
    qt5-default libx11-dev libxext-dev libxrender-dev \
    fonts-liberation xfonts-75dpi xfonts-100dpi \
    x11-apps x11-common x11-xserver-utils \
    mesa-utils libgl1-mesa-glx \
    alsaconf alsa-utils pulseaudio \
    curl wget gnupg2 lsb-release apt-transport-https \
    locales tzdata \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Generate locale
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

# Install Google Chrome (optional, can be skipped)
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* || echo "Chrome installation optional"

# Create non-root user
RUN useradd -m -s /bin/bash -G audio,video user
RUN echo "user:user" | chpasswd

# Copy ScottOS 8x
COPY --chown=user:user . /home/user/ScottOS-8x
WORKDIR /home/user/ScottOS-8x

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Create startup script
RUN echo '#!/bin/bash' > /start.sh && \
    echo 'set -e' >> /start.sh && \
    echo 'echo ""' >> /start.sh && \
    echo 'echo "╔════════════════════════════════════════════════════════╗"' >> /start.sh && \
    echo 'echo "║   ScottOS 8x - Windows 11 Inspired Linux OS             ║"' >> /start.sh && \
    echo 'echo "║   Running in Docker Container                          ║"' >> /start.sh && \
    echo 'echo "╚════════════════════════════════════════════════════════╝"' >> /start.sh && \
    echo 'echo ""' >> /start.sh && \
    echo 'echo "Available commands:"' >> /start.sh && \
    echo 'echo "  Boot Components:"' >> /start.sh && \
    echo 'echo "    - python3 src/boot/splash-screen.py"' >> /start.sh && \
    echo 'echo "    - python3 src/boot/boot-animation.py"' >> /start.sh && \
    echo 'echo "    - python3 src/boot/boot-manager.py"' >> /start.sh && \
    echo 'echo ""' >> /start.sh && \
    echo 'echo "  Desktop Environment:"' >> /start.sh && \
    echo 'echo "    - python3 src/desktop-environment/session-manager.py"' >> /start.sh && \
    echo 'echo "    - python3 src/taskbar/taskbar.py"' >> /start.sh && \
    echo 'echo ""' >> /start.sh && \
    echo 'echo "  System Apps:"' >> /start.sh && \
    echo 'echo "    - python3 src/system-apps/file-explorer.py"' >> /start.sh && \
    echo 'echo "    - python3 src/system-apps/settings.py"' >> /start.sh && \
    echo 'echo ""' >> /start.sh && \
    echo 'echo "  Other:"' >> /start.sh && \
    echo 'echo "    - bash quick-start.sh"' >> /start.sh && \
    echo 'echo "    - bash build/build.sh"' >> /start.sh && \
    echo 'echo ""' >> /start.sh && \
    echo '/bin/bash' >> /start.sh && \
    chmod +x /start.sh

# Set user
USER user

# Expose ports (for future services)
EXPOSE 8000 8080 9000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python3 -c "import sys; sys.exit(0)" || exit 1

ENTRYPOINT ["/start.sh"]
