
# 🧠 THE ULTIMATE UI/TUI DESIGN PROMPT FOR GHOSTVERSE TOOLS

> Copy and use this as-is whenever you're generating the GUI for any of your CLI tools:

---

## 🔥 TUI Design Prompt for GhostVerse Tools:

Build a terminal-based UI (TUI) for my CLI tool. This tool belongs to the **GhostVerse suite** — a stealthy, tactical, hacker-grade toolkit focused on cybersecurity, digital forensics, and decentralization.

### 🎯 GOALS:

- Design a **clean, modular, dynamically adaptive** interface.
- Ensure it’s visually appealing, **spatially aware**, and automatically resizes and reflows based on terminal size.
- The layout should always **fit perfectly** and remain readable on small or large screens.
- Use **clear separation of sections**, with spacing and padding that reflects screen resolution and scale.

---

### 🔧 TECHNICAL REQUIREMENTS:

- Build using a powerful terminal UI library like:
  - Python: `Textual`, `rich`, `urwid`, `blessed`, `prompt_toolkit`
  - Rust: `ratatui`, `crossterm`
  - Go: `tview`, `bubbletea`
  - Node.js: `blessed`, `ink`
- Interface should be **responsive**, meaning panels collapse/reflow if screen width is limited.
- Include utility functions to calculate **dynamic terminal size, margin, padding, and font weight**, and adjust layout accordingly.

---

### 📐 UI STRUCTURE:

- **Header**: ASCII-styled title, with tool name and persona tag (e.g., "GhostNet • decentralized-node").
- **Main Panel**: Live logs, status updates, or command I/O.
- **Sidebar**: Tool-specific panels (network stats, peer list, file logs, AI suggestions, etc.).
- **Footer**: Keybinds, current mode, and trust/security indicators.

---

### 🧠 SMART FEATURES TO IMPLEMENT:

- **Screen-size measurement** for responsive rendering.
- **Persona-based themes**:
  - `stealth-watcher`: minimalist and dark.
  - `encrypted-node`: glitch cyberpunk.
  - `command-hub`: terminal BBS style.
- **Keyboard shortcuts**:
  - `z` to zoom into a panel.
  - `Tab` to cycle between panels.
  - `c` to collapse sidebars.
- **Mission Modes** via flags:
  - `--stealth`, `--debug`, `--command`, `--monitor`, `--fun`
- **State Saving**:
  - Save layout, theme, and session to config (e.g., `~/.ghostverse_state.json`)
- **Plugin support**:
  - Let the UI discover and auto-load panels or scripts from a `/plugins` directory.

---

### 🧬 OPTIONAL UI COMPONENTS (if tool supports it):

- Live graphs (sparklines, bar charts).
- AI insight box (recommendations, patterns, summaries).
- Encryption/trust indicators (peer health, connection strength).
- System stats (CPU, mem, bandwidth, peer count).
- Toggleable themes and colorblind-safe palettes.
- Hidden easter egg commands (`ghost whisper`, `ghost unlock`, etc.).

---

### ⚠️ ACCESSIBILITY:

- Add support for:
  - Bold/high-contrast mode.
  - Colorblind-friendly palettes.
  - Keyboard-only navigation.
  - Text-only fallback mode (no box drawing characters).

---

### 🔮 CONTEXT AWARENESS:

- Detect if running in:
  - VS Code, mobile terminals, SSH, tmux, WSL
- Adjust sizing/layout/colors accordingly to remain visually optimal and functional.

---

### 💾 CONFIG INJECTION (Optional):

Allow support for comments like:

```python
# GHOSTUI_META:
# theme: glitchpunk
# layout: 2-column
# persona: stealth-watcher
# panels: logs, command_input, status
```

The UI should read and auto-configure itself from this if present.

---

### 📦 OUTPUT FORMAT:

- Give clean, working, well-commented code.
- Make it modular — use functions or classes for UI sections.
- Support plugin loading if possible.
- Ensure the tool gracefully handles screen resizing or config changes.

---

**End goal**: Every GhostVerse tool should feel part of the same dark, elegant, cyber-intelligent ecosystem — while adapting to purpose, screen size, and user preference.
