"""Define the different types of pieces."""
from piece import Piece

p1 = Piece([[1],         # 🟨
            [1],         # 🟨
            [1]],        # 🟨
            "yellow")

p2 = Piece([[1,0],       # 🟦
            [1,1],       # 🟦🟦
            [0,1]],      # ⬛🟦
            "greenblue")

p3 = Piece([[0,1,0,0],   # ⬛🟧
            [1,1,1,1]],  # 🟧🟧🟧🟧
            "orange")

p4 = Piece([[1,1,1],     # ⬜⬜⬜
            [0,1,0],     # ⬛⬜
            [0,1,0]],    # ⬛⬜
            "white")

p5 = Piece([[0,0,0,1],   # ⬛⬛⬛🟪
            [1,1,1,1]],  # 🟪🟪🟪🟪
            "pink")

p6 = Piece([[1,1,0],     # 🟦🟦
            [0,1,1],     # ⬛🟦🟦
            [0,1,0]],    # ⬛🟦
            "blue")

p7 = Piece([[0,0,1,1],   # ⬛⬛🟥🟥
            [1,1,1,0]],  # 🟥🟥🟥
            "red")

p8 = Piece([[1,0],       # 🟪
            [1,1],       # 🟪🟪
            [1,1]],      # 🟪🟪
            "purple")

p9 = Piece([[1,0],       # 🟩
            [1,0],       # 🟩
            [1,1]],      # 🟩🟩
            "light_green")

p10 = Piece([[1,0],      # 🟩
             [1,1],      # 🟩🟩
             [1,0]],     # 🟩
            "dark_green")


############################################
#############   ROTATION   #################
############################################
"""
_3 = [[0,1,0,0],   # ⬛🟧
      [1,1,1,1]]   # 🟧🟧🟧🟧

     [[1,0],       # 🟧
      [1,1],       # 🟧🟧
      [1,0],       # 🟧
      [1,0]]       # 🟧

     [[1,1,1,1],   # 🟧🟧🟧🟧
      [0,0,1,0]]   # ⬛⬛🟧

     [[0,1],       # ⬛🟧
      [0,1],       # ⬛🟧
      [1,1],       # 🟧🟧
      [0,1]]       # ⬛🟧
"""