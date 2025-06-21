from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, async_mode='eventlet')  # ใช้ eventlet สำหรับ Render

# ตัวแปรเกม
board = [""] * 9
current_player = "X"

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("make_move")
def handle_move(data):
    global board, current_player
    idx = data["index"]
    if board[idx] == "":
        board[idx] = current_player
        emit("update", {"board": board, "player": current_player}, broadcast=True)
        current_player = "O" if current_player == "X" else "X"

# เรียกใช้ PORT จากระบบ Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    socketio.run(app, host="0.0.0.0", port=port)
