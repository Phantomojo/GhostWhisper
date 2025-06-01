import unittest
import subprocess
import time
import requests
import threading
import os

class TestListenIntegration(unittest.TestCase):
    def setUp(self):
        self.port = 9000
        self.listener_process = None

    def start_listener(self):
        # Start the listener CLI command as a subprocess
        self.listener_process = subprocess.Popen(
            ['python3', '-m', 'cli.ghostwhisper', 'listen', '--port', str(self.port)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Give the server some time to start
        time.sleep(3)

    def stop_listener(self):
        if self.listener_process:
            self.listener_process.terminate()
            self.listener_process.wait()

    def test_listener_receives_message(self):
        self.start_listener()

        # Send a test message to the backend
        url = f'http://localhost:{self.port}/receive'
        payload = {
            "sender": "test_sender",
            "receiver": "test_receiver",
            "content": "Integration test message",
            "timestamp": "2024-01-01T00:00:00Z"
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.json().get("status", ""))

        # Check listener output for message receipt indication
        # Read stdout lines
        output_lines = []
        try:
            if self.listener_process.stdout:
                for _ in range(10):
                    line = self.listener_process.stdout.readline()
                    if line:
                        output_lines.append(line.strip())
        except Exception:
            pass

        self.assertTrue(any("Message received" in line or "Integration test message" in line for line in output_lines))

        self.stop_listener()

if __name__ == "__main__":
    unittest.main()
