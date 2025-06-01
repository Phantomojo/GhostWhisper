import unittest
from unittest.mock import patch, MagicMock
from core.message import Message
import transports.http
import transports.smtp
import transports.qr
import transports.localpipe

class TestTransports(unittest.TestCase):
    def setUp(self):
        self.message = Message(sender='alice', receiver='http://localhost', content='Hello')

    @patch('transports.http.requests.post')
    def test_http_send_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        transports.http.send(self.message, self.message.receiver)
        mock_post.assert_called_once()

    @patch('transports.http.requests.post')
    def test_http_send_failure(self, mock_post):
        mock_post.side_effect = Exception('Network error')
        with self.assertRaises(Exception):
            transports.http.send(self.message, self.message.receiver)

    def test_smtp_send_stub(self):
        with patch('transports.smtp.log_devlog') as mock_log:
            transports.smtp.send(self.message, self.message.receiver)
            mock_log.assert_called()

    def test_qr_send_stub(self):
        with patch('transports.qr.log_devlog') as mock_log:
            transports.qr.send(self.message, self.message.receiver)
            mock_log.assert_called()

    def test_localpipe_send_stub(self):
        with patch('transports.localpipe.log_devlog') as mock_log:
            transports.localpipe.send(self.message, self.message.receiver)
            mock_log.assert_called()

if __name__ == '__main__':
    unittest.main()
