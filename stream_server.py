# stream_server.py
from flask import Flask, Response
import cv2
import numpy as np
import pyautogui

app = Flask(__name__)

def gen_frames():
    while True:
        screen = np.array(pyautogui.screenshot())
        frame = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host='0.0.0.0', port=5000)
