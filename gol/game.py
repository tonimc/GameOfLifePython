import time

class World:

    def __init__(self):
        self.cells = []

    def init_cells(self, cells):
        self.cells = cells

    def next_generation(self):
        next_gen = []
        for cell in self.get_freq().items():
            if (cell[1]==3 or
                (cell[1]==2 and 
                    self.cells.count(Cell(cell[0][0], cell[0][1])))==1):
                next_gen.append(Cell(cell[0][0], cell[0][1]))
        return next_gen

    def get_freq(self):
        freq = {}
        for cell in self.cells:
            for neighbor in cell.get_neighbors():
                key = (neighbor.x, neighbor.y)
                freq[key] = 1 if (not freq.has_key(key)) else (freq[key]+1)
        return freq

    def __str__(self):
        to_ret = '[ '
        for cell in self.cells:
            to_ret += cell.__str__()
        return to_ret + ' ]'

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_neighbors(self):
        return (Cell(self.x-1,self.y+1), Cell(self.x,self.y+1), Cell(self.x+1,self.y+1),
                Cell(self.x-1,self.y), Cell(self.x+1,self.y),
                Cell(self.x-1,self.y-1), Cell(self.x,self.y-1), Cell(self.x+1,self.y-1))

    def __cmp__(self, other):
        if(self.x==other.x and self.y==other.y):
            return 0
        else:
            return -1

    def __str__(self):
        return " Cell(" + str(self.x) + "," + str(self.y) + ") "

class Printer:
    def __init__(self, world):
        self.world = world

    def _get_min_max(self):
        min = 9999
        max = -9999
        for cell in self.world.cells:
            min = cell.x if (cell.x < min) else min
            min = cell.y if (cell.y < min) else min
            max = cell.x if (cell.x > max) else max
            max = cell.y if (cell.y > max) else max
        return (min,max) 

    def print_world(self):
        m = (0,40)
        w = ''
        for y in range(m[0],m[1]+1):
            w +=  "|"
            for x in range(m[0],m[1]+1):
                w += ('X' if (self.world.cells.count(Cell(x,y))==1) else ' ')+'|'
            w +=  "\n"
        print w

if __name__ == '__main__':
    tablero = World()
    tablero.init_cells([Cell(1,0), Cell(3,4), Cell(4,3), Cell(2,3), Cell(1,2), Cell(2,2), Cell(3,2)])
    """
    tablero.init_cells([Cell(24,0),
                        Cell(22,1), Cell(24,1),
                        Cell(12,2), Cell(13,2),Cell(20,2), Cell(21,2),Cell(34,2), Cell(35,2),
                        Cell(11,3), Cell(15,3),Cell(20,3), Cell(21,3),Cell(34,3), Cell(35,3),
                        Cell(0,4), Cell(1,4),Cell(10,4), Cell(16,4),Cell(20,4), Cell(21,4),
                        Cell(0,5), Cell(1,5),Cell(10,5), Cell(14,5),Cell(16,5), Cell(17,5),Cell(22,5), Cell(24,5),
                        Cell(10,6), Cell(16,6),Cell(24,6),
                        Cell(11,7), Cell(15,7),
                        Cell(12,8), Cell(13,8)])
    """
    Printer(tablero).print_world()

    for i in range(1,1000):
        tablero.cells = tablero.next_generation()
        Printer(tablero).print_world()
    
