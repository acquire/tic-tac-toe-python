from cell import Cell

class Board:

    def __init__(self, width):
        self.width = width
        height = width
        size = self.width * height
        self.cells = [] #a list of cells
        self.create_board(size)

    def create_board(self, size):
        count = 0
        while count < size:
            c = Cell(count, count)
            self.cells.append(c)
            count += 1

#b = Board(3)
#print(len(b.cells))
#for c in b.cells:
#    print(str(c.description))
