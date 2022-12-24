import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from copy import deepcopy
import data.puzzles
import data.colors as colors
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
# background = pygame.image.load("img/flames/4_black2.png")
# background = pygame.transform.scale(background, (screen_width, screen_height))
board_square = pygame.image.load("img/board_square/1.jpg")
board_square = pygame.image.load("img/board_square/2_square_brighter.jfif")
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
    draw_pieces_to_the_right(puzzle)
    draw_put_pieces(puzzle)
    draw_selected_piece(puzzle)

def draw_pieces_to_the_right(puzzle, one_column=True):
    """Draw the pieces that are not put or selected to the right."""
    for counter, piece in enumerate(puzzle.pieces):
        if not piece.is_put and not piece.is_selected:
            # Depending on if 1 or 2 columns, define top_left and square size.
            if one_column:
                piece_y_space = 150
                scaling = 0.40
                top_left = (vertical_line + 0.7*dfb, 0.7*dfb + counter * piece_y_space)
            else: # 2 columns:
                piece_x_space = 230
                piece_y_space = 230
                scaling = 0.45
                if counter < 2:
                    top_left = (vertical_line + 0.7*dfb, dfb + counter * piece_y_space)
                else:
                    top_left = (vertical_line + 0.7*dfb + piece_x_space, dfb + (counter - 2) * piece_y_space)

            # Draw the piece.
            for i in range(piece.height()):
                for j in range(piece.width()):
                    x = top_left[0] + j * scaling * ss
                    y = top_left[1] + i * scaling * ss
                    if piece.piece[i][j]:
                        rect = [x, y, scaling * ss, scaling * ss]
                        pygame.draw.rect(gameWindow, colors.colors[piece.color], rect)

def draw_put_pieces(puzzle):
    """Draw the pieces that are put in the puzzle."""
    for piece in (puzzle.pieces):
        if piece.is_put:
            for i in range(piece.height()):
                for j in range(piece.width()):
                    x = dfb + (piece.position[0] + j) * ss
                    y = dfb + (piece.position[1] + i) * ss
                    if piece.piece[i][j]:
                        rect = [x, y, ss, ss]
                        pygame.draw.rect(gameWindow, colors.colors[piece.color], rect)

def draw_selected_piece(puzzle):
    """Draw the piece that is selected, if any, with its faded color in the puzzle."""
    for piece in (puzzle.pieces):
        if piece.is_selected:
            for i in range(piece.height()):
                for j in range(piece.width()):
                    x = dfb + (piece.position[0] + j) * ss
                    y = dfb + (piece.position[1] + i) * ss
                    if piece.piece[i][j]:
                        rect = [x, y, ss, ss]
                        pygame.draw.rect(gameWindow, piece.faded_color, rect)

def draw_available_squares(puzzle):
    for i in range(puzzle.height):
        for j in range(puzzle.width):
            x = dfb + j * ss
            y = dfb + i * ss
            if puzzle.available_squares[i][j]:
                rect = [x, y, ss, ss]
                pygame.draw.rect(gameWindow, colors.colors["red"], rect)

def select_new_piece(selected_piece: int) -> int:
    """Select new piece by circularly rotating the index 'selected_piece'."""
    # print("\n SELECT NEW PIECE")
    # Deselect previous piece.
    if selected_piece != len(puzzle.pieces):
        puzzle.pieces[selected_piece].is_selected = False
    
    # Select new piece.
    selected_piece += 1
    if selected_piece > len(puzzle.pieces):
        selected_piece = 0
    if selected_piece != len(puzzle.pieces):
        puzzle.pieces[selected_piece].is_selected = True
        if not puzzle.pieces[selected_piece].is_put:
            puzzle.pieces[selected_piece].position = (2, 1)
    return selected_piece

def rotate_piece(selected_piece: int):
    print("\n ROTATE PIECE")
    if selected_piece != len(puzzle.pieces):
        puzzle.pieces[selected_piece].rotate()

# Game Loop
def gameloop():
    exit_game = False
    selected_piece = len(puzzle.pieces)
    fps = 10

    prev_available_squares = deepcopy(puzzle.available_squares)
    print("puzzle.available_squares:")
    print(puzzle.available_squares)

    while not exit_game:
        dx = 0
        dy = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    # (Mouse right click).
                    rotate_piece(selected_piece)
            
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_RIGHT:
                    dx = 1
                    dy = 0
                    
                if event.key == pygame.K_LEFT:
                    dx = -1
                    dy = 0

                if event.key == pygame.K_UP:
                    dy = -1
                    dx = 0

                if event.key == pygame.K_DOWN:
                    dy = 1
                    dx = 0

                if event.key == pygame.K_TAB:
                    selected_piece = select_new_piece(selected_piece)

                if event.key == pygame.K_SPACE:
                    rotate_piece(selected_piece)

                if event.key == pygame.K_RETURN:
                    if selected_piece != len(puzzle.pieces):
                        piece = puzzle.pieces[selected_piece]
                        if piece.is_put:
                            print("\n REMOVE PIECE")
                            puzzle.remove_piece(piece)
                        else:
                            print("\n PUT PIECE")
                            success = puzzle.put_piece(piece)
                            if not success:
                                print("CANNOT PUT PIECE THERE!")
                    selected_piece = select_new_piece(selected_piece)

        # Move piece.
        if selected_piece != len(puzzle.pieces):
            piece = puzzle.pieces[selected_piece]
            
            # First make sure the piece stays inside the puzzle.
            if not piece.is_put:
                if dx < 0:
                    if piece.position[0] <= 0:
                        dx = 0
                if dx > 0:
                    if piece.position[0] + piece.width() >= puzzle.width:
                        dx = 0
                if dy < 0:
                    if piece.position[1] <= 0:
                        dy = 0
                if dy > 0:
                    if piece.position[1] + piece.height() >= puzzle.height:
                        dy = 0
                
            piece.position = (piece.position[0] + dx, piece.position[1] + dy)
        
        gameWindow.fill(colors.black)
        # gameWindow.blit(background, background.get_rect())
        pygame.draw.line(gameWindow, colors.white, (vertical_line,20), (vertical_line,screen_height-20), 2)
        draw_board(puzzle)
        draw_pieces(puzzle)
        # draw_available_squares(puzzle)

        if puzzle.available_squares != prev_available_squares:
            print("puzzle.available_squares:")
            print(puzzle.available_squares)
            for piece in puzzle.pieces:
                if piece.is_selected:
                    print("piece:")
                    print(piece.piece)
                    print(piece.position)
            print("\n")
            prev_available_squares = deepcopy(puzzle.available_squares)

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()


