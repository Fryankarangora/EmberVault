# test_embervault.py
"""
Tests for EmberVault module.
"""

import unittest
from embervault import EmberVault

class TestEmberVault(unittest.TestCase):
    """Test cases for EmberVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EmberVault()
        self.assertIsInstance(instance, EmberVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EmberVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
