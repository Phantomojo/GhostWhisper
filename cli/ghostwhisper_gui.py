[{
	"resource": "/home/mikey/GhostWhisper/cli/ghostwhisper_gui.py",
	"owner": "pylance",
	"code": {
		"value": "reportAttributeAccessIssue",
		"target": {
			"$mid": 1,
			"path": "/microsoft/pylance-release/blob/main/docs/diagnostics/reportAttributeAccessIssue.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 8,
	"message": "Cannot assign to attribute \"container\" for class \"Layout\"\n  Expression of type \"TextArea\" cannot be assigned to attribute \"container\" of class \"Layout\"\n    \"TextArea\" is not assignable to \"Container\"",
	"source": "Pylance",
	"startLineNumber": 291,
	"startColumn": 33,
	"endLineNumber": 291,
	"endColumn": 42
},{
	"resource": "/home/mikey/GhostWhisper/cli/ghostwhisper_gui.py",
	"owner": "pylance",
	"code": {
		"value": "reportAttributeAccessIssue",
		"target": {
			"$mid": 1,
			"path": "/microsoft/pylance-release/blob/main/docs/diagnostics/reportAttributeAccessIssue.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 8,
	"message": "Cannot assign to attribute \"container\" for class \"Layout\"\n  Expression of type \"TextArea\" cannot be assigned to attribute \"container\" of class \"Layout\"\n    \"TextArea\" is not assignable to \"Container\"",
	"source": "Pylance",
	"startLineNumber": 293,
	"startColumn": 33,
	"endLineNumber": 293,
	"endColumn": 42
},{
	"resource": "/home/mikey/GhostWhisper/cli/ghostwhisper_gui.py",
	"owner": "pylance",
	"code": {
		"value": "reportAttributeAccessIssue",
		"target": {
			"$mid": 1,
			"path": "/microsoft/pylance-release/blob/main/docs/diagnostics/reportAttributeAccessIssue.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 8,
	"message": "Cannot assign to attribute \"container\" for class \"Layout\"\n  Expression of type \"TextArea\" cannot be assigned to attribute \"container\" of class \"Layout\"\n    \"TextArea\" is not assignable to \"Container\"",
	"source": "Pylance",
	"startLineNumber": 296,
	"startColumn": 33,
	"endLineNumber": 296,
	"endColumn": 42
},{
	"resource": "/home/mikey/GhostWhisper/cli/ghostwhisper_gui.py",
	"owner": "pylance",
	"code": {
		"value": "reportAttributeAccessIssue",
		"target": {
			"$mid": 1,
			"path": "/microsoft/pylance-release/blob/main/docs/diagnostics/reportAttributeAccessIssue.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 8,
	"message": "Cannot assign to attribute \"container\" for class \"Layout\"\n  Expression of type \"TextArea\" cannot be assigned to attribute \"container\" of class \"Layout\"\n    \"TextArea\" is not assignable to \"Container\"",
	"source": "Pylance",
	"startLineNumber": 298,
	"startColumn": 33,
	"endLineNumber": 298,
	"endColumn": 42
},{
	"resource": "/home/mikey/GhostWhisper/cli/ghostwhisper_gui.py",
	"owner": "pylance",
	"code": {
		"value": "reportAttributeAccessIssue",
		"target": {
			"$mid": 1,
			"path": "/microsoft/pylance-release/blob/main/docs/diagnostics/reportAttributeAccessIssue.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 8,
	"message": "Cannot access attribute \"from_plain_text\" for class \"type[Document]\"\n  Attribute \"from_plain_text\" is unknown",
	"source": "Pylance",
	"startLineNumber": 356,
	"startColumn": 52,
	"endLineNumber": 356,
	"endColumn": 67
},{
	"resource": "/home/mikey/GhostWhisper/cli/ghostwhisper_gui.py",
	"owner": "pylance",
	"code": {
		"value": "reportAttributeAccessIssue",
		"target": {
			"$mid": 1,
			"path": "/microsoft/pylance-release/blob/main/docs/diagnostics/reportAttributeAccessIssue.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 8,
	"message": "Cannot assign to attribute \"targets\" for class \"Completer\"\n  Attribute \"targets\" is unknown",
	"source": "Pylance",
	"startLineNumber": 370,
	"startColumn": 46,
	"endLineNumber": 370,
	"endColumn": 53
# Removed duplicate import statement causing SyntaxError
import json
import os
from pathlib import Path
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, HSplit, VSplit, Window, ConditionalContainer, FloatContainer, Float
from prompt_toolkit.widgets import Frame, TextArea, Label, Box
from prompt_toolkit.styles import Style
from prompt_toolkit.filters import Condition
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.dimension import D
from prompt_toolkit.layout.margins import ScrollbarMargin
from prompt_toolkit.layout.containers import DynamicContainer, Window, VSplit, HSplit, Container
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.layout.processors import Processor, Transformation
from prompt_toolkit.layout.controls import UIContent, UIControl
from prompt_toolkit.data_structures import Point
from prompt_toolkit.output.color_depth import ColorDepth
from core.discovery import DiscoveryServer, discover_peers
from core.message import Message
from core.router import route_message
from datetime import datetime
import threading

CONFIG_PATH = Path.home() / ".ghostverse_state.json"

# Persona themes with cyberpunk colors and fonts
THEMES = {
    "stealth-watcher": Style.from_dict({
        "header": "bg:#000000 #00ff00 bold",
        "footer": "bg:#000000 #00ff00",
        "sidebar": "bg:#003300 #00ff00",
        "main": "bg:#001100 #00ff00",
        "title": "bold underline",
        "keybind": "bg:#000000 #00ff00",
        "chat.sent": "bg:#004400 #ccffcc",
        "chat.received": "bg:#002200 #99cc99",
        "chat.bubble.sent": "bg:#006600 #ccffcc",
        "chat.bubble.received": "bg:#004400 #99cc99",
        "chat.timestamp": "italic #00ff00",
    }),
    "encrypted-node": Style.from_dict({
        "header": "bg:#1a001a #ff00ff bold",
        "footer": "bg:#1a001a #ff00ff",
        "sidebar": "bg:#330033 #ff00ff",
        "main": "bg:#1a001a #ff00ff",
        "title": "bold underline",
        "keybind": "bg:#1a001a #ff00ff",
        "chat.sent": "bg:#660066 #ff99ff",
        "chat.received": "bg:#330033 #cc66cc",
        "chat.bubble.sent": "bg:#990099 #ffccff",
        "chat.bubble.received": "bg:#660066 #cc99cc",
        "chat.timestamp": "italic #ff00ff",
    }),
    "command-hub": Style.from_dict({
        "header": "bg:#000040 #ffffff bold",
        "footer": "bg:#000040 #ffffff",
        "sidebar": "bg:#000060 #ffffff",
        "main": "bg:#000020 #ffffff",
        "title": "bold underline",
        "keybind": "bg:#000040 #ffffff",
        "chat.sent": "bg:#000080 #ccccff",
        "chat.received": "bg:#000040 #9999cc",
        "chat.bubble.sent": "bg:#0000cc #ccccff",
        "chat.bubble.received": "bg:#000080 #9999cc",
        "chat.timestamp": "italic #ccccff",
    }),
}

DEFAULT_PERSONA = "stealth-watcher"

class ChatMessage:
    def __init__(self, sender, content, timestamp=None, sent=True):
        self.sender = sender
        self.content = content
        self.timestamp = timestamp or datetime.utcnow().strftime("%H:%M:%S")
        self.sent = sent

    def format_message(self):
        # Format message with sender, timestamp, and content
        header = f"{self.sender} [{self.timestamp}]"
        return f"{header}\n{self.content}"

class CommandCompleter(Completer):
    def __init__(self, commands, targets):
        super().__init__()
        self.commands = commands
        self._targets = targets

    @property
    def targets(self):
        return self._targets

    @targets.setter
    def targets(self, value):
        self._targets = value

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor.lstrip()
        words = text.split()
        if not words:
            for cmd in self.commands:
                if cmd.startswith(text):
                    yield Completion(cmd, start_position=-len(text))
        elif len(words) == 1:
            cmd = words[0]
            if cmd in ["send", "sendauto", "clients", "discover", "help", "exit"]:
                if cmd in ["send", "sendauto"]:
                    for target in self._targets:
                        if target.startswith(document.get_word_before_cursor()):
                            yield Completion(target, start_position=-len(document.get_word_before_cursor()))
                else:
                    # No further completions
                    return
            else:
                for cmd in self.commands:
                    if cmd.startswith(cmd):
                        yield Completion(cmd, start_position=-len(cmd))

class GhostWhisperGUI:
    def __init__(self):
        self.running = True
        self.discovery_server = None
        self.discovered_clients = {}
        self.chat_messages = []  # List of ChatMessage
        self.input_buffer = ""
        self.selected_panel = "chat"  # chat, devices
        self.sidebar_collapsed = False
        self.persona = DEFAULT_PERSONA
        self.mission_mode = "stealth"
        self.state = {}
        self.load_state()

        self.kb = KeyBindings()
        self._bind_keys()

        self.header = Window(
            height=3,
            content=FormattedTextControl(text=self.get_header_text),
            style="class:header",
            always_hide_cursor=True,
        )
        self.footer = Window(
            height=2,
            content=FormattedTextControl(text=self.get_footer_text),
            style="class:footer",
            always_hide_cursor=True,
        )
        self.chat_panel = TextArea(
            text="Welcome to GhostWhisper Chat\n",
            scrollbar=True,
            line_numbers=False,
            style="class:main",
            focusable=True,
            wrap_lines=True,
            read_only=True,
        )
        self.devices_panel = TextArea(
            text="Device Scan: No devices yet.\n",
            scrollbar=True,
            line_numbers=False,
            style="class:sidebar",
            focusable=True,
            wrap_lines=True,
            read_only=True,
            width=40,
        )

        self.command_input = TextArea(
            height=3,
            prompt="> ",
            style="class:main",
            multiline=False,
            wrap_lines=False,
            accept_handler=self.handle_command_wrapper,
            completer=CommandCompleter(
                commands=["help", "discover", "clients", "send", "sendauto", "exit"],
                targets=list(self.discovered_clients.keys()),
            ),
            history=InMemoryHistory(),
        )

        self.body = DynamicContainer(self.get_body_container)

        self.layout = Layout(
            HSplit([
                self.header,
                VSplit([
                    self.body,
                    ConditionalContainer(
                        content=self.devices_panel,
                        filter=Condition(lambda: not self.sidebar_collapsed),
                    ),
                ]),
                self.footer,
                self.command_input,
            ])
        )

        self.application = Application(
            layout=self.layout,
            key_bindings=self.kb,
            style=THEMES[self.persona],
            full_screen=True,
            color_depth=ColorDepth.TRUE_COLOR,
            mouse_support=True,
        )

    def load_state(self):
        if CONFIG_PATH.exists():
            try:
                with open(CONFIG_PATH, "r") as f:
                    self.state = json.load(f)
                    self.persona = self.state.get("persona", DEFAULT_PERSONA)
                    self.mission_mode = self.state.get("mission_mode", "stealth")
                    self.sidebar_collapsed = self.state.get("sidebar_collapsed", False)
            except Exception:
                self.state = {}

    def save_state(self):
        self.state["persona"] = self.persona
        self.state["mission_mode"] = self.mission_mode
        self.state["sidebar_collapsed"] = self.sidebar_collapsed
        try:
            with open(CONFIG_PATH, "w") as f:
                json.dump(self.state, f)
        except Exception:
            pass

    def get_header_text(self):
        title = "GhostWhisper"
        persona_tag = {
            "stealth-watcher": "stealth-watcher",
            "encrypted-node": "encrypted-node",
            "command-hub": "command-hub",
        }.get(self.persona, "unknown")
        return [
            ("class:title", f" {title} "),
            ("", " • "),
            ("class:title", f"{persona_tag} "),
        ]

    def get_footer_text(self):
        keybinds = "Tab: Cycle Panels | z: Zoom Panel | c: Collapse Sidebar | Ctrl-C: Exit"
        mode = f"Mode: {self.mission_mode}"
        trust = "Trust: High"
        return [
            ("class:keybind", keybinds),
            ("", " | "),
            ("class:keybind", mode),
            ("", " | "),
            ("class:keybind", trust),
        ]

    def get_body_container(self):
        if self.selected_panel == "chat":
            return self.chat_panel
        elif self.selected_panel == "devices":
            return self.devices_panel
        else:
            return self.chat_panel

    def _bind_keys(self):
        @self.kb.add("tab")
        def _(event):
            # Cycle focus between chat, devices, and command input
            if self.application.layout.has_focus(self.chat_panel):
                self.selected_panel = "devices"
                event.app.layout.focus(self.devices_panel)
            elif self.application.layout.has_focus(self.devices_panel):
                event.app.layout.focus(self.command_input)
            else:
                self.selected_panel = "chat"
                event.app.layout.focus(self.chat_panel)

        @self.kb.add("c")
        def _(event):
            # Collapse or expand devices panel
            self.sidebar_collapsed = not self.sidebar_collapsed
            self.save_state()

        @self.kb.add("z")
        def _(event):
            # Zoom into the focused panel (toggle fullscreen)
            focused = self.application.layout.current_control
            if focused == self.chat_panel.control:
                if self.layout.container == self.chat_panel:
                    self.layout.container = self.get_body_container()
                else:
                    self.layout.container = self.chat_panel
            elif focused == self.devices_panel.control:
                # Instead of assigning TextArea directly, toggle a ConditionalContainer
                if isinstance(self.layout.container, ConditionalContainer) and self.layout.container.content == self.devices_panel:
                    self.layout.container = self.get_body_container()
                else:
                    self.layout.container = ConditionalContainer(
                        content=self.devices_panel,
                        filter=Condition(lambda: True),
                    )

        @self.kb.add("c-c")
        @self.kb.add("q")
        def _(event):
            # Exit application
            self.running = False
            event.app.exit()

    def handle_command(self, buff):
        text = buff.text.strip()
        if not text:
            return False
        self.log_message(f"> {text}")
        parts = text.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd == "help":
            self.print_help()
        elif cmd == "discover":
            timeout = int(args[0]) if args else 5
            self.discover_clients(timeout)
        elif cmd == "send":
            if len(args) < 3:
                self.log_message("Usage: send <target> <via> <message>")
                return False
            target = args[0]
            via = args[1]
            message = " ".join(args[2:])
            self.send_message(target, via, message)
        elif cmd == "sendauto":
            if len(args) < 1:
                self.log_message("Usage: sendauto <target>")
                return False
            target = args[0]
            self.send_message_auto(target)
        elif cmd == "clients":
            self.show_clients()
        elif cmd == "exit":
            self.running = False
            self.application.exit()
        else:
            self.log_message(f"Unknown command: {cmd}")

    def log_message(self, message, sent=False):
        timestamp = datetime.utcnow().strftime("%H:%M:%S")
        sender = "You" if sent else "Peer"
        chat_msg = ChatMessage(sender, message, timestamp, sent)
        self.chat_messages.append(chat_msg)
        # Format chat messages with bubbles
        formatted = []
        for msg in self.chat_messages[-50:]:
            style = "class:chat.bubble.sent" if msg.sent else "class:chat.bubble.received"
            formatted.append((style, f"{msg.sender} [{msg.timestamp}]\n{msg.content}\n\n"))
        self.chat_panel.text = ""
        # Use Document class directly to create empty document
        from prompt_toolkit.document import Document as PTDocument
        self.chat_panel.buffer.document = PTDocument.from_plain_text("")
        self.chat_panel.buffer.insert_text("".join([text for style, text in formatted]))

    def discover_clients(self, timeout=5):
        self.log_message(f"Discovering clients for {timeout} seconds...")
        clients = discover_peers(timeout=timeout)
        self.discovered_clients = clients
        if clients:
            self.log_message("Discovered clients with transports:")
            for client, transports in clients.items():
                self.log_message(f" - {client} (transports: {', '.join(transports)})")
            self.update_devices_panel()
            # Update completer targets
            if self.command_input.completer and hasattr(self.command_input.completer, 'targets'):
                self.command_input.completer.targets = list(self.discovered_clients.keys())
        else:
            self.log_message("No clients discovered.")
            self.devices_panel.text = "Device Scan: No devices discovered."

    def show_clients(self):
        if self.discovered_clients:
            self.log_message("Discovered clients with transports:")
            for client, transports in self.discovered_clients.items():
                self.log_message(f" - {client} (transports: {', '.join(transports)})")
        else:
            self.log_message("No clients discovered yet.")

    def send_message(self, target, via, message):
        msg = Message(
            sender="user",
            receiver=target,
            content=message,
            timestamp=datetime.utcnow().isoformat(),
        )
        try:
            route_message(msg, via)
            self.log_message(f"Message sent to {target} via {via}.", sent=True)
        except Exception as e:
            self.log_message(f"Failed to send message: {e}")

    def send_message_auto(self, target):
        if target not in self.discovered_clients:
            self.log_message(f"Unknown target {target}. Please discover clients first.")
            return
        transports = self.discovered_clients[target]
        if not transports:
            self.log_message(f"No transports available for {target}.")
            return
        best_transport = transports[0]
        self.log_message(f"Sending message to {target} via {best_transport}.", sent=True)
        # For demo, just prompt input in terminal (blocking)
        message = input(f"Enter message to send to {target} via {best_transport}: ")
        self.send_message(target, best_transport, message)

    def update_devices_panel(self):
        if self.sidebar_collapsed:
            return
        if not self.discovered_clients:
            self.devices_panel.text = "Device Scan: No devices discovered."
            return
        lines = ["Discovered Devices:"]
        for client, transports in self.discovered_clients.items():
            lines.append(f" - {client} (transports: {', '.join(transports)})")
        self.devices_panel.text = "\n".join(lines)

    def print_help(self):
        help_text = [
            "Commands:",
            "  help                 Show this help message",
            "  discover [timeout]   Discover clients on the network",
            "  clients              Show discovered clients with transports",
            "  send <target> <via> <message>  Send a message",
            "  sendauto <target>    Send message to target using best transport",
            "  exit                 Exit the GUI",
        ]
        for line in help_text:
            self.log_message(line)

    def handle_command_wrapper(self, buff):
        # Wrapper to match expected return type for accept_handler
        self.handle_command(buff)
        return True

    def run(self):
        self.discovery_server = DiscoveryServer()
        self.discovery_server.start()
        self.application.run()
        self.discovery_server.stop()

if __name__ == "__main__":
    gui = GhostWhisperGUI()
    gui.run()
