# filepath: c:\Users\Dell-saikumar\Desktop\AMIGHO-PROJECT\talking-robot-app\src\app.py
from flask import Flask, render_template
from flask_static_digest import FlaskStaticDigest
from robot.robot import handleCommand
import threading

app = Flask(__name__)
flask_static_digest = FlaskStaticDigest(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_robot():
    threading.Thread(target=handleCommand).start()
    return "Robot started"

if __name__ == "__main__":
    app.run(debug=True)