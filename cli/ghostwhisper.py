import argparse
import sys
import os
from core.router import route_message
from core.message import Message
from datetime import datetime

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ghostwhisper-devlog.txt')

def log_devlog(entry: str):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {entry}\n")

def main():
    log_devlog("[INFO] Created cli/ghostwhisper.py with argparse structure")
    log_devlog("[REASONING] Click not used to minimize dependency tree")

    parser = argparse.ArgumentParser(prog='ghostwhisper', description='GhostWhisper CLI tool')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # send command
    send_parser = subparsers.add_parser('send', help='Send a message')
    send_parser.add_argument('--to', required=True, help='Destination address or identifier')
    send_parser.add_argument('--via', required=True, choices=['http', 'smtp', 'qr', 'localpipe'], help='Transport method')
    send_parser.add_argument('--message', required=True, help='Message content')

    # listen command
    listen_parser = subparsers.add_parser('listen', help='Listen for incoming messages')
    listen_parser.add_argument('--via', required=True, choices=['http', 'smtp', 'qr', 'localpipe'], help='Transport method')

    args = parser.parse_args()

    if args.command == 'send':
        log_devlog(f"[EXECUTION] User ran: ghostwhisper send --to {args.to} --via {args.via} --message \"{args.message}\"")
        message = Message(
            sender='user',  # Placeholder, could be from config in future
            receiver=args.to,
            content=args.message,
            timestamp=datetime.utcnow().isoformat()
        )
        route_message(message, args.via)
    elif args.command == 'listen':
        log_devlog(f"[EXECUTION] User ran: ghostwhisper listen --via {args.via}")
        # For now, listen is stubbed
        log_devlog(f"[ROUTER] Listen mode selected for transport '{args.via}' - stub implementation")
        print(f"Listening on transport '{args.via}' (stub)")

if __name__ == '__main__':
    main()
