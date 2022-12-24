import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
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
                    x = piece.position[0] + j * ss
                    y = piece.position[1] + i * ss
                    if piece.piece[i][j]:
                        rect = [x, y, ss, ss]
                        pygame.draw.rect(gameWindow, colors.colors[piece.color], rect)

def draw_selected_piece(puzzle):
    """Draw the piece that is selected, if any, with its faded color in the puzzle."""
    for piece in (puzzle.pieces):
        if piece.is_selected:
            for i in range(piece.height()):
                for j in range(piece.width()):
                    x = piece.position[0] + j * ss
                    y = piece.position[1] + i * ss
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



# Game Loop
def gameloop():
    exit_game = False
    x_pos = dfb + 2 * ss
    y_pos = dfb + 1 * ss
    selected_piece = len(puzzle.pieces)
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

                if event.key == pygame.K_SPACE:
                    print("SELECT NEW PIECE")
                    # Deselect previous piece.
                    if selected_piece != len(puzzle.pieces):
                        puzzle.pieces[selected_piece].is_selected = False
                    
                    # Rotate selected_piece
                    selected_piece += 1
                    if selected_piece > len(puzzle.pieces):
                        selected_piece = 0
                    
                    # Select piece
                    if selected_piece != len(puzzle.pieces):
                        puzzle.pieces[selected_piece].is_selected = True
                        x_pos = dfb + 2 * ss
                        y_pos = dfb + 1 * ss

                if event.key == pygame.K_TAB:
                    print("ROTATE PIECE")
                    if selected_piece != len(puzzle.pieces):
                        puzzle.pieces[selected_piece].rotate()

                if event.key == pygame.K_RETURN:
                    if selected_piece != len(puzzle.pieces):
                        piece = puzzle.pieces[selected_piece]

                        if piece.is_put:
                            print("REMOVE PIECE")
                            piece.is_put = False
                            # TODO: remove piece from puzzle's available_squares

                        else:
                            print("PUT PIECE")
                            # TODO: try to put piece.
                            success = puzzle.put_piece(piece)
                            if not success:
                                print("CANNOT PUT PIECE THERE!")
                            else:
                                piece.is_put = True
    
        x_pos = x_pos + dx
        y_pos = y_pos + dy

        if x_pos < 0 or x_pos > screen_width - 20 or y_pos < 50 or y_pos > screen_height - 20:
            x_pos = x_pos - dx
            y_pos = y_pos - dy
            # TODO: limit the position to within the puzzle.
        
        # Calculate square index corresponding to pixels (x_pos, y_pos)
        # ...
        # ... wait, no. Better if I change piece.position to integers in [0, 5] 
        #               and change the code here in ubongo.py instead of the 
        #               code in puzzle.py



        if selected_piece != len(puzzle.pieces):
            piece = puzzle.pieces[selected_piece]
            if not piece.is_put:
                piece.position = (x_pos, y_pos)

        gameWindow.fill(colors.black)
        # gameWindow.blit(background, background.get_rect())
        pygame.draw.line(gameWindow, colors.white, (vertical_line,20), (vertical_line,screen_height-20), 2)
        draw_board(puzzle)
        draw_pieces(puzzle)
        # draw_available_squares(puzzle)

        print("available squares:")
        print(puzzle.available_squares)
        
        for piece in puzzle.pieces:
            if piece.is_selected:
                print("\n piece:")
                print(piece.piece)
                print(piece.position)
        print("\n\n")

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()


