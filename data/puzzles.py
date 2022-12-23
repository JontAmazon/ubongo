"""Define the different puzzles."""
import data.pieces as pieces
from piece import Piece
from puzzle import Puzzle

line    = pieces.p1
S       = pieces.p2
orange  = pieces.p3
big_T   = pieces.p4
big_L   = pieces.p5
acrobat = pieces.p6
red_S   = pieces.p7
block   = pieces.p8
small_L = pieces.p9
small_T = pieces.p10

puzzles = [
    
    Puzzle(
        board = [[0,0,1,1,1,0],
                 [0,1,1,1,1,1],
                 [0,1,1,1,1,0],
                 [1,1,1,1,1,0]],
        pieces = [line, S, orange, big_T]
    ),

    Puzzle(
        board = [[1,1,1,1,1,1],
                 [0,0,1,1,1,1],
                 [0,0,1,1,1,1]],
        pieces = [small_L, orange, red_S]
    ),

    Puzzle(
        board = [[0,1,0,0,0,1],
                 [0,1,1,1,1,1],
                 [0,1,1,1,1,1],
                 [1,1,1,1,1,1]],
        pieces = [big_L, line, acrobat, big_T]
    ),

]


