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

    @patch('cli.ghostwhisper.route_message')
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

    @patch('subprocess.run')
    def test_listen_command(self, mock_subprocess_run):
        mock_subprocess_run.return_value = None
        test_args = ['ghostwhisper', 'listen', '--port', '8000']
        with patch.object(sys, 'argv', test_args):
            import cli.ghostwhisper as gw
            with patch('builtins.print') as mock_print:
                gw.main()
                mock_print.assert_any_call("Starting listener on port 8000...")
                with open(LOG_PATH, 'r') as f:
                    logs = f.read()
                self.assertIn("[LISTENER] Starting FastAPI listener on port 8000", logs)

    @patch('core.discovery.discover_peers')
    def test_discover_command(self, mock_discover):
        mock_discover.return_value = {'192.168.1.2': ['http', 'smtp'], '192.168.1.3': ['qr']}
        test_args = ['ghostwhisper', 'discover', '--timeout', '3']
        with patch.object(sys, 'argv', test_args):
            import cli.ghostwhisper as gw
            with patch('builtins.print') as mock_print:
                gw.main()
                mock_discover.assert_called_once_with(timeout=3)

if __name__ == '__main__':
    unittest.main()
