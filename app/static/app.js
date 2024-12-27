let mazePromise;
let maze;
window.onload = () => {
	fetch('/getmaze')
		.then(res => res.json())
		.then(data => {
			maze = data;
			console.log('Maze loaded:', maze);
		})
		.catch(err => {
			console.log(err);
		});
}

const btn = document.getElementById('btn1')
btn.addEventListener('click', () => {
	if (maze) {
		createMaze(maze);
	} else {
		alert("try again: maze didn't load yet!")
	}
})

function createMaze(maze) {
	const c = getCanvasContext();
	const ctx = c[0];
	const canvas = c[1];
	const cellx = 80;
	const celly = 80;
	ctx.clearRect(0, 0, canvas.width, canvas.height);

	for (let row = 0; row < maze.length; row++) {
		for (let col = 0; col < maze[row].length; col++) {
			const x = col * (cellx);
			const y = row * celly;
			
			if (maze[row][col] === 1) {
				ctx.fillStyle = 'black';
			} else if (maze[row][col] === 0) {
				ctx.fillStyle = 'white';
			} else if (maze[row][col] === 2) {
				ctx.fillStyle = 'blue'
			}
			ctx.fillRect(x, y, cellx, celly);
		}
	}
}

function getCanvasContext() {
	const canvas = document.getElementById('canva'); // Corrected method call
	if (canvas && canvas.getContext) {
		const ctx = canvas.getContext('2d');
		ctx.canvas.width = maze[0].length * 80
		ctx.canvas.height = maze.length * 80
		return [ctx, canvas];
	} else {
		console.error('Canvas context not available or canvas element not found');
	}
}

function findPath() {
	fetch('/solveMaze')
	.then(res => res.json())
	.then(res => {
		console.log(res)
	})
}