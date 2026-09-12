#!/usr/bin/env python3
"""
ScottOS 8x Boot Logger
Logs boot events and diagnostics
"""

import logging
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List

class BootLogger:
    """Manages boot logging and diagnostics"""
    
    def __init__(self, log_file: str = "/var/log/scottos-boot.log"):
        self.log_file = Path(log_file)
        self.log_dir = self.log_file.parent
        self.boot_events: List[Dict] = []
        self.boot_start_time = datetime.now()
        
        # Create log directory if needed
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # Setup logging
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - [%(levelname)s] - %(name)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("Boot Logger Initialized")
    
    def log_event(self, event_name: str, status: str, duration: float = None, details: Dict = None):
        """Log a boot event"""
        event = {
            'timestamp': datetime.now().isoformat(),
            'event': event_name,
            'status': status,
            'duration': duration,
            'details': details or {}
        }
        
        self.boot_events.append(event)
        
        if status == "success":
            self.logger.info(f"✓ {event_name}")
        elif status == "warning":
            self.logger.warning(f"⚠ {event_name}")
        else:
            self.logger.error(f"✗ {event_name}")
    
    def log_service_startup(self, service_name: str, duration: float):
        """Log service startup"""
        self.log_event(
            f"Service Started: {service_name}",
            "success",
            duration=duration
        )
    
    def log_error(self, error_name: str, error_message: str, error_type: str = "critical"):
        """Log boot error"""
        self.log_event(
            error_name,
            "error",
            details={
                'error_message': error_message,
                'error_type': error_type
            }
        )
    
    def save_boot_report(self, filename: str = "boot-report.json"):
        """Save boot report to file"""
        report = {
            'boot_start': self.boot_start_time.isoformat(),
            'boot_end': datetime.now().isoformat(),
            'total_events': len(self.boot_events),
            'events': self.boot_events
        }
        
        report_path = self.log_dir / filename
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        self.logger.info(f"Boot report saved: {report_path}")
        return report_path
    
    def get_boot_summary(self) -> Dict:
        """Get boot summary statistics"""
        successful = sum(1 for e in self.boot_events if e['status'] == 'success')
        warnings = sum(1 for e in self.boot_events if e['status'] == 'warning')
        errors = sum(1 for e in self.boot_events if e['status'] == 'error')
        total_duration = sum(e['duration'] for e in self.boot_events if e['duration'])
        
        return {
            'total_events': len(self.boot_events),
            'successful': successful,
            'warnings': warnings,
            'errors': errors,
            'total_duration': total_duration
        }

if __name__ == "__main__":
    boot_logger = BootLogger()
    boot_logger.log_event("Kernel Initialization", "success", duration=0.5)
    boot_logger.log_event("Device Detection", "success", duration=1.2)
    boot_logger.log_event("Filesystem Check", "success", duration=2.1)
    print("\nBoot Summary:")
    print(boot_logger.get_boot_summary())
