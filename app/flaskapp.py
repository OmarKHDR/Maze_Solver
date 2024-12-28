from flask import jsonify, Flask, render_template

app = Flask(__name__)

@app.route('/incrementpos')
def inc():
	pos += 1
	return pos

@app.route('/getmaze')
def getMaze():
	with open('./database/maze.json') as data:
		maze = data
	return jsonify(maze)


@app.route('/solveMaze')
def solver():
	with open('./database/solution.json') as data:
		solution = data
	return solution


@app.route('/')
def home():
	return render_template('index.html')

if __name__ == '__main__':
	app.run('0.0.0.0',port=5000, debug=True)
