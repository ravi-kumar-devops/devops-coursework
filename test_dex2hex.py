import unittest
from Dex2Hex import decimal_to_hex

class TestDex2Hex(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(decimal_to_hex(15), "F")
        
    def test_no_input(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(None)
            
    def test_non_integer(self):
        with self.assertRaises(ValueError):
            decimal_to_hex("abc")
