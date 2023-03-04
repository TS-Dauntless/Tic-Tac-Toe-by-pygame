import pygame


# Initializing Pygame
pygame.init()

# Creating Pygame Window
screen = pygame.display.set_mode((600, 600))

# Creating Logo and Caption
pygame.display.set_caption("Tic Tac Teo")
pygame.display.set_icon(pygame.transform.scale(pygame.image.load("img/TTT_logo.png"), (128, 128)))

# Load Image
img_o = pygame.transform.scale(pygame.image.load("img/O.png"), (128, 128))
img_x = pygame.transform.scale(pygame.image.load("img/X.png"), (128, 128))



# Initialing Variables
is_x = []
x_cor = []
y_cor = []
x_turn = True
game_over = False

for i in range(1, 10):
    x_cor.append(None)
    y_cor.append(None)
    is_x.append(None)


def initialize_variable():
    global is_x, x_turn, game_over

    is_x = []
    x_turn = True
    game_over = False

    for b in range(1, 10):
        x_cor.append(None)
        y_cor.append(None)
        is_x.append(None)


initialize_variable()


# Functions Block

# Function for displaying X
def display_x(xcor, ycor, m):
    global img_x
    if is_x[m] and is_x[m] is not None:
        screen.blit(img_x, (xcor, ycor))


# Function for displaying O
def display_y(xcor, ycor, n):
    global img_o
    if not is_x[n] and is_x[n] is not None:
        screen.blit(img_o, (xcor, ycor))


# Function for displaying border lines
def display_border_lines():
    # vertical lines
    pygame.draw.line(screen, (0, 0, 0), (50, 50), (50, 550))
    pygame.draw.line(screen, (0, 0, 0), (216, 50), (216, 550))
    pygame.draw.line(screen, (0, 0, 0), (382, 50), (382, 550))
    pygame.draw.line(screen, (0, 0, 0), (550, 50), (550, 550))

    # horizontal lines
    pygame.draw.line(screen, (0, 0, 0), (50, 50), (550, 50))
    pygame.draw.line(screen, (0, 0, 0), (50, 216), (550, 216))
    pygame.draw.line(screen, (0, 0, 0), (50, 382), (550, 382))
    pygame.draw.line(screen, (0, 0, 0), (50, 550), (550, 550))


# Function for cross line
def display_cross_line(sx, sy, ex, ey):
    pygame.draw.line(screen, (0, 255, 0), (sx, sy), (ex, ey), 10)


# Function for if box clicked
# noinspection PyTypeChecker
def check_if_box(x, y):
    global is_x, x_turn
    if 50 <= x <= 216 and 50 <= y <= 216:
        if x_cor[0] is not True:
            x_cor[0] = 67
            y_cor[0] = 70
            if x_turn:
                is_x[0] = True
                x_turn = False
            else:
                is_x[0] = False
                x_turn = True

    elif 216 <= x <= 382 and 50 <= y <= 216:
        if x_cor[1] is not True:
            x_cor[1] = 235
            y_cor[1] = 70
            if x_turn:
                is_x[1] = True
                x_turn = False
            else:
                is_x[1] = False
                x_turn = True

    elif 382 <= x <= 550 and 50 <= y <= 216:
        if x_cor[2] is not True:
            x_cor[2] = 400
            y_cor[2] = 70
            if x_turn:
                is_x[2] = True
                x_turn = False
            else:
                is_x[2] = False
                x_turn = True

    elif 50 <= x <= 216 and 216 <= y <= 382:
        if x_cor[3] is not True:
            x_cor[3] = 70
            y_cor[3] = 235
            if x_turn:
                is_x[3] = True
                x_turn = False
            else:
                is_x[3] = False
                x_turn = True

    elif 216 <= x <= 382 and 216 <= y <= 382:
        if x_cor[4] is not True:
            x_cor[4] = 235
            y_cor[4] = 235
            if x_turn:
                is_x[4] = True
                x_turn = False
            else:
                is_x[4] = False
                x_turn = True

    elif 382 <= x <= 550 and 216 <= y <= 382:
        if x_cor[5] is not True:
            x_cor[5] = 400
            y_cor[5] = 235
            if x_turn:
                is_x[5] = True
                x_turn = False
            else:
                is_x[5] = False
                x_turn = True

    elif 50 <= x <= 216 and 382 <= y <= 550:
        if x_cor[6] is not True:
            x_cor[6] = 70
            y_cor[6] = 400
            if x_turn:
                is_x[6] = True
                x_turn = False
            else:
                is_x[6] = False
                x_turn = True

    elif 216 <= x <= 382 and 382 <= y <= 550:
        if x_cor[7] is not True:
            x_cor[7] = 235
            y_cor[7] = 400
            if x_turn:
                is_x[7] = True
                x_turn = False
            else:
                is_x[7] = False
                x_turn = True

    elif 382 <= x <= 550 and 382 <= y <= 550:
        if x_cor[8] is not True:
            x_cor[8] = 400
            y_cor[8] = 400
            if x_turn:
                is_x[8] = True
                x_turn = False
            else:
                is_x[8] = False
                x_turn = True


# Function for displaying play again
def display_play_again():
    screen.blit(pygame.font.Font("freesansbold.ttf", 40).
                render("Play again ? Press Enter", True, (0, 0, 0), (255, 255, 255)), (70, 280))


def gameover():
    global is_x, game_over

    # For X

    if is_x[0] and is_x[1] and is_x[2]:
        game_over = True
        sx = 50
        sy = 133
        ex = 550
        ey = 133
        return sx, sy, ex, ey
    elif is_x[0] and is_x[3] and is_x[6]:
        game_over = True
        sx = 133
        sy = 50
        ex = 133
        ey = 550
        return sx, sy, ex, ey
    elif is_x[0] and is_x[4] and is_x[8]:
        game_over = True
        sx = 50
        sy = 50
        ex = 550
        ey = 550
        return sx, sy, ex, ey

    elif is_x[1] and is_x[4] and is_x[7]:
        game_over = True
        sx = 299
        sy = 50
        ex = 299
        ey = 550
        return sx, sy, ex, ey

    elif is_x[2] and is_x[5] and is_x[8]:
        game_over = True
        sx = 466
        sy = 50
        ex = 466
        ey = 550
        return sx, sy, ex, ey
    elif is_x[2] and is_x[4] and is_x[6]:
        game_over = True
        sx = 550
        sy = 50
        ex = 50
        ey = 550
        return sx, sy, ex, ey

    elif is_x[3] and is_x[4] and is_x[5]:
        game_over = True
        sx = 50
        sy = 299
        ex = 550
        ey = 299
        return sx, sy, ex, ey

    elif is_x[6] and is_x[7] and is_x[8]:
        game_over = True
        sx = 50
        sy = 466
        ex = 550
        ey = 466
        return sx, sy, ex, ey

    # For O

    elif is_x[0] is False and is_x[1] is False and is_x[2] is False:
        game_over = True
        sx = 50
        sy = 133
        ex = 550
        ey = 133
        return sx, sy, ex, ey
    elif is_x[0] is False and is_x[3] is False and is_x[6] is False:
        game_over = True
        sx = 133
        sy = 50
        ex = 133
        ey = 550
        return sx, sy, ex, ey
    elif is_x[0] is False and is_x[4] is False and is_x[8] is False:
        game_over = True
        sx = 50
        sy = 50
        ex = 550
        ey = 550
        return sx, sy, ex, ey

    elif is_x[1] is False and is_x[4] is False and is_x[7] is False:
        game_over = True
        sx = 299
        sy = 50
        ex = 299
        ey = 550
        return sx, sy, ex, ey

    elif is_x[2] is False and is_x[5] is False and is_x[8] is False:
        game_over = True
        sx = 466
        sy = 50
        ex = 466
        ey = 550
        return sx, sy, ex, ey
    elif is_x[2] is False and is_x[4] is False and is_x[6] is False:
        game_over = True
        sx = 550
        sy = 50
        ex = 50
        ey = 550
        return sx, sy, ex, ey

    elif is_x[3] is False and is_x[4] is False and is_x[5] is False:
        game_over = True
        sx = 50
        sy = 299
        ex = 550
        ey = 299
        return sx, sy, ex, ey

    elif is_x[6] is False and is_x[7] is False and is_x[8] is False:
        game_over = True
        sx = 50
        sy = 466
        ex = 550
        ey = 466
        return sx, sy, ex, ey

    return None, None, None, None


# Main Game Loop
running = True

while running:
    # Background
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # mouse event
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            check_if_box(mx, my)

        # Keyboard event
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    initialize_variable()

    # Draw boarder lines
    display_border_lines()

    # displaying X and O
    for j in range(0, 9):
        if is_x[j]:
            display_x(x_cor[j], y_cor[j], j)
        else:
            display_y(x_cor[j], y_cor[j], j)

    # cross line when game over
    s_x, s_y, e_x, e_y = gameover()

    if game_over:
        display_cross_line(s_x, s_y, e_x, e_y)
        display_play_again()

    # update pygame window
    pygame.display.update()
