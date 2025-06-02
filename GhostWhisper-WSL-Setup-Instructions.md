# GhostWhisper Setup Instructions for WSL (Windows Subsystem for Linux)

These instructions will guide you through setting up the GhostWhisper project on a Windows PC using WSL. This will allow you to run the GhostWhisper CLI and backend server in a Linux-like environment compatible with the project.

---

## Prerequisites

- Windows 10 or 11 with WSL installed and a Linux distribution (e.g., Ubuntu) set up.
- Internet connection to download dependencies.
- Python 3.11 or higher installed in WSL.

---

## Step 1: Open WSL Terminal

Open your WSL terminal (e.g., Ubuntu) from the Start menu or Windows Terminal.

---

## Step 2: Update Package Lists and Install Python 3.11

```bash
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3.11-distutils
```

Verify Python version:

```bash
python3.11 --version
```

---

## Step 3: Clone the GhostWhisper Repository

Navigate to your desired directory and clone the repo:

```bash
git clone <repository-url>
cd GhostWhisper
```

Replace `<repository-url>` with the actual URL of the GhostWhisper repository.

---

## Step 4: Create and Activate Python Virtual Environment

```bash
python3.11 -m venv ghostwhisper-env
source ghostwhisper-env/bin/activate
```

---

## Step 5: Upgrade pip and Install Dependencies

```bash
pip install --upgrade pip
pip install -e ".[dev]"
pip install fastapi uvicorn
```

---

## Step 6: Fix PATH for CLI Command (Optional)

If the `ghostwhisper` command is not found, run:

```bash
./fix_path_and_reload.sh
```

Then restart your terminal or source your shell config.

---

## Step 7: Verify Installation

Check if the CLI is available:

```bash
ghostwhisper --help
```

---

## Step 8: Run the Listener Server

Start the FastAPI listener on port 8000:

```bash
ghostwhisper listen --port 8000
```

---

## Step 9: Send a Test Message from Another Terminal or PC

```bash
ghostwhisper send --to http://<listener-ip>:8000/receive --via http --message "Hello from another PC"
```

Replace `<listener-ip>` with the IP address of the PC running the listener.

---

## Notes

- Ensure both PCs are on the same network and can reach each other on the specified port.
- Adjust firewall settings if necessary to allow traffic on port 8000.
- Use `Ctrl+C` to stop the listener server.

---

If you need further assistance or encounter issues, feel free to ask.
