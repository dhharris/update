#!/bin/bash
BREW="/usr/local/bin/brew"
PIP_REVIEW="/usr/local/bin/pip-review"
PIP="/usr/local/bin/pip"
RUST_BIN="$HOME/.cargo/bin"

# Add a timestamp to the logfile
echo "------------------------[" $(/bin/date) "]------------------------"

# Update Homebrew package list and upgrade packages that are out of date
echo "Updating Homebrew..."
$BREW update
$BREW upgrade

# Update Vim plugins
echo "Updating vim plugins..."
sh ~/Scripts/update/update_vim_plugins.sh

# Update pip
echo "Updating pip..."
$PIP install --upgrade pip

# Update pip packages
echo "Updating pip packages..."
$PIP_REVIEW --auto

# Update rustc and cargo packages
echo "Updating rust toolchain..."
$RUST_BIN/rustup -v update nightly

echo "Updating cargo packages..."
$RUST_BIN/cargo install-update --all

# Cleanup
echo "Cleaning up..."
$BREW cleanup

echo "Done!"
