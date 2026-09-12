#!/usr/bin/env python3
"""
ScottOS 8x File Explorer
Windows 11-style file manager
"""

import logging
from pathlib import Path
from typing import List, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FileExplorer:
    """File manager application"""
    
    def __init__(self):
        self.current_path = Path.home()
        self.history = [self.current_path]
        self.history_index = 0
        logger.info("File Explorer initialized")
    
    def navigate_to(self, path: str) -> bool:
        """Navigate to a directory"""
        target = Path(path).expanduser()
        
        if not target.exists():
            logger.error(f"Path does not exist: {path}")
            return False
        
        if not target.is_dir():
            logger.error(f"Path is not a directory: {path}")
            return False
        
        self.current_path = target
        self.history.append(target)
        self.history_index = len(self.history) - 1
        logger.info(f"Navigated to: {self.current_path}")
        return True
    
    def get_contents(self) -> List[Dict]:
        """Get directory contents"""
        contents = []
        try:
            for item in sorted(self.current_path.iterdir()):
                contents.append({
                    'name': item.name,
                    'type': 'folder' if item.is_dir() else 'file',
                    'path': str(item),
                    'size': item.stat().st_size if item.is_file() else 0,
                    'modified': item.stat().st_mtime
                })
        except PermissionError:
            logger.error(f"Permission denied: {self.current_path}")
        
        return contents
    
    def go_back(self) -> bool:
        """Go back in history"""
        if self.history_index > 0:
            self.history_index -= 1
            self.current_path = self.history[self.history_index]
            logger.info(f"Navigated back to: {self.current_path}")
            return True
        return False
    
    def go_forward(self) -> bool:
        """Go forward in history"""
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.current_path = self.history[self.history_index]
            logger.info(f"Navigated forward to: {self.current_path}")
            return True
        return False
    
    def create_folder(self, name: str) -> bool:
        """Create a new folder"""
        try:
            new_folder = self.current_path / name
            new_folder.mkdir(exist_ok=False)
            logger.info(f"Folder created: {new_folder}")
            return True
        except Exception as e:
            logger.error(f"Failed to create folder: {e}")
            return False
    
    def delete_item(self, name: str) -> bool:
        """Delete a file or folder"""
        try:
            item = self.current_path / name
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                import shutil
                shutil.rmtree(item)
            logger.info(f"Deleted: {item}")
            return True
        except Exception as e:
            logger.error(f"Failed to delete item: {e}")
            return False

if __name__ == "__main__":
    explorer = FileExplorer()
    print(f"Current Path: {explorer.current_path}")
    print(f"Contents: {explorer.get_contents()[:5]}")
