#!/usr/bin/env python3
"""
ScottOS 8x Taskbar
Windows 11-style centered taskbar with app launcher and system tray
"""

import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TaskbarApp:
    """Represents an app pinned to taskbar"""
    
    def __init__(self, name: str, icon: str, command: str):
        self.name = name
        self.icon = icon
        self.command = command
        self.is_running = False
    
    def launch(self):
        """Launch the application"""
        logger.info(f"Launching {self.name}")
        self.is_running = True
    
    def close(self):
        """Close the application"""
        logger.info(f"Closing {self.name}")
        self.is_running = False

class Taskbar:
    """Windows 11-style taskbar"""
    
    def __init__(self):
        self.apps: List[TaskbarApp] = []
        self.position = "bottom-center"  # Windows 11 centered
        self.height = 48
        self.theme = "fluent-dark"
        self.system_tray_visible = True
        logger.info("Taskbar initialized")
        self.init_default_apps()
    
    def init_default_apps(self):
        """Initialize default pinned apps"""
        default_apps = [
            TaskbarApp("File Explorer", "folder.png", "nautilus"),
            TaskbarApp("Settings", "settings.png", "gnome-control-center"),
            TaskbarApp("Chrome", "chrome.png", "google-chrome"),
            TaskbarApp("Terminal", "terminal.png", "gnome-terminal"),
            TaskbarApp("Store", "store.png", "scottos-store"),
        ]
        self.apps.extend(default_apps)
        logger.info(f"Initialized {len(self.apps)} default apps")
    
    def add_app(self, app: TaskbarApp):
        """Add app to taskbar"""
        self.apps.append(app)
        logger.info(f"App added to taskbar: {app.name}")
    
    def remove_app(self, app_name: str):
        """Remove app from taskbar"""
        self.apps = [app for app in self.apps if app.name != app_name]
        logger.info(f"App removed from taskbar: {app_name}")
    
    def get_running_apps(self) -> List[TaskbarApp]:
        """Get list of running apps"""
        return [app for app in self.apps if app.is_running]
    
    def render(self) -> Dict:
        """Render taskbar UI"""
        return {
            'position': self.position,
            'height': self.height,
            'theme': self.theme,
            'apps': [{'name': app.name, 'icon': app.icon, 'running': app.is_running} 
                     for app in self.apps],
            'system_tray': self.system_tray_visible
        }

if __name__ == "__main__":
    taskbar = Taskbar()
    print("Taskbar Config:", taskbar.render())
