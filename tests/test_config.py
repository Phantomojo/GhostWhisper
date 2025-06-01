import unittest
import os
import json
from unittest.mock import patch, mock_open
from core.config import Config

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.test_profiles = {
            "default": {
                "name": "default",
                "key": "abc123"
            }
        }

    @patch('builtins.open', new_callable=mock_open, read_data='{"default": {"name": "default", "key": "abc123"}}')
    @patch('os.path.exists', return_value=True)
    def test_load_profiles(self, mock_exists, mock_file):
        self.config._load_profiles()
        self.assertEqual(self.config.profiles, self.test_profiles)

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.makedirs')
    def test_save_profiles(self, mock_makedirs, mock_file):
        self.config.profiles = self.test_profiles
        self.config.save_profiles()
        mock_makedirs.assert_called()
        mock_file().write.assert_called()

    def test_add_key_stub(self):
        with patch('core.config.log_devlog') as mock_log:
            self.config.add_key('default', 'keydata')
            mock_log.assert_called()

if __name__ == '__main__':
    unittest.main()
