import unittest
from unittest.mock import patch, MagicMock
import sys
from io import StringIO
import os

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ghostwhisper-devlog.txt')

class TestCLI(unittest.TestCase):
    def setUp(self):
        # Clear devlog before each test
        if os.path.exists(LOG_PATH):
            os.remove(LOG_PATH)

    @patch('core.router.route_message')
    def test_send_command(self, mock_route):
        test_args = ['ghostwhisper', 'send', '--to', 'http://localhost', '--via', 'http', '--message', 'Hello']
        with patch.object(sys, 'argv', test_args):
            import cli.ghostwhisper as gw
            with patch('builtins.print') as mock_print:
                gw.main()
                mock_route.assert_called_once()
                # Check devlog contains execution log
                with open(LOG_PATH, 'r') as f:
                    logs = f.read()
                self.assertIn('User ran: ghostwhisper send', logs)

    def test_listen_command(self):
        test_args = ['ghostwhisper', 'listen', '--via', 'http']
        with patch.object(sys, 'argv', test_args):
            import cli.ghostwhisper as gw
            with patch('builtins.print') as mock_print:
                gw.main()
                mock_print.assert_called_with("Listening on transport 'http' (stub)")
                with open(LOG_PATH, 'r') as f:
                    logs = f.read()
                self.assertIn("Listen mode selected for transport 'http'", logs)

if __name__ == '__main__':
    unittest.main()
