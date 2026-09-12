#!/usr/bin/env python3
"""
ScottOS 8x Boot Manager
Handles boot sequence, splash screen, and initialization
"""

import logging
import time
import sys
from pathlib import Path
from typing import List, Callable

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)
logger = logging.getLogger(__name__)

class BootService:
    """Represents a service to be loaded during boot"""
    
    def __init__(self, name: str, description: str, callback: Callable):
        self.name = name
        self.description = description
        self.callback = callback
        self.status = "pending"
        self.progress = 0
    
    def start(self) -> bool:
        """Start the service"""
        try:
            self.status = "loading"
            self.callback()
            self.status = "loaded"
            self.progress = 100
            return True
        except Exception as e:
            self.status = "failed"
            logger.error(f"Failed to load {self.name}: {e}")
            return False

class BootManager:
    """Manages the complete boot sequence"""
    
    def __init__(self):
        self.boot_time_start = time.time()
        self.services: List[BootService] = []
        self.boot_complete = False
        self.splash_screen_enabled = True
        logger.info("Boot Manager Initialized")
    
    def register_service(self, service: BootService) -> None:
        """Register a service to be loaded during boot"""
        self.services.append(service)
        logger.info(f"Service registered: {service.name}")
    
    def load_services(self) -> bool:
        """Load all registered services"""
        logger.info(f"Loading {len(self.services)} services...")
        total_services = len(self.services)
        
        for index, service in enumerate(self.services):
            progress = int((index / total_services) * 100)
            logger.info(f"[{progress}%] Loading: {service.description}")
            
            if not service.start():
                logger.error(f"Failed to load: {service.name}")
                return False
            
            time.sleep(0.1)  # Small delay for boot sequence
        
        return True
    
    def complete_boot(self) -> None:
        """Mark boot as complete"""
        boot_duration = time.time() - self.boot_time_start
        self.boot_complete = True
        logger.info(f"Boot Complete! Total time: {boot_duration:.2f}s")
    
    def get_boot_status(self) -> dict:
        """Get current boot status"""
        loaded = sum(1 for s in self.services if s.status == "loaded")
        failed = sum(1 for s in self.services if s.status == "failed")
        
        return {
            'boot_complete': self.boot_complete,
            'total_services': len(self.services),
            'loaded_services': loaded,
            'failed_services': failed,
            'boot_duration': time.time() - self.boot_time_start,
            'services': [
                {'name': s.name, 'status': s.status, 'progress': s.progress}
                for s in self.services
            ]
        }

if __name__ == "__main__":
    manager = BootManager()
    print("Boot Manager Ready")
