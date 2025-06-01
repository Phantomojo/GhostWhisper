import unittest
from fastapi.testclient import TestClient
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'backend')))
from app import app, LOG_PATH, RECEIVED_MESSAGES_LOG

class TestBackend(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        # Clear logs before each test
        if os.path.exists(LOG_PATH):
            os.remove(LOG_PATH)
        if os.path.exists(RECEIVED_MESSAGES_LOG):
            os.remove(RECEIVED_MESSAGES_LOG)

    def test_receive_valid_message(self):
        payload = {
            "sender": "alice",
            "receiver": "bob",
            "content": "Hello Bob!",
            "timestamp": "2024-01-01T00:00:00Z"
        }
        response = self.client.post("/receive", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.json().get("status", ""))
        # Check logs
        with open(LOG_PATH, 'r') as f:
            logs = f.read()
        self.assertIn("Message received from alice to bob", logs)
        with open(RECEIVED_MESSAGES_LOG, 'r') as f:
            received = f.read()
        self.assertIn("Hello Bob!", received)

    def test_receive_invalid_json(self):
        response = self.client.post("/receive", data="not a json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid JSON payload", response.json().get("detail", ""))

    def test_receive_invalid_message_format(self):
        # Missing required fields
        payload = {"foo": "bar"}
        response = self.client.post("/receive", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid message format", response.json().get("detail", ""))

if __name__ == "__main__":
    unittest.main()
