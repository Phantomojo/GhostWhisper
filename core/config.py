import os
import json
from datetime import datetime

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ghostwhisper-devlog.txt')

def log_devlog(entry: str):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {entry}\n")

class Config:
    PROFILES_PATH = os.path.expanduser('~/.ghostwhisper/profiles.json')

    def __init__(self):
        self.profiles = {}
        self._load_profiles()
        log_devlog(f"[INFO] Initialized Config and loaded profiles from {self.PROFILES_PATH}")

    def _load_profiles(self):
        if os.path.exists(self.PROFILES_PATH):
            try:
                with open(self.PROFILES_PATH, 'r', encoding='utf-8') as f:
                    self.profiles = json.load(f)
                log_devlog(f"[INFO] Loaded profiles from {self.PROFILES_PATH}")
            except Exception as e:
                log_devlog(f"[ERROR] Failed to load profiles: {e}")
                self.profiles = {}
        else:
            log_devlog(f"[INFO] Profiles file {self.PROFILES_PATH} does not exist, starting with empty profiles")

    def save_profiles(self):
        os.makedirs(os.path.dirname(self.PROFILES_PATH), exist_ok=True)
        try:
            with open(self.PROFILES_PATH, 'w', encoding='utf-8') as f:
                json.dump(self.profiles, f, indent=2)
            log_devlog(f"[INFO] Saved profiles to {self.PROFILES_PATH}")
        except Exception as e:
            log_devlog(f"[ERROR] Failed to save profiles: {e}")

    # Stub for key management
    def add_key(self, profile_name: str, key_data: str):
        log_devlog(f"[INFO] Stub: add_key called for profile {profile_name}")
        # TODO: Implement key management
