import unittest
from unittest.mock import patch, MagicMock
import sys
from io import StringIO
import os

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ghostwhisper-devlog.txt')

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Clear devlog before each test
        if os.path.exists(LOG_PATH):
            os.remove(LOG_PATH)

    @patch('core.router.http.send')
    def test_cli_send_integration(self, mock_send):
        mock_send.return_value = None
        test_args = ['ghostwhisper', 'send', '--to', 'http://localhost', '--via', 'http', '--message', 'Hello']
        with patch.object(sys, 'argv', test_args):
            import cli.ghostwhisper as gw
            with patch('builtins.print') as mock_print:
                gw.main()
                mock_print.assert_not_called()
                mock_send.assert_called_once()
                with open(LOG_PATH, 'r') as f:
                    logs = f.read()
                self.assertIn('User ran: ghostwhisper send', logs)
                self.assertIn('Message sent via http transport', logs)

if __name__ == '__main__':
    unittest.main()
