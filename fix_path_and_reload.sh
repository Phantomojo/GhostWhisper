#!/bin/bash

# Helper script to add ~/.local/bin to PATH if missing, reload shell config, and inform user
# Enhanced to update both ~/.zshrc and ~/.bashrc to avoid PATH issues in common shells

LOCAL_BIN="$HOME/.local/bin"

update_path_in_file() {
    local config_file="$1"
    if [ -w "$config_file" ]; then
        if grep -Fxq "export PATH=\"$LOCAL_BIN:\$PATH\"" "$config_file"; then
            echo "PATH export line already present in $config_file"
        else
            echo "Adding ~/.local/bin to PATH in $config_file"
            echo "" >> "$config_file"
            echo "# Added by GhostWhisper helper script to fix PATH for CLI" >> "$config_file"
            echo "export PATH=\"$LOCAL_BIN:\$PATH\"" >> "$config_file"
        fi
    else
        echo "WARNING: Cannot write to $config_file. Please add ~/.local/bin to your PATH manually."
    fi
}

echo "Updating PATH in shell config files..."

update_path_in_file "$HOME/.zshrc"
update_path_in_file "$HOME/.bashrc"

# Reload current shell config based on current shell
if [ -n "$ZSH_VERSION" ]; then
    echo "Reloading ~/.zshrc"
    source "$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    echo "Reloading ~/.bashrc"
    source "$HOME/.bashrc"
else
    echo "Unknown shell, please reload your shell manually."
fi

echo "PATH updated and shell config reloaded where possible."

echo ""
echo "Note: pip 25.3 will deprecate legacy editable installs."
echo "Consider adding a pyproject.toml or using --use-pep517 with setuptools >= 64."
echo "See https://github.com/pypa/pip/issues/11457 for details."

echo ""
echo "Please try running the 'ghostwhisper' CLI command again now."
