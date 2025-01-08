import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
from findMaze import maze_to_array
from mazeSolver import dijkstra
from mazeVisualizer import isTheMazeCorrect, putStartAndEnd, createScreen, quitScreen

if len(sys.argv) > 1 and sys.argv[1] != '':
	image_name = sys.argv[1]
else:
	image_name = "./maze2.png"
array = maze_to_array(image_name).tolist()

screen = createScreen(array, 40)

array = isTheMazeCorrect(screen, array)
if array != None:
	with open(f'{os.path.abspath(os.path.join(os.path.dirname(__file__), "./database/maze.json"))}', 'w') as file:
		json.dump(array, file)

	startAndEndPoints = putStartAndEnd(screen, array)

	start = startAndEndPoints[0][0] * len(array[0]) + startAndEndPoints[0][1]

	end = startAndEndPoints[1][0] * len(array[0]) + startAndEndPoints[1][1]

	quitScreen()

	solution = dijkstra(array, start, end)

	with open(f'{os.path.abspath(os.path.join(os.path.dirname(__file__), "./database/solution.json"))}', 'w') as file:
		json.dump(solution, file)
