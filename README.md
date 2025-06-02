# GhostWhisper

A stealthy-yet-flexible messaging CLI tool designed for modularity, extensibility, and research-grade logging.

---

## Phase 1: Foundational Code

- Modular architecture with `cli/`, `core/`, `transports/`, and `tests/` directories.
- CLI implemented with `argparse` supporting `send` and `listen` commands.
- Core modules for `Message` object, routing, and configuration.
- HTTP transport implemented with retry and logging.
- Comprehensive logging to `ghostwhisper-devlog.txt` for all actions.
- Unit and integration tests covering message serialization, transport, routing, and CLI.

## Phase 2: FastAPI Receiver & Listen Command

- FastAPI backend server in `src/backend/app.py` with `/receive` POST endpoint.
- Async handling of incoming messages with CORS enabled for localhost.
- CLI `listen` command to start FastAPI server on specified port (default 8000).
- Incoming messages streamed live in CLI and saved to `received_messages.log`.
- Graceful shutdown handling and detailed logging of listener events.
- Thorough backend and integration tests for message receiving and CLI listening.

---

## Installation & Setup

1. Clone the repository.

2. Create and activate a Python 3.11+ virtual environment.

3. Install dependencies:

```bash
pip install -e .[dev]
```

4. Ensure `~/.local/bin` is in your PATH. Use the provided helper script `fix_path_and_reload.sh` if needed.

5. Verify CLI installation:

```bash
ghostwhisper --help
```

---

## Usage

### Sending a Message

```bash
ghostwhisper send --to http://localhost:8000/receive --via http --message "Hello World"
```

### Listening for Messages

```bash
ghostwhisper listen --port 8000
```

- The listener starts a FastAPI server on the specified port.
- Incoming messages are displayed live and saved to `received_messages.log`.
- Logs of all actions are in `ghostwhisper-devlog.txt`.

---

## Development & Testing

- Run all tests with:

```bash
python -m unittest discover tests
```

- Tests cover core message handling, transports, CLI commands, backend API, and integration flows.

---

## Troubleshooting

- If `ghostwhisper` command is not found, ensure `~/.local/bin` is in your PATH.
- Use `fix_path_and_reload.sh` to add it for bash or zsh shells.
- Restart your terminal or source your shell config after changes.

---

## Contributing

- Fork the repo and create feature branches.
- Write tests for new features or bug fixes.
- Submit pull requests with clear descriptions.

---

## License

MIT License

---

## Setup Instructions for WSL (Windows Subsystem for Linux)

For setting up GhostWhisper on a Windows PC using WSL, please refer to the detailed instructions in the file [GhostWhisper-WSL-Setup-Instructions.md](./GhostWhisper-WSL-Setup-Instructions.md).

---

## ASCII Art

```
   ____ _               _     _       _                 
  / ___| |__   ___  ___| | __| | __ _| |_ ___  _ __ ___ 
 | |  _| '_ \ / _ \/ __| |/ _` |/ _` | __/ _ \| '__/ _ \\
 | |_| | | | |  __/ (__| | (_| | (_| | || (_) | | |  __/
  \____|_| |_|\___|\___|_|\__,_|\__,_|\__\___/|_|  \___|
