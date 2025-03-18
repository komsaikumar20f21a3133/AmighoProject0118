from flask import Flask, render_template
from robot.robot import handleCommand
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_robot():
    threading.Thread(target=handleCommand).start()
    return "Robot started"

if __name__ == "__main__":
    app.run(debug=True)