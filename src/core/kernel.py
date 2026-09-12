#!/usr/bin/env python3
"""
ScottOS 8x Core Kernel
Manages system initialization and core services
"""

import logging
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ScottOSKernel:
    """Main kernel for ScottOS 8x"""
    
    def __init__(self):
        self.version = "8.0.0"
        self.name = "ScottOS 8x"
        self.services = {}
        logger.info(f"{self.name} Kernel v{self.version} Initializing...")
    
    def load_service(self, service_name, service_class):
        """Load a system service"""
        try:
            self.services[service_name] = service_class()
            logger.info(f"✓ Service loaded: {service_name}")
            return True
        except Exception as e:
            logger.error(f"✗ Failed to load {service_name}: {e}")
            return False
    
    def start_services(self):
        """Start all system services"""
        logger.info("Starting system services...")
        for name, service in self.services.items():
            try:
                if hasattr(service, 'start'):
                    service.start()
                    logger.info(f"✓ Started: {name}")
            except Exception as e:
                logger.error(f"✗ Failed to start {name}: {e}")
    
    def shutdown(self):
        """Graceful shutdown"""
        logger.info("Shutting down ScottOS 8x...")
        for name, service in reversed(list(self.services.items())):
            try:
                if hasattr(service, 'stop'):
                    service.stop()
                    logger.info(f"✓ Stopped: {name}")
            except Exception as e:
                logger.error(f"✗ Failed to stop {name}: {e}")

if __name__ == "__main__":
    kernel = ScottOSKernel()
    kernel.start_services()
