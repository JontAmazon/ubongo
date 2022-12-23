"""Class for the pieces you put in the puzzle."""

class Piece():
    def __init__(self, piece: list[list[int]], color: str):
        self.piece = piece
        self.color = color
        self.is_put = False

    def width(self):
        return len(self.piece[0])

    def height(self):
        return len(self.piece)

    def rotate(self):
        self.piece = list(zip(*self.piece[::-1]))
    

