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
BLOCKSIZE = 1

maze = [[0 for _ in range(800//20)] for _ in range(600//20)]

def drawMaze(screen):
	while True:
		if not maze:
			return
		for event in pygame.event.get():
			if event.type == QUIT:
				return maze
			if (event.type == KEYDOWN):
				if event.key == K_KP_ENTER:
					return maze

			if event.type == MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				maze[int(pos[1]/BLOCKSIZE)][int(pos[0]/BLOCKSIZE)] = 1
		for i in range(len(maze)):
			for j in range(len(maze[0])):
				if maze[i][j] == 1:
					pygame.draw.rect(screen, BLACK, (j * BLOCKSIZE, i * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
				elif maze[i][j] == 0:
					pygame.draw.rect(screen, WHITE, (j * BLOCKSIZE, i * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
				elif maze[i][j] == 2:
					pygame.draw.rect(screen, BLUE, (j * BLOCKSIZE, i * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
		pygame.display.flip()


def solveMaze(screen, maze):
	mazew = len(maze[0])
	mazeh = len(maze)
	solution = dijkstra(maze, 0,  mazew * mazeh - 21)
	solution = json.loads(solution)
	for i in solution["path"]:
		maze[i // mazew][i % mazeh] = 2
	print("soved\n")
	print(solution)
	drawMaze(screen)


if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode([800, 600])
	drawMaze(screen)
	solveMaze(screen, maze)
	pygame.quit()