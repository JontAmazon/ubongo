"""Ubongo puzzle class; each puzzle consists of a board and 3-4 pieces."""

from piece import Piece
from copy import deepcopy

class Puzzle:

    def __init__(self, board: list[list[int]], pieces: list[Piece]):
        self.board = board
        self.pieces = pieces
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.available_squares = deepcopy(self.board)

    def possible_move(self, piece: Piece) -> bool:
        """Return True if it's possible to put the piece in the puzzle."""
        # Check if piece is inside the puzzle.
        pos = piece.position
        if pos[0] < 0 \
            or pos[1] < 0 \
            or pos[0] + piece.width() > self.width \
            or pos[1] + piece.height() > self.height:
                print("The piece is outside of the puzzle.")
                return False
        # Check if position is occupied by other pieces.
        for i in range(piece.height()):
            for j in range(piece.width()):
                if piece.piece[i][j]:
                    if not self.available_squares[i + pos[1]][j + pos[0]]:
                        return False
        return True
    
    def put_piece(self, piece: Piece) -> bool:
        """Put a piece in the puzzle and return True if it is possible."""
        if self.possible_move(piece):
            pos = piece.position
            for i in range(piece.height()):
                for j in range(piece.width()):
                    if piece.piece[i][j]:
                        self.available_squares[i + pos[1]][j + pos[0]] = 0
            piece.is_put = True
            return True
        return False

    def remove_piece(self, piece: Piece):
        """Remove the piece from the puzzle."""
        assert piece.is_put
        piece.is_put = False
        pos = piece.position
        for i in range(piece.height()):
            for j in range(piece.width()):
                if piece.piece[i][j]:
                    self.available_squares[i + pos[1]][j + pos[0]] = 1



