import unittest
from unittest.mock import patch
from transports.smtp import send as smtp_send
from transports.qr import send as qr_send
from transports.localpipe import send as localpipe_send
from core.message import Message

class TestExtraTransports(unittest.TestCase):
    def setUp(self):
        self.message = Message(sender="alice", receiver="bob", content="Test message", timestamp="2024-01-01T00:00:00Z")

    @patch('transports.smtp.log_devlog')
    def test_smtp_send_stub(self, mock_log):
        smtp_send(self.message, "bob@example.com")
        mock_log.assert_called_with("[TRANSPORT] SMTP send() called - stub implementation")

    @patch('transports.qr.log_devlog')
    def test_qr_send_stub(self, mock_log):
        qr_send(self.message, "bob")
        mock_log.assert_called_with("[TRANSPORT] QR send() called - stub implementation")

    @patch('transports.localpipe.log_devlog')
    def test_localpipe_send_stub(self, mock_log):
        localpipe_send(self.message, "bob")
        mock_log.assert_called_with("[TRANSPORT] Localpipe send() called - stub implementation")

if __name__ == "__main__":
    unittest.main()
