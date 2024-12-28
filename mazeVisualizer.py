#!/usr/bin/env python3
import time
import pygame
import json
dijkstra = __import__('mazeSolver').dijkstra
from pygame.locals import (
	K_RIGHT,
	K_LEFT,
	K_DOWN,
	K_UP,
	K_ESCAPE,
	QUIT,
	KEYDOWN,
	MOUSEBUTTONDOWN,
	K_KP_ENTER
)


WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0,0,255)
BLOCKSIZE = 100


def drawMaze(screen, maze, flag=False):
	counter = 0
	SandE = [(0,0), (len(maze) - 1, len(maze[0]) -1)]
	global BLOCKSIZE
	while True:
		if not maze:
			return
		for event in pygame.event.get():
			if event.type == QUIT and not flag:
				return maze
			if (event.type == KEYDOWN) and not flag:
				if event.key == K_KP_ENTER:
					return maze
			if event.type == pygame.VIDEORESIZE:
				new_block_size_width = event.w // len(maze[0])
				new_block_size_height = event.h // len(maze)
				BLOCKSIZE = min(new_block_size_width, new_block_size_height)
			if event.type == MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if not flag:
					maze[int(pos[1]/BLOCKSIZE)][int(pos[0]/BLOCKSIZE)] = int(not maze[int(pos[1]/BLOCKSIZE)][int(pos[0]/BLOCKSIZE)])
				else:
					if counter >= 2:
						maze[SandE[0][0]][SandE[0][1]] = 0
						maze[SandE[1][0]][SandE[1][1]] = 0
						return SandE
					else:
						SandE[counter] = int(pos[1]/BLOCKSIZE), int(pos[0]/BLOCKSIZE)
						counter += 1
					maze[int(pos[1]/BLOCKSIZE)][int(pos[0]/BLOCKSIZE)] = 2

		for i in range(len(maze)):
			for j in range(len(maze[0])):
				if maze[i][j] == 1:
					pygame.draw.rect(screen, BLACK, (j * BLOCKSIZE, i * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
				elif maze[i][j] == 0:
					pygame.draw.rect(screen, WHITE, (j * BLOCKSIZE, i * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
				elif maze[i][j] == 2:
					pygame.draw.rect(screen, BLUE, (j * BLOCKSIZE, i * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
		pygame.display.flip()

def isTheMazeCorrect(screen, maze):
	pygame.display.set_caption("click to toggle wrong walls")
	drawMaze(screen, maze)
	return maze

def putStartAndEnd(screen, maze):
	pygame.display.set_caption("click on start and end nodes respectevly")
	return drawMaze(screen, maze, True)

def solveMaze(screen, maze,start,end):
	mazew = len(maze[0])
	mazeh = len(maze)
	solution = dijkstra(maze, start, end)
	solution = json.loads(solution)
	print(solution)
	for i in solution["path"]:
		maze[i // mazew][i % mazew] = 2
	print("soved\n")
	print(solution)
	drawMaze(screen, maze)
	return


def createScreen(maze, blockSize =20):
	pygame.init()
	BLOCKSIZE = blockSize
	screen = pygame.display.set_mode([len(maze[0]) * BLOCKSIZE , len(maze) * BLOCKSIZE], pygame.RESIZABLE)
	return screen

def quitScreen():
	pygame.quit()


if __name__ == '__main__':
# Example maze for testing
	maze = [[0, 0, 1],
			[1, 0, 1],
			[0, 0, 0],
			[1, 1, 1]]
	screen = createScreen(maze,100)
	maze = isTheMazeCorrect(screen, maze)
	startAndEndPoints = putStartAndEnd(screen, maze)
	start = startAndEndPoints[0][0] * len(maze[0]) + startAndEndPoints[0][1]
	end = startAndEndPoints[1][0] * len(maze[0]) + startAndEndPoints[1][1]
	print("start is ", start, end)
	solveMaze(screen,maze, start, end)
	quitScreen()