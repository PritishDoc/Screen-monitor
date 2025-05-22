# Add global state to pause/resume
PAUSED = False

def toggle_pause():
    global PAUSED
    PAUSED = not PAUSED

def capture_screen():
    if not PAUSED:
        image = pyautogui.screenshot()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        image.save(f'screenshots/screenshot_{timestamp}.png')
