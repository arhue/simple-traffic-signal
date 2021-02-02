#!/bin/bash
terminal_emulator=gnome-terminal
$terminal_emulator -- python3 traffic.py 0
$terminal_emulator -- python3 traffic.py 70
$terminal_emulator -- python3 traffic.py 140
$terminal_emulator -- python3 traffic.py 210
