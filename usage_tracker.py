import psutil
import time
from collections import defaultdict
import win32gui

usage = defaultdict(int)

def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def track_usage(interval=1):
    while True:
        title = get_active_window_title()
        usage[title] += interval
        time.sleep(interval)
