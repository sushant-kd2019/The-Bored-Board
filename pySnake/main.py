import random
import curses

# initial setup of the game.

# initializing the screen and configuring it.
s = curses.initscr()

curses.curs_set(0)

sh, sw = s.getmaxyx()

w = curses.newwin(sh, sw, 0, 0)

w.keypad(1)

w.timeout(100)

# initialising the snake's position.
snake_x = sw/4
snake_y = sh/2

# initialising the snake's body parts.
snake = [[snake_y, snake_x], [snake_y, snake_x-1], [snake_y, snake_x-2]]

# setting initial food item
food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# initial direction of snake.
key = curses.KEY_RIGHT
score = 0
while True:
    next_key = w.getch()

    # ensuring that snake cannot make a 180 degree turn.
    wrong_operation = True if (next_key == -1 or next_key == curses.KEY_DOWN and key == curses.KEY_UP
                               or key == curses.KEY_DOWN and next_key == curses.KEY_UP
                               or next_key == curses.KEY_LEFT and key == curses.KEY_RIGHT
                               or key == curses.KEY_LEFT and next_key == curses.KEY_RIGHT) else False
    key = key if wrong_operation else next_key

    # losing criteria of game. (hitting wall or hitting yourself.)
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.nocbreak()
        s.keypad(False)
        curses.echo()
        curses.endwin()
        print("Not so charming anymore, huh snake charmer?")
        print("Your Score : "+str(score))
        break
        quit()

    # directional movement.
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    snake.insert(0, new_head)
    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            while nf in snake:
                nf = [
                    random.randint(1, sh-1),
                    random.randint(1, sw-1)
                ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    try:
        w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
    except:
        print("Not so charming anymore, huh snake charmer?")
