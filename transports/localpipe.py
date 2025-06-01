from datetime import datetime
import os

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ghostwhisper-devlog.txt')

def log_devlog(entry: str):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {entry}\\n")

def send(message, to: str):
    log_devlog("[TRANSPORT] Localpipe send() called - stub implementation")
    # TODO: Implement Localpipe send functionality
