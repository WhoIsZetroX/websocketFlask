from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

# The correct way to do this would be using a db but for testing I'll be using a list defined here
# Another way for testing would be defining the topics on a file but i prefered this way
current_topic = 0
topics = ["This is the first topic...", "Improving the code.", "Uploading everything to github."]


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', initial_topic=topics[current_topic], topics=topics)


@app.route('/get_current_topic', methods=['GET'])
def get_current_topic():
    return jsonify({'topic': topics[current_topic]}), 200


@app.route('/next_topic', methods=['GET'])
def next_topic():
    global current_topic
    current_topic = current_topic + 1 if current_topic < len(topics)-1 else 0
    socketio.emit('my_topic', {'topic': topics[current_topic]})
    return 'ok', 200


@app.route('/prev_topic', methods=['GET'])
def previous_topic():
    global current_topic
    current_topic = current_topic - 1 if current_topic > 0 else len(topics)-1
    socketio.emit('my_topic', {'topic': topics[current_topic]})
    return 'ok', 200


if __name__ == '__main__':
    app.run(host=os.getenv("HOSTNAME"), port=os.getenv("PORT"), debug=os.getenv("DEBUG"))
