import random
import string


class BoggleBoard:
  def __init__(self):
    self.board = []
  
#create randomly generated letters in 4x4 grid
  def shake(self, rows, columns):
    letters = []
    for i in range(rows):
        row = []
        for j in range(columns):
            x = random.choice(string.ascii_uppercase)
            if x == 'Q':
                x = 'Qu'
            row.append(x)
        self.board.append(row)


  def print_board(self):
    for rows in self.board:
      for column in rows:
        print(column, end=" ")
      print()


# # Print the generated grid
# for row in four_by_four_grid:
#     print(" ".join(row))



    # self._letters = letters
    # self._input = input
    # if input == "shake!":
    #   for _ in self._rows:
    #     return random.choice(string.ascii_uppercase)
    # else:
    #   return "invalid input" 

blankTable = BoggleBoard()
blankTable.shake(16,4)
blankTable.print_board()