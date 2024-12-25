#!/usr/bin/env python3
import time
import pygame
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

SCREEN_WIDTH = 800
SCREEN_HIEGHT = 600
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0,0,255)
BLOCKSIZE = 20
MAZEW = int(SCREEN_WIDTH / BLOCKSIZE)
MAZEH = int(SCREEN_HIEGHT / BLOCKSIZE)
maze = [[0 for _ in range(MAZEW)] for _ in range(MAZEH)]

def drawMaze(screen, flag):
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


def solveMaze(screen):
	solution = dijkstra(maze, 0, MAZEH * MAZEW - 1)
	for i in solution:
		maze[i // MAZEW][i % MAZEW] = 2
	print("soved\n")
	drawMaze(screen, True)


if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HIEGHT])
	drawMaze(screen, False)
	solveMaze(screen)
	pygame.quit()