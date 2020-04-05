import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()

# Creating a new window using height and width at the strting of the screen
window = curses.newwin(sh, sw, 0, 0)

# Accept keypad input
window.keypad(1)
# Refresh every 100ms
window.timeout(100)

# Creating a snake's initial position
snake_x = sw/4
snake_y = sh/2

# Defining the snake
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

# Set the food to be at ceneter of the screen
food = [sh/2,sw/2]

# Adding the food to the screen
window.addch(food[0], food[1], curses.ACS_PI)

# Set the direction of movement of snake at first.
key = curses.KEY_RIGHT

# For every movement
while True:
    # Get the next key
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    # Check if the person has lost the game
    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    # Check the key pressed
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] += 1
    if key == curses.KEY_LEFT:
        new_head[1] += 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0,new_head)

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.readint(1, sh-1),
                random.readint(1, sw-1)
            ]

            food = new_food if new_food not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.A_COLOR)
