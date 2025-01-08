let mazePromise;
let maze;
let solution;
let pos = 0;

window.onload = () => {
	fetch('/getmaze')
		.then(res => res.json())
		.then(data => {
			maze = data;
			console.log('Maze loaded:', maze);
			showNotification('loaded maze successfully')
		})
		.catch(err => {
			console.log(err);
		});
	
	fetch('/solveMaze')
	.then(res => res.json())
	.then(data => {
		solution = JSON.parse(data);
		console.log("solution loaded:", solution);
		showNotification('loaded solution successfully');
	})
}

const btn = document.getElementById('btn1')
btn.addEventListener('click', () => {
	if (maze) {
		createMaze(maze);
	} else {
		alert("try again: maze didn't load yet!")
	}
})

const btn2 = document.getElementById('btn2');
btn2.addEventListener('click', () => {
	if(solution && maze) {
		for (let k = 0; k < solution.path.length; k++){
			console.log(k, solution.path[k])
			index2 = solution.path[k]
			i = parseInt(index2 / maze[0].length);
			j = parseInt(index2 % maze[0].length);
			maze[i][j] = 2;
		}
		btn1.click()
		// console.log('k= ', k, ', index2 =', index2, ", index=",index, realPos)
	} else {
		alert("try again after few sec")
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

function showNotification(message, isError = false) {
    const container = document.getElementById('notification-container');
    const notification = document.createElement('div');
    notification.className = 'notification';
    if (isError) {
        notification.style.backgroundColor = '#e74c3c'; // Red for errors
    }
    notification.innerText = message;
    container.appendChild(notification);

    // Automatically hide the notification after 3 seconds
    setTimeout(() => {
        notification.classList.add('hide');
        setTimeout(() => {
            container.removeChild(notification);
        }, 500); // Wait for the fade-out transition to complete
    }, 3000);
}