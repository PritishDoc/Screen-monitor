# scheduler.py
import schedule
import time
from capture_screen import capture_screen

# Schedule a screenshot every 10 seconds
schedule.every(10).seconds.do(capture_screen)

while True:
    schedule.run_pending()
    time.sleep(1)
