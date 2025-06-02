import socket
import threading
import time

DISCOVERY_PORT = 9999
DISCOVERY_MESSAGE = b"GhostWhisperDiscovery"
RESPONSE_MESSAGE = b"GhostWhisperHere"
DISCOVERY_TIMEOUT = 5  # seconds

class DiscoveryServer(threading.Thread):
    def __init__(self, listen_ip="0.0.0.0", port=DISCOVERY_PORT):
        super().__init__(daemon=True)
        self.listen_ip = listen_ip
        self.port = port
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.listen_ip, self.port))

    def run(self):
        while self.running:
            try:
                data, addr = self.sock.recvfrom(1024)
                if data == DISCOVERY_MESSAGE:
                    self.sock.sendto(RESPONSE_MESSAGE, addr)
            except Exception:
                pass

    def stop(self):
        self.running = False
        self.sock.close()

def discover_peers(timeout=DISCOVERY_TIMEOUT, broadcast_ip="255.255.255.255", port=DISCOVERY_PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    sock.sendto(DISCOVERY_MESSAGE, (broadcast_ip, port))

    peers = set()
    start_time = time.time()
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            if data == RESPONSE_MESSAGE:
                peers.add(addr[0])
        except socket.timeout:
            break
        if time.time() - start_time > timeout:
            break
    sock.close()
    return list(peers)
