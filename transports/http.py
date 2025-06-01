import requests
from datetime import datetime
import os

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ghostwhisper-devlog.txt')

def log_devlog(entry: str):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {entry}\\n")

import time
import requests
from datetime import datetime
import os

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ghostwhisper-devlog.txt')

def _log_devlog(entry: str):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {entry}\\n")

def send(message, to: str):
    url = to
    headers = {'Content-Type': 'application/json'}
    data = message.serialize()
    max_retries = 3
    backoff = 1  # seconds
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(url, data=data, headers=headers)
            response.raise_for_status()
            _log_devlog(f"[TRANSPORT] Sent message to {url} via POST on attempt {attempt}")
            return
        except Exception as e:
            _log_devlog(f"[TRANSPORT] Attempt {attempt} failed: {e}")
            if attempt == max_retries:
                _log_devlog(f"[ERROR] Failed to send message via HTTP after {max_retries} attempts: {e}")
                raise
            else:
                time.sleep(backoff)
                backoff *= 2  # exponential backoff
