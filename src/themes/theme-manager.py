#!/usr/bin/env python3
"""
ScottOS 8x Theme Manager
Manages visual themes, colors, icons, and wallpapers
"""

import logging
from pathlib import Path
from typing import Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Theme:
    """Represents a visual theme"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.colors = {}
        self.icons = {}
        self.wallpaper = None
    
    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'description': self.description,
            'colors': self.colors,
            'icons': self.icons,
            'wallpaper': self.wallpaper
        }

class ThemeManager:
    """Manages application themes"""
    
    def __init__(self):
        self.current_theme = None
        self.themes: Dict[str, Theme] = {}
        self.themes_dir = Path(__file__).parent / 'themes'
        logger.info("Theme Manager initialized")
        self.create_default_themes()
    
    def create_default_themes(self):
        """Create default Windows 11-inspired themes"""
        
        # Fluent Dark Theme
        fluent_dark = Theme(
            "Fluent Dark",
            "Windows 11 Fluent Design Dark Theme"
        )
        fluent_dark.colors = {
            'primary': '#0078D4',
            'background': '#1E1E1E',
            'text': '#FFFFFF',
            'accent': '#0078D4',
            'secondary': '#323232',
            'border': '#3E3E42'
        }
        fluent_dark.wallpaper = 'wallpapers/windows11-dark.png'
        self.themes['fluent-dark'] = fluent_dark
        
        # Fluent Light Theme
        fluent_light = Theme(
            "Fluent Light",
            "Windows 11 Fluent Design Light Theme"
        )
        fluent_light.colors = {
            'primary': '#0078D4',
            'background': '#FFFFFF',
            'text': '#000000',
            'accent': '#0078D4',
            'secondary': '#F3F3F3',
            'border': '#E1E1E1'
        }
        fluent_light.wallpaper = 'wallpapers/windows11-light.png'
        self.themes['fluent-light'] = fluent_light
        
        logger.info(f"Created {len(self.themes)} default themes")
    
    def set_theme(self, theme_name: str) -> bool:
        """Set active theme"""
        if theme_name not in self.themes:
            logger.error(f"Theme not found: {theme_name}")
            return False
        
        self.current_theme = self.themes[theme_name]
        logger.info(f"Theme changed to: {theme_name}")
        return True
    
    def get_current_theme(self) -> Theme:
        """Get current active theme"""
        if self.current_theme is None:
            self.set_theme('fluent-dark')
        return self.current_theme
    
    def list_themes(self) -> List[str]:
        """List all available themes"""
        return list(self.themes.keys())
    
    def add_custom_theme(self, theme: Theme) -> bool:
        """Add custom theme"""
        if theme.name in self.themes:
            logger.warning(f"Theme already exists: {theme.name}")
            return False
        
        self.themes[theme.name.lower().replace(' ', '-')] = theme
        logger.info(f"Custom theme added: {theme.name}")
        return True

if __name__ == "__main__":
    manager = ThemeManager()
    manager.set_theme('fluent-dark')
    print("Current Theme:", manager.get_current_theme().to_dict())
    print("Available Themes:", manager.list_themes())
