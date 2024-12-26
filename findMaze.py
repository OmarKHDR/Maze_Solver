import cv2
import numpy as np
import matplotlib.pyplot as plt

def maze_to_array(image_path):
    """
    Convert a maze image to a 2D binary array with improved wall detection
    0 represents paths (white)
    1 represents walls (black)
    """
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not read the image at {image_path}")
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Increase contrast
    gray = cv2.equalizeHist(gray)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply binary thresholding with Otsu's method
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Enhance edges
    kernel = np.ones((3,3), np.uint8)
    binary = cv2.dilate(binary, kernel, iterations=1)
    binary = cv2.erode(binary, kernel, iterations=1)
    
    # Get image dimensions
    height, width = binary.shape
    grid_size = 20  # Adjust based on maze complexity
    
    # Calculate cell dimensions
    cell_height = height // grid_size
    cell_width = width // grid_size
    
    # Create maze array
    maze_array = np.zeros((grid_size, grid_size), dtype=np.int32)
    
    # More sensitive wall detection with special handling for edges
    for i in range(grid_size):
        for j in range(grid_size):
            # Get region for current cell
            y_start = i * cell_height
            y_end = (i + 1) * cell_height
            x_start = j * cell_width
            x_end = (j + 1) * cell_width
            
            # Get cell region
            cell_region = binary[y_start:y_end, x_start:x_end]
            
            # More sensitive detection for bottom edge
            if i == grid_size - 1:
                threshold = 0.05  # Lower threshold for bottom edge
            else:
                threshold = 0.1   # Normal threshold for other cells
            
            # If any significant amount of black pixels, mark as wall
            if np.sum(cell_region > 0) > (cell_height * cell_width * threshold):
                maze_array[i, j] = 1
    
    # Ensure bottom border is detected
    bottom_strip = binary[-cell_height:]
    if np.sum(bottom_strip > 0) > (bottom_strip.size * 0.05):
        maze_array[-1, :] = 1
    
    return maze_array

def display_processing_steps(image_path, maze_array):
    """Display original, binary, and final maze array"""
    # Read original image
    original = cv2.imread(image_path)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    
    # Process image to show binary step
    gray = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3,3), np.uint8)
    binary = cv2.dilate(binary, kernel, iterations=1)
    binary = cv2.erode(binary, kernel, iterations=1)
    
    # Create figure with three subplots
    plt.figure(figsize=(15, 5))
    
    # Original image
    plt.subplot(1, 3, 1)
    plt.imshow(original)
    plt.title('Original Maze')
    plt.axis('off')
    
    # Binary image
    plt.subplot(1, 3, 2)
    plt.imshow(binary, cmap='gray')
    plt.title('Binary Processing')
    plt.axis('off')
    
    # Final maze array
    plt.subplot(1, 3, 3)
    plt.imshow(maze_array, cmap='binary')
    plt.title('Final Maze Array')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

def main():
    try:
        # Process the maze image
        image_path = 'maze2.png'  # Replace with your image path
        maze_array = maze_to_array(image_path)
        
        print("Maze array shape:", maze_array.shape)
        print("\nMaze array (0 = path, 1 = wall):")
        print(maze_array)
        
        # Display all processing steps
        display_processing_steps(image_path, maze_array)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()