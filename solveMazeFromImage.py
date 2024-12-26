from findMaze import maze_to_array 
from mazeVisualizer import solveMaze
from mazeSolver import dijkstra
import json
import matplotlib.pyplot as plt


array = maze_to_array("maze2.png").tolist()
mazew = len(array[0])
mazeh = len(array)
array[mazeh - 1][mazew -1] = 0
solution = dijkstra(array, 0,  mazew * mazeh -1)
solution = json.loads(solution)
for i in solution["path"]:
	array[i // mazew][i % mazeh] = 2
print("soved\n")
print(solution)

cmap = plt.cm.colors.ListedColormap(['white', 'black', 'blue'])

plt.imshow(array, cmap=cmap)
plt.show()