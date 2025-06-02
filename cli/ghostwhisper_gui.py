import threading
import time
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from core.discovery import DiscoveryServer, discover_peers
from core.message import Message
from core.router import route_message
from datetime import datetime
import subprocess
import sys

class GhostWhisperCLI:
    def __init__(self):
        self.listener_process = None
        self.discovery_server = None
        self.session = PromptSession()
        self.running = True
        self.discovered_clients = []

    def start_listener(self, port=8000):
        if self.listener_process is None:
            self.discovery_server = DiscoveryServer()
            self.discovery_server.start()
            self.listener_process = subprocess.Popen([
                sys.executable, "-m", "uvicorn", "src.backend.app:app",
                "--host", "0.0.0.0",
                "--port", str(port),
                "--log-level", "info"
            ])
            print(f"Listener started on port {port} with discovery server.")

    def stop_listener(self):
        if self.listener_process:
            self.listener_process.terminate()
            self.listener_process.wait()
            self.listener_process = None
        if self.discovery_server:
            self.discovery_server.stop()
            self.discovery_server = None
        print("Listener and discovery server stopped.")

    def discover_clients(self, timeout=5):
        print(f"Discovering clients for {timeout} seconds...")
        self.discovered_clients = discover_peers(timeout=timeout)
        if self.discovered_clients:
            print("Discovered clients with transports:")
            for client, transports in self.discovered_clients.items():
                print(f" - {client} (transports: {', '.join(transports)})")
        else:
            print("No clients discovered.")

    def send_message(self, target, via, message):
        msg = Message(
            sender='user',
            receiver=target,
            content=message,
            timestamp=datetime.utcnow().isoformat()
        )
        try:
            route_message(msg, via)
            print(f"Message sent to {target} via {via}.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    def send_message_auto(self, target):
        if target not in self.discovered_clients:
            print(f"Unknown target {target}. Please discover clients first.")
            return
        transports = self.discovered_clients[target]
        if not transports:
            print(f"No transports available for {target}.")
            return
        # Select best transport (first in list)
        best_transport = transports[0]
        message = input(f"Enter message to send to {target} via {best_transport}: ")
        self.send_message(target, best_transport, message)

    def run(self):
        self.start_listener()
        print("Welcome to GhostWhisper CLI GUI")
        print("Type 'help' for commands.")
        with patch_stdout():
            while self.running:
                try:
                    text = self.session.prompt("> ")
                    self.handle_command(text.strip())
                except (KeyboardInterrupt, EOFError):
                    self.running = False
        self.stop_listener()

    def handle_command(self, command_line):
        if not command_line:
            return
        parts = command_line.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd == "help":
            self.print_help()
        elif cmd == "discover":
            timeout = int(args[0]) if args else 5
            self.discover_clients(timeout)
        elif cmd == "send":
            if len(args) < 3:
                print("Usage: send <target> <via> <message>")
                return
            target = args[0]
            via = args[1]
            message = " ".join(args[2:])
            self.send_message(target, via, message)
        elif cmd == "sendauto":
            if len(args) < 1:
                print("Usage: sendauto <target>")
                return
            target = args[0]
            self.send_message_auto(target)
        elif cmd == "clients":
            if self.discovered_clients:
                print("Discovered clients with transports:")
                for client, transports in self.discovered_clients.items():
                    print(f" - {client} (transports: {', '.join(transports)})")
            else:
                print("No clients discovered yet.")
        elif cmd == "exit":
            self.running = False
        else:
            print(f"Unknown command: {cmd}")


    def print_help(self):
        print("Commands:")
        print("  help                 Show this help message")
        print("  discover [timeout]   Discover clients on the network")
        print("  clients              Show discovered clients with transports")
        print("  send <target> <via> <message>  Send a message")
        print("  sendauto <target>    Send message to target using best transport")
        print("  exit                 Exit the CLI GUI")

if __name__ == "__main__":
    gui = GhostWhisperCLI()
    gui.run()
