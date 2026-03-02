import unittest
import sys
import os

# This makes sure the test can find the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.poi_engine import POIEngine

class TestHPI(unittest.TestCase):
    def setUp(self):
        self.engine = POIEngine(threshold=2)

    def test_valid_delivery(self):
        # Case: 2 people signed (Worker + Witness)
        result = self.engine.verify_delivery("event_123", ["sig_worker", "sig_witness"])
        self.assertEqual(result["status"], "VERIFIED")

    def test_invalid_delivery(self):
        # Case: Only 1 person signed
        result = self.engine.verify_delivery("event_123", ["sig_worker"])
        self.assertEqual(result["status"], "PENDING")

if __name__ == '__main__':
    unittest.main()
