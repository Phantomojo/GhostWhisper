import unittest
from unittest.mock import patch, MagicMock
from core.router import route_message
from core.message import Message

class TestRouter(unittest.TestCase):
    def setUp(self):
        self.message = Message(sender='alice', receiver='bob', content='Hello')

    @patch('transports.http.send')
    def test_route_http(self, mock_send):
        route_message(self.message, 'http')
        mock_send.assert_called_once_with(self.message, self.message.receiver)

    @patch('transports.smtp.send')
    def test_route_smtp(self, mock_send):
        route_message(self.message, 'smtp')
        mock_send.assert_called_once_with(self.message, self.message.receiver)

    @patch('transports.qr.send')
    def test_route_qr(self, mock_send):
        route_message(self.message, 'qr')
        mock_send.assert_called_once_with(self.message, self.message.receiver)

    @patch('transports.localpipe.send')
    def test_route_localpipe(self, mock_send):
        route_message(self.message, 'localpipe')
        mock_send.assert_called_once_with(self.message, self.message.receiver)

    def test_route_unknown(self):
        with self.assertRaises(ValueError):
            route_message(self.message, 'unknown')

if __name__ == '__main__':
    unittest.main()
