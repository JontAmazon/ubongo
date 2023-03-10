"""Class for the pieces you put in the puzzle."""

import data.colors

class Piece():
    def __init__(self, piece: list[list[int]], color: str):
        self.piece = piece
        self.color = color
        self.faded_color = tuple([0.90 * value for value in data.colors.colors[color]])
        self.is_put = False
        self.is_selected = False
        self.position = (2, 1)

    def width(self):
        return len(self.piece[0])

    def height(self):
        return len(self.piece)

    def rotate(self):
        self.piece = list(zip(*self.piece[::-1]))
    
    

