from flask import jsonify, Flask, render_template, request
import os
import sys
import json

app = Flask(__name__)

@app.route('/incrementpos')
def inc():
	pos += 1
	return pos

@app.route('/getmaze')
def getMaze():
	with open(f'{os.path.abspath(os.path.join(os.path.dirname(__file__), "./database/maze.json"))}', 'r') as data:
		maze = json.load(data)
	return jsonify(maze)


@app.route('/solveMaze')
def solver():
	with open(f'{os.path.abspath(os.path.join(os.path.dirname(__file__), "./database/solution.json"))}', 'r') as data:
		solution = json.load(data)
	return jsonify(solution)

@app.route('/setPos')
def setPos():
	pos = request.args.get('pos')
	with  open(f'{os.path.abspath(os.path.join(os.path.dirname(__file__), "./database/pos.txt"))}', 'w') as file:
		file.write(pos)
	return jsonify({'position': pos})

@app.route('/getPos')
def getPos():
	with  open(f'{os.path.abspath(os.path.join(os.path.dirname(__file__), "./database/pos.txt"))}', 'r') as file:
		pos = file.read()
	return str(pos)


@app.route('/')
def home():
	return render_template('index.html')

if __name__ == '__main__':
	app.run('0.0.0.0',port=5000, debug=True)
