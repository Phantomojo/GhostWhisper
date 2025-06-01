import json
from datetime import datetime
import os

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ghostwhisper-devlog.txt')

def log_devlog(entry: str):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {entry}\n")

class Message:
    def __init__(self, sender: str, receiver: str, content: str, timestamp: str | None = None):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = timestamp or datetime.utcnow().isoformat()
        log_devlog(f"[INFO] Created Message object with sender={sender}, receiver={receiver}")


    def serialize(self) -> str:
        data = {
            'sender': self.sender,
            'receiver': self.receiver,
            'content': self.content,
            'timestamp': self.timestamp,
        }
        serialized = json.dumps(data)
        log_devlog(f"[INFO] Serialized Message object to JSON")
        return serialized

    @staticmethod
    def deserialize(json_str: str) -> 'Message':
        data = json.loads(json_str)
        msg = Message(
            sender=data['sender'],
            receiver=data['receiver'],
            content=data['content'],
            timestamp=data['timestamp']
        )
        log_devlog(f"[INFO] Deserialized JSON to Message object with sender={msg.sender}, receiver={msg.receiver}")
        return msg
