from cell import Cell

class Board:

    def __init__(self, width):
        self.width = width
        height = width
        size = self.width * height
        self.cells = [] #a list of cells
        self.__create_board(size)

    def __create_board(self, size):
        count = 0
        while count < size:
            c = Cell(count, count)
            self.cells.append(c)
            count += 1

    def console_print(self):
        b = self.cells
        print(" {} | {} | {}".format(b[0],b[1],b[2]))
        print("===+===+===")
        print(" {} | {} | {}".format(b[3],b[4],b[5]))
        print("===+===+===")
        print(" {} | {} | {}".format(b[6],b[7],b[8]))

#b = Board(3)
#print(len(b.cells))
#for c in b.cells:
#    print(str(c.description))
