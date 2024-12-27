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


def drawMaze(screen, maze, flag=False):
	counter = 0
	StoE = (0, len(maze) *len(maze[0]) - 1)
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
				if flag:
					maze[int(pos[1]/BLOCKSIZE)][int(pos[0]/BLOCKSIZE)] = int(not maze[int(pos[1]/BLOCKSIZE)][int(pos[0]/BLOCKSIZE)])
				else:
					if counter >= 2:
						return StoE
					else:
						StoE[counter] = int(pos[1]/BLOCKSIZE), int(pos[0]/BLOCKSIZE)

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
	write_text(screen, "click to toggle wrong walls", (5,5))
	drawMaze(screen, maze)
	return maze

def putStartAndEnd(screen, maze):
	write_text(screen, "click on start and end nodes respectevly", (5,5))
	return drawMaze(screen, maze, True)

def solveMaze(screen, maze,start,end):
	mazew = len(maze[0])
	mazeh = len(maze)
	solution = dijkstra(maze, start, end)
	solution = json.loads(solution)
	for i in solution["path"]:
		maze[i // mazew][i % mazeh] = 2
	print("soved\n")
	print(solution)
	drawMaze(screen)


def createScreen(maze, blockSize =20):
	pygame.init()
	BLOCKSIZE = blockSize
	screen = pygame.display.set_mode([len(maze[0]) * BLOCKSIZE , len(maze) * BLOCKSIZE])
	return screen

def quitScreen():
	pygame.quit()


def write_text(screen, text, position, font_size=30, color=BLACK):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)
    pygame.display.flip()


if __name__ == '__main__':
# Example maze for testing
	maze = [[0, 0, 1, 0],
			[1, 0, 1, 0],
			[0, 0, 0, 0],
			[1, 1, 1, 0]]

	screen = createScreen(maze)
	maze = isTheMazeCorrect(screen, maze)
	start, end = putStartAndEnd(screen, maze)
	print(start, end)
	solveMaze(screen,maze, start, end)
	quitScreen()