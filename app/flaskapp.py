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
# curl -H "ngrok-skip-browser-warning: 6954O" https://fa50-196-159-5-64.ngrok-free.app/solveMaze	

@app.route('/getInstructions')
def instructions():
	with open(f'{os.path.abspath(os.path.join(os.path.dirname(__file__), "./database/solution.json"))}', 'r') as data:
		solution_str = data.read()
		solution_str = json.loads(solution_str)
		solution = json.loads(solution_str)  # Convert JSON string to Python object
	instructions_list = solution.get('instructionString', [])
	return instructions_list

@app.route('/')
def home():
	return render_template('index.html')

if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] != '':
		port = sys.argv[1]
	else:
		port = 5000
	app.run('0.0.0.0',port= port, debug=True)
