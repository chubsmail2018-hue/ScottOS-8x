#!/usr/bin/env python3
"""
ScottOS 8x Core Tests
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from core.kernel import ScottOSKernel

class TestKernel:
    """Test ScottOS Kernel"""
    
    def test_kernel_initialization(self):
        """Test kernel initializes correctly"""
        kernel = ScottOSKernel()
        assert kernel.version == "8.0.0"
        assert kernel.name == "ScottOS 8x"
        assert isinstance(kernel.services, dict)
    
    def test_service_loading(self):
        """Test loading services"""
        kernel = ScottOSKernel()
        
        class TestService:
            def start(self):
                pass
        
        result = kernel.load_service('test', TestService)
        assert result is True
        assert 'test' in kernel.services

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
