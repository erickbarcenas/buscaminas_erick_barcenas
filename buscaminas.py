class CompassRose:
  def __init__(self, board, cols, rows, x, y):
    self.board = board
    self.cols = cols
    self.rows = rows
    self.x = x
    self.y = y

    self.top = y - 1
    self.right = x + 1
    self.left = x - 1
    self.down = y + 1

    if y !=0:
      self.N = self.board[self.top][self.x] #
      if self.x != self.cols - 1:
        self.NE = self.board[self.top][self.right] #
      if self.x != 0:
        self.NW = self.board[self.top][self.left]

    # Corner positions
    if self.x != self.cols - 1: 
      self.E = self.board[self.y][self.right] # <---

    if self.y != self.rows - 1:
      self.S = self.board[self.down][self.x] # <---
      if self.x != self.cols - 1:
        self.SE = self.board[self.down][self.right] # <---
      

    if self.x != 0:
      self.W = self.board[self.y][self.left]
      if self.y != self.rows -1:
        self.WS = self.board[self.down][self.left]
      
    
    # More info : https://www.ecured.cu/images/e/ea/Rosa_de_los_vientos123.jpg



class Minesweeper:
  def __init__(self, data_raw):
    self.data = data_raw.split()
    self.data.reverse()
    self.rows = int(self.data.pop(-1))
    self.cols = int(self.data.pop(-1))
    self.data.reverse()

    self.board = self.board()
    self.new_board = self.final_board()

    # Create final board
  def final_board(self):
    new_board = []
    for i in range(self.rows):          # A for loop for row entries
        a =[]
        for j in range(self.cols):      # A for loop for column entries
            if self.board[i][j] == '.':
              a.append(0)
            else:
              a.append("*")
        new_board.append(a)
    return new_board

  # Create data board
  def board(self):
    board = []
    for idx, item in enumerate(self.data):
      new_list = list(item)
      board.append(new_list)
    return board


  def x_analysis(self, row, col):
    # ----------- ROW 0 ----------- 
    # first
    if col == 0 and row == 0:
      self.corner_top_left(row, col)
    # last
    if col == self.cols -1 and row == 0:
      self.corner_top_right(row, col)
    
    # ----------- ROW -1 ----------- 
    if col == self.cols -1 and row == self.rows -1:
      self.corner_bottom_right(row, col)

    if col == 0 and row == self.rows -1:
      self.corner_bottom_left(row, col)

    # ----------- COL -> RIGHT ------------------
    if col == 0 and (row > 0) and (row < self.rows -1):
      self.five_movements_right(row, col)

    # ----------- COL -> LEFT ------------------
    if (col == self.cols -1) and (row > 0) and (row < self.rows -1):
      self.five_movements_left(row, col)
    

    # ---------- CENTER ----------------
    if col != 0 and col != self.cols -1:
      if row == 0:
        self.five_movements_down(row, col)
      elif row == self.rows -1:
        #print("five_movements_top")
        self.five_movements_top(row, col)
      else:
        self.height_movements_circle(row, col)
        
  # ----------------------------------------------------
  # Start the analysis of the corners
  # --------------------- TOP --------------------------  
  def corner_top_left(self, y, x): # position
    c_rose_1 = CompassRose(self.board, self.cols, self.rows, x, y)

    if c_rose_1.E == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

    
    if c_rose_1.SE == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    
    if c_rose_1.S == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    

  def corner_top_right(self, y, x): # análisis hacia la izquierda y abajo
    c_rose_2 = CompassRose(self.board, self.cols, self.rows, x, y)
    if c_rose_2.S == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

    if c_rose_2.WS == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    
    if c_rose_2.W == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

  # --------------------- LEFT - CENTER -------------------------- 
  def five_movements_right(self, y, x):
    
    c_rose_mr = CompassRose(self.board, self.cols, self.rows, x, y)
    if c_rose_mr.N == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_mr.NE == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_mr.E == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_mr.SE == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_mr.S == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1


  # --------------------- RIGHT - CENTER -------------------------- 
  def five_movements_left(self, y, x):
    c_rose_ml = CompassRose(self.board, self.cols, self.rows, x, y)
    if c_rose_ml.S == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_ml.WS == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_ml.W == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_ml.NW == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_ml.N == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

  # --------------------- TOP - CENTER -------------------------- 
  def five_movements_down(self, y, x):
    c_rose_c1 = CompassRose(self.board, self.cols, self.rows, x, y)
    if c_rose_c1.E == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

    if c_rose_c1.SE == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

    if c_rose_c1.S == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    
    if c_rose_c1.WS == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    
    if c_rose_c1.W == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1


  def five_movements_top(self, y, x):
    c_rose_c2 = CompassRose(self.board, self.cols, self.rows, x, y)
    if c_rose_c2.W == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

    if c_rose_c2.NW == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

    if c_rose_c2.N == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

    if c_rose_c2.NE == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

    if c_rose_c2.E == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

  # --------------------- CENTER - CENTER -------------------------- 
  def height_movements_circle(self, y, x):
    c_rose_circle = CompassRose(self.board, self.cols, self.rows, x, y)
    if c_rose_circle.N == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_circle.NE == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_circle.E == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_circle.SE == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_circle.S == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_circle.WS == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_circle.W == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    if c_rose_circle.NW == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

  # --------------------- BOTTOM --------------------------  
  def corner_bottom_left(self, y, x): # position
      c_rose_4 = CompassRose(self.board, self.cols, self.rows, x, y)
      if c_rose_4.N == "*":
        self.new_board[y][x] = self.new_board[y][x] + 1

      if c_rose_4.NE == "*":
        self.new_board[y][x] = self.new_board[y][x] + 1
      
      if c_rose_4.E == "*":
        self.new_board[y][x] = self.new_board[y][x] + 1
  
  def corner_bottom_right(self, y, x): # position
    c_rose_3 = CompassRose(self.board, self.cols, self.rows, x, y)
    if c_rose_3.W == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1

    if c_rose_3.NW == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1
    
    if c_rose_3.N == "*":
      self.new_board[y][x] = self.new_board[y][x] + 1


def main(data_raw):

    minesweeper = Minesweeper(data_raw)

    for row in range(minesweeper.rows):
        if row == 0:
          for col in range(minesweeper.cols):
            # Analysis on X
            #print(minesweeper.new_board)
            minesweeper.x_analysis(row, col)
            #print(f"{row}")

        if row == minesweeper.rows-1:
          for col in range(minesweeper.cols):
            # Analysis on X
            minesweeper.x_analysis(row, col)
            #print(f"{row}")
      
        if row != 0 and row != minesweeper.cols -1:
          for col in range(minesweeper.cols):
          # Analysis on X
            minesweeper.x_analysis(row, col)
          # print(minesweeper.new_board)  
          # pass
    # print the new result
    print(minesweeper.new_board)



import sys

f = open(sys.argv[1],"r")
data_raw = f.read()
f.close()
print(data_raw)

data_raw_hard = """
        4 4
        *...
        ....
        .*..
        ....
"""
main(data_raw)