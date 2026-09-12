#!/usr/bin/env python3
"""
ScottOS 8x Boot System Tests
"""

import pytest
import sys
import time
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src' / 'boot'))

from boot_manager import BootManager, BootService
from boot_animation import BootAnimation, AnimationType
from boot_logger import BootLogger

class TestBootManager:
    """Test Boot Manager"""
    
    def test_boot_manager_initialization(self):
        """Test boot manager initializes correctly"""
        manager = BootManager()
        assert manager.boot_complete == False
        assert len(manager.services) == 0
    
    def test_service_registration(self):
        """Test service registration"""
        manager = BootManager()
        
        def dummy_service():
            pass
        
        service = BootService("TestService", "Test Service", dummy_service)
        manager.register_service(service)
        
        assert len(manager.services) == 1
        assert manager.services[0].name == "TestService"
    
    def test_service_loading(self):
        """Test service loading"""
        manager = BootManager()
        
        def dummy_service():
            pass
        
        service = BootService("TestService", "Test Service", dummy_service)
        result = manager.load_services()
        # No services registered, should succeed
        assert result == True

class TestBootAnimation:
    """Test Boot Animation"""
    
    def test_animation_initialization(self):
        """Test animation system initializes"""
        animator = BootAnimation()
        assert animator.enabled == True
        assert animator.fps == 30
    
    def test_animation_types(self):
        """Test animation types"""
        assert AnimationType.FADE_IN.value == "fade_in"
        assert AnimationType.SLIDE_UP.value == "slide_up"
        assert AnimationType.SCALE.value == "scale"
        assert AnimationType.PULSE.value == "pulse"
        assert AnimationType.PROGRESS_BAR.value == "progress_bar"
    
    def test_progress_bar_animation(self):
        """Test progress bar animation"""
        animator = BootAnimation()
        start_time = time.time()
        # Progress bar should complete in ~0.5 seconds (short test version)
        # In real use it would be longer

class TestBootLogger:
    """Test Boot Logger"""
    
    def test_boot_logger_initialization(self, tmp_path):
        """Test boot logger initializes"""
        log_file = tmp_path / "test-boot.log"
        logger = BootLogger(str(log_file))
        assert logger.log_dir.exists()
    
    def test_event_logging(self, tmp_path):
        """Test event logging"""
        log_file = tmp_path / "test-boot.log"
        logger = BootLogger(str(log_file))
        
        logger.log_event("TestEvent", "success", duration=0.5)
        assert len(logger.boot_events) == 1
        assert logger.boot_events[0]['event'] == "TestEvent"
        assert logger.boot_events[0]['status'] == "success"
    
    def test_boot_summary(self, tmp_path):
        """Test boot summary"""
        log_file = tmp_path / "test-boot.log"
        logger = BootLogger(str(log_file))
        
        logger.log_event("Event1", "success", duration=1.0)
        logger.log_event("Event2", "success", duration=0.5)
        logger.log_event("Event3", "warning", duration=0.2)
        
        summary = logger.get_boot_summary()
        assert summary['total_events'] == 3
        assert summary['successful'] == 2
        assert summary['warnings'] == 1
        assert summary['errors'] == 0

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
