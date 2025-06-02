# GhostWhisper

<p align="center">
  <img src="https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif" alt="GhostWhisper Animation" width="300"/>
</p>

A stealthy-yet-flexible messaging CLI tool designed for modularity, extensibility, and research-grade logging.

---

## 🚀 Features

- Modular architecture with `cli/`, `core/`, `transports/`, and `tests/` directories.
- CLI implemented with `argparse` supporting `send` and `listen` commands.
- Core modules for `Message` object, routing, and configuration.
- HTTP transport implemented with retry and logging.
- Comprehensive logging to `ghostwhisper-devlog.txt` for all actions.
- Unit and integration tests covering message serialization, transport, routing, and CLI.
- FastAPI backend server with async message handling and CORS support.
- Automatic client discovery with transport detection.
- Interactive CLI GUI with chat window and transport selection.

---

## 📦 Installation & Setup

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

## 💬 Usage

### Sending a Message

```bash
ghostwhisper send --to http://localhost:8000/receive --via http --message "Hello World"
```

Or use the interactive CLI GUI:

```bash
PYTHONPATH=. python cli/ghostwhisper_gui.py
```

Type `help` for commands, `discover` to find clients, and `sendauto <target>` to send messages using the best transport.

### Listening for Messages

```bash
ghostwhisper listen --port 8000
```

- The listener starts a FastAPI server on the specified port.
- Incoming messages are displayed live and saved to `received_messages.log`.
- Logs of all actions are in `ghostwhisper-devlog.txt`.

---

## 🧪 Development & Testing

- Run all tests with:

```bash
python -m unittest discover tests
```

- Tests cover core message handling, transports, CLI commands, backend API, and integration flows.

---

## 🛠 Troubleshooting

- If `ghostwhisper` command is not found, ensure `~/.local/bin` is in your PATH.
- Use `fix_path_and_reload.sh` to add it for bash or zsh shells.
- Restart your terminal or source your shell config after changes.

---

## 🤝 Contributing

- Fork the repo and create feature branches.
- Write tests for new features or bug fixes.
- Submit pull requests with clear descriptions.

---

## 🔒 Security

We continuously review and improve security. Please report any issues via GitHub.

---

## 🎨 Visual

Enjoy the animated mascot:

<p align="center">
  <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" alt="Ghost Animation" width="200"/>
</p>

---

## 📄 License

MIT License
