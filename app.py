from flask import Flask, render_template, Response, jsonify
import subprocess
import os
import threading
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game_page():
    return render_template('game.html')

@app.route('/start_magic')
def start_magic():
    try:
        # Run the gamePlay.py script in a separate process
        subprocess.Popen(['python', 'gesture_controller.py'])
        return "Game started!"
    except Exception as e:
        return f"Error: {str(e)}"
    
@app.route('/start_game')
def start_game():
    try:
        # Run the gamePlay.py script in a separate process
        subprocess.Popen(['python', 'gamePlay.py'])
        return "Game started!"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/end_game')
def end_game():
    try:
        # Terminate the gamePlay.py process
        subprocess.Popen(['pkill', '-f', 'gamePlay.py'])
        return "Game stopped!"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/check_game_status')
def check_game_status():
    global game_running
    return jsonify({'status': 'running' if game_running else 'stopped'})

if __name__ == '__main__':
    import eventlet
    eventlet.monkey_patch()
    app.run(host='0.0.0.0', port=5000,debug=True)



