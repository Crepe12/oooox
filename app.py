from flask import Flask, render_template
from flask_socketio import SocketIO
import os

app = Flask(__name__)
socketio = SocketIO(app, async_mode="eventlet")  # ระบุ eventlet ตรงนี้

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    socketio.run(app, host="0.0.0.0", port=port)
