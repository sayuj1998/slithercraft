from tkinter import *
import random

WIDTH = 1500
HEIGHT = 900
SPEED = 120
SPACE = 30
SNAKE_STARTING_LENGTH = 2
SNAKE_COLOR = "#00FF00"
ITEM_COLOR = "#ADD8E6"
BACKGROUND = "#000000"

game_over = False

class SnakePlayer:
    def __init__(self):
        """Snake class"""
        self.snake_size:int = SNAKE_STARTING_LENGTH
        self.coordinates = []
        self.oval = []

        for i in range(0, SNAKE_STARTING_LENGTH):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            oval:int = canvas.create_oval(x, y, x + SPACE, y + SPACE, fill=SNAKE_COLOR, tag="snake")
            self.oval.append(oval)

class Item:
    def __init__(self):
        """Item class"""
        x:int = random.randint(0, (WIDTH//SPACE)-1) * SPACE
        y:int = random.randint(0, (HEIGHT//SPACE)-1) * SPACE

        self.coordinates = [x, y]
        canvas.create_rectangle(x, y, x + SPACE, y + SPACE, fill=ITEM_COLOR, tag="item")

def advance_to_next_turn(snake, item):
    """Move the snake to next turns"""
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE
    elif direction == "down":
        y += SPACE
    elif direction == "left":
        x -= SPACE
    elif direction == "right":
        x += SPACE

    snake.coordinates.insert(0, (x, y))

    oval:int = canvas.create_oval(x, y, x + SPACE, y + SPACE, fill=SNAKE_COLOR)

    snake.oval.insert(0, oval)

    if x == item.coordinates[0] and y == item.coordinates[1]:
        global score
        score += 1000
        label.config(text=f"Score: {score}")

        canvas.delete("item")
        item = Item()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.oval[-1])
        del snake.oval[-1]

    if detect_collision(snake):
        end_game()
    else:
        window.after(SPEED, advance_to_next_turn, snake, item)

def change_direction(new_direction: str):
    """Change the direction of the snake"""
    global direction

    if new_direction == "left" or new_direction == "a":
        if direction != "right" and direction != "d":
            direction = new_direction
    elif new_direction == "right" or new_direction == "d":
        if direction != "left" and direction != "a":
            direction = new_direction
    elif new_direction == "up" or new_direction == "w":
        if direction != "down" and direction != "s":
            direction = new_direction
    elif new_direction == "down" or new_direction == "s":
        if direction != "up" and direction != "w":
            direction = new_direction

def detect_collision(snake: SnakePlayer) -> bool:
    """Detect collision of the snake with boundaries or itself"""
    x, y = snake.coordinates[0]

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

def end_game():
    """End the game and display the final score"""
    global game_over
    game_over = True

    label.pack_forget()
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=("Arial", 70, "bold"), text="DEFEAT\n",
                       fill="red", tag="endgame")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 50,
                       font=("Arial", 40), text=f"Score: {score}",
                       fill="#66ff00", tag="endgame")
    try_again_button.pack()

def try_again():
    """Reset the game"""
    global score, direction, game_over
    score = 0
    direction = "down"
    game_over = False
    label.config(text=f"Score: {score}")
    canvas.delete("endgame")
    snake = SnakePlayer()
    item = Item()
    advance_to_next_turn(snake, item)
    try_again_button.pack_forget()

window = Tk()
window.title("SlitherCraft")
window.resizable(True, True)
window.configure(bg="#111111")

"""Making it launch in the middle of the screen"""
window_width = WIDTH
window_height = HEIGHT
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

score = 0
direction = "down"

label = Label(window, text="Score:{}".format(score), font=("Arial", 40), bg="#111111", fg="white")
label.pack()

canvas = Canvas(window, bg=BACKGROUND, width=WIDTH, height=HEIGHT)
canvas.pack()

try_again_button = Button(window, text="Try Again", font=("Arial", 20), command=try_again)

window.update()

window_width: int = window.winfo_width()
window_height: int = window.winfo_height()
screen_width: int = window.winfo_screenwidth()
screen_height: int = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

"""Binding arrow keys for movement"""
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

"""Binding WASD keys for movement"""
window.bind("<a>", lambda event: change_direction("left"))
window.bind("<d>", lambda event: change_direction("right"))
window.bind("<w>", lambda event: change_direction("up"))
window.bind("<s>", lambda event: change_direction("down"))

snake = SnakePlayer()
item = Item()

advance_to_next_turn(snake, item)

window.mainloop()
