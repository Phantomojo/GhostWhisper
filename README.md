# GhostWhisper

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.11+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

```
  ____ _               _     _       _                 
 / ___| |__   ___  ___| | __| | __ _| |_ ___  _ __ ___ 
| |  _| '_ \ / _ \/ __| |/ _` |/ _` | __/ _ \| '__/ _ \
| |_| | | | |  __/ (__| | (_| | (_| | || (_) | | |  __/
 \____|_| |_|\___|\___|_|\__,_|\__,_|\__\___/|_|  \___|
                                                      
```

Welcome to **GhostWhisper**, the stealthy-yet-flexible modular CLI messaging tool designed for researchers and developers who want full control and traceability over their messaging workflows.

---

## Features

- Modular architecture with pluggable transports (HTTP, SMTP, QR, Localpipe)
- Clean CLI interface with `send` and `listen` commands
- Robust message serialization and deserialization
- Automatic routing with fallback transports for reliability
- Detailed development logging to `ghostwhisper-devlog.txt` for research-grade traceability
- Extensible core for future transport and feature additions
- Thoroughly tested with unit and integration tests

---

## Installation

```bash
pip install -e .
```

Make sure you have Python 3.11+ installed.

---

## Usage

```bash
ghostwhisper send --to http://localhost --via http --message "Hello, world!"
ghostwhisper listen --via http
```

*Note:* The `listen` command is currently a stub and will be fully implemented in upcoming phases.

---

## Roadmap

- Phase 2: FastAPI-based receiver and full listen mode implementation
- Add real SMTP, QR code, and localpipe transports
- Key management and encryption support
- Enhanced logging and analytics
- GUI and WSL compatibility checks

---

## Contributing

Contributions are welcome! Please fork the repo and submit pull requests. For major changes, open an issue first to discuss your ideas.

---

## Logging & Debugging

All actions, errors, and decisions are logged in `ghostwhisper-devlog.txt`. It’s like having a research assistant who never forgets — and never sleeps. If you find yourself lost, check the log!

---

## License

MIT License © 2025 GhostWhisper Contributors

---

*Keep whispering, keep coding.* 🚀
