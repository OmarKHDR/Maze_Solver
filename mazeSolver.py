#!/usr/bin/env python3
"""dijkstra map solverrrr
solver = {pos -> (width of maze * j - (width of maze - i) ): (dist, prev, [next])}
"""
def dijkstra(maze, start, end):
	width = len(maze[0])
	height = len(maze)
	solver = {pos: (float('inf'), None, []) for pos in range(width * height)}
	solver[start] = (0, None, [])
	queue = [start]
	while queue:
		current = queue.pop(0)
		i = current // width
		j = current % width
		for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
			if 0 <= x < height and 0 <= y < width and maze[x][y] == 0:
				pos = width * x + y
				dist = solver[current][0] + 1
				if dist < solver[pos][0]:
					solver[pos] = (dist, current, [])
					queue.append(pos)
				if dist == solver[pos][0]:
					solver[pos][2].append(current)
	path = []
	current = end
	i = 0
	while current is not None and i < len(solver.keys()):
		path.append(current)
		current = solver[current][1]
	return path[::-1]

if __name__ == '__main__':
	pass