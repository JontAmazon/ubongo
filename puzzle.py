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

    def put_piece(self, piece: Piece, position: tuple[int, int]) -> bool:
        """Put a piece in the puzzle and return True if it was possible."""
        if self.possible_move(piece, position):
            # TODO: do a for-loop like in "possible_move", but update
            #       the values in self.available_squares !!
            piece.is_put = True
            return True
        return False

    def possible_move(self, piece: Piece, position: tuple[int, int]) -> bool:
        # Check if piece is inside the puzzle.
        if position[0] < 0 \
            or position[1] < 0 \
            or position[0] + piece.width > self.width \
            or position[1] + piece.height > self.height:
                print("The piece is outside of the puzzle.")
                return False
        
        # Check if position is occupied by other pieces.
        for i in range(piece.height):    # height, right?
            for j in range(piece.width): # width, right?
                if piece[i][j]:
                    if not self.available_squares[i + position[0]][j + position[1]]: # hopefully working
                        return False
        return True






