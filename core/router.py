import os
from datetime import datetime
from transports import http
from transports import smtp
from transports import qr
from transports import localpipe
import os
from datetime import datetime

LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'ghostwhisper-devlog.txt')

def log_devlog(entry: str):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {entry}\\n")

def route_message(message, via: str):
    log_devlog(f"[ROUTER] Using '{via}' transport")
    transports_order = ['http', 'smtp', 'qr', 'localpipe']
    if via not in transports_order:
        log_devlog(f"[ERROR] Unknown transport method: {via}")
        raise ValueError(f"Unknown transport method: {via}")

    # Try primary transport, fallback to others if failure
    for transport in [via] + [t for t in transports_order if t != via]:
        try:
            if transport == 'http':
                http.send(message, message.receiver)
            elif transport == 'smtp':
                smtp.send(message, message.receiver)
            elif transport == 'qr':
                qr.send(message, message.receiver)
            elif transport == 'localpipe':
                localpipe.send(message, message.receiver)
            log_devlog(f"[ROUTER] Message sent via {transport} transport")
            return
        except Exception as e:
            log_devlog(f"[ROUTER] Transport {transport} failed with error: {e}")
    log_devlog(f"[ERROR] All transports failed for message to {message.receiver}")
    raise RuntimeError("All transports failed")
