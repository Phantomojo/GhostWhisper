import unittest
import os

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ghostwhisper-devlog.txt')

class TestLoggingCompleteness(unittest.TestCase):
    def test_log_file_exists(self):
        self.assertTrue(os.path.exists(LOG_PATH), "Devlog file does not exist")

    def test_log_contains_send_execution(self):
        with open(LOG_PATH, 'r') as f:
            logs = f.read()
        self.assertIn("[EXECUTION] User ran: ghostwhisper send", logs)

    def test_log_contains_router_usage(self):
        with open(LOG_PATH, 'r') as f:
            logs = f.read()
        self.assertIn("[ROUTER] Using", logs)

    def test_log_contains_transport_send(self):
        with open(LOG_PATH, 'r') as f:
            logs = f.read()
        self.assertIn("[TRANSPORT] Sent message", logs)

if __name__ == '__main__':
    unittest.main()
