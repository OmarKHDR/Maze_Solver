#!/usr/bin/env python3
"""dijkstra map solverrrr
solver = {pos : (dist, prev, [next])}
"""
import json

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
	""" if i of past ind == i of current ind pass
	else if past i less current i then instruction is L else inst is R
	then handle rotation
	"""
	path = []
	current = end
	i = 0
	while current is not None and i < len(solver.keys()):
		path.append(current)
		current = solver[current][1]
		i+=1
	path = path[::-1]
	ang_of_rotations = [0]
	instructions = []
	stopPoints = []
	prev = path[0]
	for current in path:
		getDir(prev, current, ang_of_rotations, instructions, width, stopPoints)
		prev = current

	return json.dumps({"path": path[:], "instructions": instructions[:], "stopPoints": stopPoints[:], "instructionString": "".join(instructions)})

def getDir(prev, current, ang_of_rotations, instructions, width,stopPoints):
	prev_i = prev // width
	prev_j = prev % width
	current_i = current // width
	current_j = current % width
	if prev_i == current_i:
		if prev_j > current_j:
			if ang_of_rotations[0] == 1:
				instructions.append("R")
				stopPoints.append(prev)
			elif ang_of_rotations[0] == 3:
				instructions.append("L")
				stopPoints.append(prev)
			ang_of_rotations[0] = 2
		elif prev_j < current_j:
			if ang_of_rotations[0] == 1:
				stopPoints.append(prev)
				instructions.append("L")
			elif ang_of_rotations[0] == 3:
				instructions.append("R")
				stopPoints.append(prev)
			ang_of_rotations[0] = 0
	elif prev_j == current_j:
		if prev_i > current_i:
			if ang_of_rotations[0] == 0:
				instructions.append("L")
				stopPoints.append(prev)
			elif ang_of_rotations[0] == 2:
				instructions.append("R")
				stopPoints.append(prev)
			ang_of_rotations[0] = 3
		elif prev_i < current_i:
			if ang_of_rotations[0] == 0:
				instructions.append("R")
				stopPoints.append(prev)
			elif ang_of_rotations[0] == 2:
				instructions.append("L")
				stopPoints.append(prev)
			ang_of_rotations[0] = 1



if __name__ == '__main__':
	pass