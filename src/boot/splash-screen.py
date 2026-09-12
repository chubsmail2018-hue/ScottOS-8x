#!/usr/bin/env python3
"""
ScottOS 8x Splash Screen
Windows 11-style boot splash screen with animations
"""

import time
import sys
import logging
from pathlib import Path

try:
    from PyQt5.QtWidgets import QApplication, QSplashScreen, QMainWindow
    from PyQt5.QtGui import QPixmap, QFont, QColor, QPainter
    from PyQt5.QtCore import Qt, QTimer, QRect
    PYQT5_AVAILABLE = True
except ImportError:
    PYQT5_AVAILABLE = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SplashScreen:
    """Windows 11-style boot splash screen"""
    
    def __init__(self, show_gui=True):
        self.show_gui = show_gui and PYQT5_AVAILABLE
        self.start_time = time.time()
        self.boot_messages = [
            "Initializing ScottOS 8x...",
            "Loading kernel modules...",
            "Initializing display server...",
            "Loading sound system...",
            "Starting services...",
            "Loading theme engine...",
            "Initializing taskbar...",
            "Preparing AI assistant...",
            "Loading Chrome integration...",
            "Finalizing boot sequence..."
        ]
        self.current_message_index = 0
        self.progress = 0
        logger.info("Splash Screen Initialized")
    
    def show(self):
        """Display splash screen"""
        if self.show_gui:
            self._show_qt_splash()
        else:
            self._show_terminal_splash()
    
    def _show_qt_splash(self):
        """Show PyQt5 splash screen"""
        try:
            app = QApplication(sys.argv)
            
            # Create splash screen pixmap (Windows 11 blue background)
            pixmap = QPixmap(800, 600)
            pixmap.fill(QColor(30, 30, 30))  # Dark background
            
            splash = QSplashScreen(pixmap)
            splash.show()
            app.processEvents()
            
            # Simulate boot progress
            for i in range(len(self.boot_messages)):
                self.progress = int((i / len(self.boot_messages)) * 100)
                message = self.boot_messages[i]
                
                # Draw on pixmap
                painter = QPainter(pixmap)
                painter.setFont(QFont("Segoe UI", 10))
                painter.setPen(QColor(255, 255, 255))
                
                # Draw ScottOS logo/text
                painter.drawText(QRect(50, 250, 700, 50), Qt.AlignCenter, "ScottOS 8x")
                
                # Draw message
                painter.drawText(QRect(50, 350, 700, 50), Qt.AlignCenter, message)
                
                # Draw progress bar
                progress_width = int((self.progress / 100) * 600)
                painter.fillRect(100, 450, progress_width, 20, QColor(0, 120, 212))
                painter.drawRect(100, 450, 600, 20)
                
                # Draw percentage
                painter.drawText(QRect(50, 480, 700, 50), Qt.AlignCenter, f"{self.progress}%")
                
                painter.end()
                splash.setPixmap(pixmap)
                app.processEvents()
                time.sleep(0.3)
            
            time.sleep(1)
            splash.close()
            app.quit()
        except Exception as e:
            logger.error(f"Failed to show Qt splash: {e}")
            self._show_terminal_splash()
    
    def _show_terminal_splash(self):
        """Show terminal-based splash screen"""
        print("\033[2J\033[H")  # Clear screen
        print("\n" * 5)
        print(" " * 20 + "╔═════════════════════════════════════╗")
        print(" " * 20 + "║                                     ║")
        print(" " * 20 + "║       ScottOS 8x - Booting...       ║")
        print(" " * 20 + "║                                     ║")
        print(" " * 20 + "║   Windows 11 Inspired Linux OS      ║")
        print(" " * 20 + "║                                     ║")
        print(" " * 20 + "╚═════════════════════════════════════╝")
        print("\n")
        
        for i, message in enumerate(self.boot_messages):
            progress = int((i / len(self.boot_messages)) * 100)
            bar_length = 30
            filled = int(bar_length * progress / 100)
            bar = "█" * filled + "░" * (bar_length - filled)
            print(f" " * 15 + f"[{bar}] {progress}%")
            print(f" " * 15 + f"➜ {message}")
            time.sleep(0.3)
        
        print("\n" + " " * 15 + "✓ Boot sequence completed!\n")
    
    def update_message(self, message: str):
        """Update boot message"""
        self.current_message_index += 1
        logger.info(f"Boot: {message}")
    
    def update_progress(self, progress: int):
        """Update boot progress"""
        self.progress = max(0, min(100, progress))
    
    def get_boot_time(self) -> float:
        """Get elapsed boot time"""
        return time.time() - self.start_time

if __name__ == "__main__":
    splash = SplashScreen(show_gui=False)
    splash.show()
