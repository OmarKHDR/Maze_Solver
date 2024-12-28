import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
from findMaze import maze_to_array
from mazeSolver import dijkstra
from mazeVisualizer import isTheMazeCorrect, putStartAndEnd, createScreen, quitScreen

array = maze_to_array("../maze2.png").tolist()

screen = createScreen(array, 80)

array = isTheMazeCorrect(screen, array)

startAndEndPoints = putStartAndEnd(screen, array)
start = startAndEndPoints[0][0] * len(array[0]) + startAndEndPoints[0][1]
end = startAndEndPoints[1][0] * len(array[0]) + startAndEndPoints[1][1]
quitScreen()
solution = dijkstra(array, start, end)
positon = 0