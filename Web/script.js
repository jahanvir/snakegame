document.addEventListener('DOMContentLoaded', () => {
    const gameContainer = document.querySelector('.game-container');
    const appleImage = document.getElementById('apple'); 
    const scoreElement = document.getElementById('score');
    const gridSize= 20;
    const snakeSpeed = 150;

    let snake = [{ x: 10, y: 10 }];
    let food = { x: 5, y: 5 };
    let direction = { x: 0, y: 0 };
    let score = 0;

    function updateScore() {
        scoreElement.textContent = `Score: ${score}`;
    }

    function drawSnake() {
        // Remove existing snake elements
        const existingSnakeElements = document.querySelectorAll('.snake');
        existingSnakeElements.forEach((el) => el.remove());

        // Draw snake body
        for (let i = 0; i < snake.length - 1; i++) { // Traversing from head to tail
            const snakeBodyElement = document.createElement('div');
            snakeBodyElement.className = 'snake';
            snakeBodyElement.style.gridRowStart = snake[i].y;
            snakeBodyElement.style.gridColumnStart = snake[i].x;
            gameContainer.appendChild(snakeBodyElement);
        }

        // Draw snake head
        const snakeHeadElement = document.createElement('div');
        snakeHeadElement.className = 'snake-head';
        snakeHeadElement.style.gridRowStart = snake[snake.length - 1].y;
        snakeHeadElement.style.gridColumnStart = snake[snake.length - 1].x;

        // Create the eyes for the snake head
        const eye1 = document.createElement('div');
        eye1.className = 'eye';
        eye1.style.top = '25%';
        eye1.style.left = '25%';

        const eye2 = document.createElement('div');
        eye2.className = 'eye';
        eye2.style.top = '25%';
        eye2.style.right = '25%';

        snakeHeadElement.appendChild(eye1);
        snakeHeadElement.appendChild(eye2);

        gameContainer.appendChild(snakeHeadElement);
    }

    function drawFood() {
        appleImage.style.gridRowStart = food.y;
        appleImage.style.gridColumnStart = food.x;
        appleImage.style.display = 'block'; // Make the apple image visible
        gameContainer.appendChild(appleImage);
    }

    function resetGame() {
        snake = [{ x: 10, y: 10 }];
        food = { x: 5, y: 5 };
        direction = { x: 0, y: 0 };
        clearInterval(gameLoop);
        gameContainer.innerHTML = '';
        score=0
        updateScore();
        gameLoop = setInterval(gameLoopFn, snakeSpeed);
    }

    function moveSnake() {
        const newHead = {
            x: snake[snake.length - 1].x + direction.x,
            y: snake[snake.length - 1].y + direction.y,
        };
    
        // Check if the new head position is within the boundaries
        if (newHead.x < 1 || newHead.x > gridSize || newHead.y < 1 || newHead.y > gridSize) {
            // Snake hit the boundary, game over
            gameOver();
            return;
        }
    
        // Check if the new head is at the same position as the apple
        if (newHead.x === food.x && newHead.y === food.y) {
            // Snake has eaten the apple, increase score and regenerate the apple
            score++;
            updateScore();
            generateNewFood();
        } else {
            // Remove the tail of the snake if it hasn't eaten the apple
            snake.shift();
        }
    
        // Add the new head to the snake
        snake.push(newHead);
    
        // Redraw the snake on the grid
        drawSnake();
    }

    function gameOver() {
        clearInterval(gameLoop);
        alert(`Game Over\nYour Score: ${score}`);
        resetGame();
    }

    function generateNewFood() {
        food.x = Math.floor(Math.random() * gridSize) + 1;
        food.y = Math.floor(Math.random() * gridSize) + 1;
    }

    function checkCollision() {
        if (
            snake[0].x < 1 ||
            snake[0].x > gridSize ||
            snake[0].y < 1 ||
            snake[0].y > gridSize
        ) {
            clearInterval(gameLoop);
            alert('Game Over! Your score: ' + (snake.length - 1));
            resetGame();
        }

        for (let i = 1; i < snake.length; i++) {
            if (snake[i].x === snake[0].x && snake[i].y === snake[0].y) {
                clearInterval(gameLoop);
                alert('Game Over! Your score: ' + (snake.length - 1));
                resetGame();
            }
        }
    }

    document.addEventListener('keydown', event => {
        switch (event.key) {
            case 'ArrowUp':
                direction = { x: 0, y: -1 };
                break;
            case 'ArrowDown':
                direction = { x: 0, y: 1 };
                break;
            case 'ArrowLeft':
                direction = { x: -1, y: 0 };
                break;
            case 'ArrowRight':
                direction = { x: 1, y: 0 };
                break;
        }
    });

    function gameLoopFn() {
        gameContainer.innerHTML = '';
        moveSnake();
        drawSnake();
        drawFood();
        checkCollision();
    }

    let gameLoop = setInterval(gameLoopFn, snakeSpeed);
});