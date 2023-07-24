import tkinter as tk
import random
import time

# Game Constants
BOARD_SIZE = 15
CELL_SIZE = 30
SNAKE_HEAD = 'X'
SNAKE_BODY = 'o'
FOOD = '*'
TK_SILENCE_DEPRECATION=1

# Initialize Snake
snake = [(BOARD_SIZE // 2, BOARD_SIZE // 2)]
snake_direction = (0, 1)

# Food
food_position = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))

# Function to handle user input
def on_key_press(event):
    global snake_direction
    key = event.keysym
    if key == 'Up':
        snake_direction = (-1, 0)
    elif key == 'Down':
        snake_direction = (1, 0)
    elif key == 'Left':
        snake_direction = (0, -1)
    elif key == 'Right':
        snake_direction = (0, 1)

# Function to move the snake
def move_snake():
    global snake, snake_direction, food_position

    # Move the snake
    head_x, head_y = snake[-1]
    dx, dy = snake_direction
    new_head = (head_x + dx, head_y + dy)

    # Check for collisions with food and boundaries
    if new_head == food_position:
        food_position = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
    else:
        snake.pop(0)

    # Check if the new head position is within the valid range of the game board
    if 0 <= new_head[0] < BOARD_SIZE and 0 <= new_head[1] < BOARD_SIZE:
        snake.append(new_head)
    else:
        # Game Over condition if the snake hits the boundaries
        canvas.create_text(CELL_SIZE * (BOARD_SIZE // 2), CELL_SIZE * (BOARD_SIZE // 2), text="Game Over!", font=("Helvetica", 20), fill="red")
        return

    # Update the game board
    draw_board()

    # Schedule the next move
    root.after(200, move_snake)

# Function to draw the game board
def draw_board():
    canvas.delete("all")
    for x, y in snake:
        canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill="green")
    canvas.create_rectangle(food_position[0] * CELL_SIZE, food_position[1] * CELL_SIZE,
                            (food_position[0] + 1) * CELL_SIZE, (food_position[1] + 1) * CELL_SIZE, fill="red")

# Create the main window
root = tk.Tk()
root.title("Snake Game")
root.geometry(f"{CELL_SIZE * BOARD_SIZE}x{CELL_SIZE * BOARD_SIZE}")

# Create the canvas to draw the game board
canvas = tk.Canvas(root, width=CELL_SIZE * BOARD_SIZE, height=CELL_SIZE * BOARD_SIZE, bg="black")
canvas.pack()

# Bind arrow key presses to the on_key_press function
root.bind('<Up>', on_key_press)
root.bind('<Down>', on_key_press)
root.bind('<Left>', on_key_press)
root.bind('<Right>', on_key_press)

# Start the game loop
move_snake()

# Run the application
root.mainloop()
