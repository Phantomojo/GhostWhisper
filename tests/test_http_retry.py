import unittest
from unittest.mock import patch, MagicMock
from core.message import Message
import transports.http

class TestHttpRetry(unittest.TestCase):
    def setUp(self):
        self.message = Message(sender='alice', receiver='http://localhost', content='Hello')

    @patch('transports.http.requests.post')
    def test_http_send_success_on_first_try(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        transports.http.send(self.message, self.message.receiver)
        mock_post.assert_called_once()

    @patch('transports.http.requests.post')
    def test_http_send_retries_and_fails(self, mock_post):
        mock_post.side_effect = Exception('Network error')
        with self.assertRaises(Exception):
            transports.http.send(self.message, self.message.receiver)
        self.assertEqual(mock_post.call_count, 3)

    @patch('transports.http.requests.post')
    def test_http_send_retries_and_succeeds(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        # Fail twice, succeed on third try
        mock_post.side_effect = [Exception('Network error'), Exception('Network error'), mock_response]

        transports.http.send(self.message, self.message.receiver)
        self.assertEqual(mock_post.call_count, 3)

if __name__ == '__main__':
    unittest.main()
