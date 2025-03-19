from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)

socketio = SocketIO(app)

def ack_client():
    print('client received the emited data')

@app.route('/')
def handle_index():
    return render_template('index.html')

@socketio.on('connect', namespace='/chat')
def handle_connect(auth):
    print(f'client connected to server. Auth data: {auth}')

@socketio.on('message', namespace='/chat')
def handle_chat_message(data):
    print(type(data))
    print(f'data received: {data}')
    username = data['username']
    message = data['message']
    send({'username': username, 'message': message}, namespace='/chat')


if __name__ == '__main__':
    socketio.run(app, debug=True)