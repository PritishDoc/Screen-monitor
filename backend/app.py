@app.route("/toggle", methods=["POST"])
def toggle():
    toggle_pause()
    return jsonify({"paused": PAUSED})
