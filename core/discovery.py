import socket
import threading
import time

DISCOVERY_PORT = 9999
DISCOVERY_MESSAGE = b"GhostWhisperDiscovery"
# Response now includes supported transports as comma-separated string
RESPONSE_MESSAGE_PREFIX = b"GhostWhisperHere:"
SUPPORTED_TRANSPORTS = "http,smtp,qr,localpipe"
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
                print(f"[DiscoveryServer] Received data from {addr}: {data}")
                if data == DISCOVERY_MESSAGE:
                    response = RESPONSE_MESSAGE_PREFIX + SUPPORTED_TRANSPORTS.encode()
                    print(f"[DiscoveryServer] Responding to discovery request from {addr} with transports: {SUPPORTED_TRANSPORTS}")
                    self.sock.sendto(response, addr)
            except Exception as e:
                print(f"[DiscoveryServer] Exception: {e}")

    def stop(self):
        self.running = False
        self.sock.close()

def discover_peers(timeout=DISCOVERY_TIMEOUT, broadcast_ip="255.255.255.255", port=DISCOVERY_PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print(f"[discover_peers] Sending discovery message to {broadcast_ip}:{port}")
    sock.sendto(DISCOVERY_MESSAGE, (broadcast_ip, port))

    peers = {}
    start_time = time.time()
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(f"[discover_peers] Received response from {addr}: {data}")
            if data.startswith(RESPONSE_MESSAGE_PREFIX):
                transports_str = data[len(RESPONSE_MESSAGE_PREFIX):].decode()
                transports = transports_str.split(",") if transports_str else []
                peers[addr[0]] = transports
        except socket.timeout:
            break
        if time.time() - start_time > timeout:
            break
    sock.close()
    return peers
