#!/bin/sh
python3 "$HOME"/update/fetch_prices.py > /tmp/runescape.log

# Terminal notification
wall < /tmp/runescape.log
