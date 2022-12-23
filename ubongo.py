import pygame
import data.puzzles
import colors
pygame.init()

# Creating window
screen_width = 1300
screen_height = 700
vertical_line = 800
ss = 100
dfb = 80 # distance from border
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Ubongo")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# Load images
background = pygame.image.load("img/flames/3_wip3.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

board_square = pygame.image.load("img/board_square/1.jpg")
board_square = pygame.image.load("img/board_square/2_square.jfif")
board_square = pygame.transform.scale(board_square, (ss, ss))

# Load puzzle
puzzle = data.puzzles.puzzles[0]
board = puzzle.board
pieces = puzzle.pieces

def draw_board(puzzle):
    # Draw board
    for i in range(puzzle.height):
        for j in range(puzzle.width):
            x = dfb + j * ss
            y = dfb + i * ss
            if puzzle.board[i][j]:
                gameWindow.blit(board_square, [x, y, ss, ss])

    # Draw black grid lines
    x0, x1 = dfb, dfb + puzzle.width * ss
    for i in range(puzzle.height + 1):
        y = dfb + i * ss
        pygame.draw.line(gameWindow, colors.black, (x0, y), (x1, y), 1)
    y0, y1 = dfb, dfb + puzzle.height * ss
    for j in range(puzzle.width + 1):
        x = dfb + j * ss
        pygame.draw.line(gameWindow, colors.black, (x, y0), (x, y1), 1)

def draw_pieces(puzzle):
    # TODO: think about opacity...
    for counter, piece in enumerate(puzzle.pieces):
        piece_x_space = 230
        piece_y_space = 230
        scaling = 0.45
        if counter < 2:
            top_left = (vertical_line + 0.7*dfb, dfb + counter * piece_y_space)
        else:
            top_left = (vertical_line + 0.7*dfb + piece_x_space, dfb + (counter - 2) * piece_y_space)

        for i in range(piece.height()):
            for j in range(piece.width()):
                x = top_left[0] + j * scaling * ss
                y = top_left[1] + i * scaling * ss
                if piece.piece[i][j]:
                    rect = [x, y, scaling * ss, scaling * ss]
                    pygame.draw.rect(gameWindow, colors.colors[piece.color], rect)

# Game Loop
def gameloop():
    exit_game = False
    x_pos = 200
    y_pos = 200
    fps = 10
    while not exit_game:
        dx = 0
        dy = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dx = ss
                    dy = 0

                if event.key == pygame.K_LEFT:
                    dx = - ss
                    dy = 0

                if event.key == pygame.K_UP:
                    dy = - ss
                    dx = 0

                if event.key == pygame.K_DOWN:
                    dy = ss
                    dx = 0

                if event.key == pygame.K_RETURN:
                    # TODO
                    pass

                if event.key == pygame.K_TAB:
                    # TODO
                    pass

        x_pos = x_pos + dx
        y_pos = y_pos + dy

        gameWindow.fill(colors.black)
        #gameWindow.blit(background, background.get_rect()) # TODO: wait for Agnes to send background
        pygame.draw.rect(gameWindow, colors.blue, [x_pos, y_pos, ss, ss])
        pygame.draw.line(gameWindow, colors.white, (vertical_line,20), (vertical_line,screen_height-20), 2)
        draw_board(puzzle)
        draw_pieces(puzzle)

        if x_pos<0 or x_pos>screen_width-20 or y_pos<50 or y_pos>screen_height-20:
            x_pos = 50
            y_pos = 50

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()


