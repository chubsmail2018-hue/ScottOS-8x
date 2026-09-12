#!/usr/bin/env python3
"""
ScottOS 8x Settings Application
System settings and preferences
"""

import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Settings:
    """System settings manager"""
    
    def __init__(self):
        self.settings = {
            'display': {
                'resolution': '1920x1080',
                'refresh_rate': 60,
                'brightness': 100,
                'scale': 100,
                'night_light': False
            },
            'sound': {
                'volume': 100,
                'muted': False,
                'enable_notifications': True
            },
            'theme': {
                'current': 'fluent-dark',
                'accent_color': '#0078D4'
            },
            'system': {
                'language': 'en_US',
                'timezone': 'UTC',
                'auto_update': True
            },
            'privacy': {
                'analytics': True,
                'tracking': False
            },
            'apps': {
                'default_browser': 'google-chrome',
                'default_terminal': 'gnome-terminal'
            }
        }
        logger.info("Settings initialized")
    
    def get_setting(self, category: str, key: str) -> Any:
        """Get a setting value"""
        if category in self.settings and key in self.settings[category]:
            return self.settings[category][key]
        logger.warning(f"Setting not found: {category}.{key}")
        return None
    
    def set_setting(self, category: str, key: str, value: Any) -> bool:
        """Set a setting value"""
        if category not in self.settings:
            logger.error(f"Category not found: {category}")
            return False
        
        self.settings[category][key] = value
        logger.info(f"Setting changed: {category}.{key} = {value}")
        return True
    
    def get_all_settings(self) -> Dict:
        """Get all settings"""
        return self.settings
    
    def reset_to_defaults(self) -> bool:
        """Reset all settings to defaults"""
        logger.info("Resetting settings to defaults")
        self.__init__()
        return True

if __name__ == "__main__":
    settings = Settings()
    print("Current Theme:", settings.get_setting('theme', 'current'))
    settings.set_setting('display', 'brightness', 75)
    print("Settings:", settings.get_all_settings())
