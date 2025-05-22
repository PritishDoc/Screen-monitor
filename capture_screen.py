# capture_screen.py
import pyautogui
from datetime import datetime

def capture_screen():
    image = pyautogui.screenshot()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    image.save(f'screenshot_{timestamp}.png')
