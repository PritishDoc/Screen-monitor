from flask import Flask, Response, jsonify, request
import cv2
import threading
import time
import pyautogui
import os
import base64
import usage_tracker
import capture_screen

app = Flask(__name__)

# Control flag for pausing/resuming screen recording
PAUSED = False

# Toggle pause state
def toggle_pause():
    global PAUSED
    PAUSED = not PAUSED

# Toggle endpoint
@app.route("/toggle", methods=["POST"])
def toggle():
    toggle_pause()
    return jsonify({"paused": PAUSED})

# Video streaming generator
def generate():
    global PAUSED
    while True:
        if not PAUSED:
            screenshot = pyautogui.screenshot()
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            time.sleep(0.5)

# Live video feed route
@app.route("/video_feed")
def video_feed():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Screenshots route
@app.route("/screenshots")
def get_screenshots():
    images = []
    path = "screenshots"
    if not os.path.exists(path):
        os.makedirs(path)
    for filename in os.listdir(path):
        if filename.endswith(".png"):
            with open(os.path.join(path, filename), "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode("utf-8")
                images.append({
                    "filename": filename,
                    "data": f"data:image/png;base64,{b64_string}"
                })
    return jsonify(images)

# App usage statistics route
@app.route("/usage")
def get_usage():
    return jsonify(usage_tracker.get_usage_data())

# Start background threads
def start_background_tasks():
    screenshot_thread = threading.Thread(target=capture_screen.capture_loop)
    usage_thread = threading.Thread(target=usage_tracker.track_usage_loop)
    screenshot_thread.daemon = True
    usage_thread.daemon = True
    screenshot_thread.start()
    usage_thread.start()

if __name__ == "__main__":
    start_background_tasks()
    app.run(debug=True)
