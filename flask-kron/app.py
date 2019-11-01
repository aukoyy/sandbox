from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

notes = ['kjøp stuff til julebord']

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def post_note():
    new_note = request.args.get('new-note')
    notes.append(new_note)
    return 'OK'


app.run()