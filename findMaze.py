import cv2
import numpy as np

"""this code is supposed to recieve an image of a map and it creates a 2d 
array representaion of the map as open field is 0 and closed field is 1
"""
def image_to_maze(image_path):
	# Load the image
	image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
	
	# Threshold the image to binary
	_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
	
	# Convert binary image to 2D array
	maze = (binary_image == 0).astype(int)
	
	return maze

# Example usage
if __name__ == "__main__":
	image_path = "./maze.jpg"
	maze = image_to_maze(image_path)
	print(maze)