#!/bin/bash
BREW="/usr/local/bin/brew"
PIP="/usr/local/bin/pip3"
RUST_BIN="$HOME/.cargo/bin"

# Add a timestamp to the logfile
echo "------------------------[" $(/bin/date) "]------------------------"

# Update Homebrew package list and upgrade packages that are out of date
echo "Updating Homebrew..."
$BREW update
$BREW upgrade

# Update Vim plugins
echo "Updating vim plugins..."
sh ~/update/update_vim_plugins.sh

# Update pip packages
echo "Updating pip packages..."
$PIP install --upgrade $($PIP list -o --format freeze 2>/dev/null | cut -d= -f1) 2>/dev/null

if [ -x $RUST_BIN ]; then 
    # Update rustc and cargo packages
    echo "Updating rust toolchain..."
    $RUST_BIN/rustup -v update nightly
    echo "Updating cargo packages..."
    $RUST_BIN/cargo install-update --all
fi

# Cleanup
echo "Cleaning up..."
$BREW cleanup

echo "Done!"
