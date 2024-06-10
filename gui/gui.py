from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'temp_string'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('send_message')
def handle_send_message(data):
    user_message = data['message']

response = requests.post("http://0.0.0.0:8000/question", json={"query": user_message})

    response_data = response.json()
    query_content = response_data.get('query', {}).get('content', '')

    print (query_content)
    bot_response = query_content
    emit('receive_message', {'message': bot_response})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=15000)
