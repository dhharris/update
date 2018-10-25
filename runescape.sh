#!/bin/sh
# Terminal notification
/usr/bin/python /Users/hugh/Scripts/fetch_prices.py | wall

# Write to /tmp/runescape.log
/usr/bin/python /Users/hugh/Scripts/fetch_prices.py > /tmp/runescape.log

