import utils
Day = utils.AdventOfCodeDay(16)
Part_1 = utils.AdventOfCodePart(Day, 1)

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if not isinstance(other, Pair):
            return False
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return Pair(self.x + other.x, self.y + other.y)

class Cell:
    def __init__(self, character) -> None:
        self.character = character
        self.energized = False

class Beam:
    def __init__(self, direction = Pair(1, 0), location = Pair(0, 0)):
        self.direction = direction
        self.location = location

    def encounter_cell(self, cell: Cell):
        cell.energized = True
        if cell.character == ".":
            pass
        elif cell.character == "|":
            if self.direction.x == 0:
                pass
            else:
                return Beam(Pair(0, 1), self.location), Beam(Pair(0, -1), self.location)
        elif cell.character == "-":
            if self.direction.y == 0:
                pass
            else:
                return Beam(Pair(1, 0), self.location), Beam(Pair(-1, 0), self.location)
        elif cell.character == "\\":
            if self.direction.y == 0:
                self.direction = Pair(0, self.direction.x)
            else:
                self.direction = Pair(self.direction.y, 0)
        elif cell.character == "/":
            if self.direction.y == 0:
                self.direction = Pair(0, -self.direction.x)
            else:
                self.direction = Pair(-self.direction.y, 0)

        self.location += self.direction
        return [self]
            

class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)
        self.datagrid = []
        self.beams = [Beam()]

    def main(self, input_data):
        self.parse_input(input_data)
        self.iterate()
        return sum(sum(x.energized for x in row) for row in self.datagrid)
    
    def parse_input(self, input_data):
        for row in input_data:
            self.datagrid.append([Cell(x) for x in row])

    def iterate(self):
        while len(self.beams) > 0:
            current_beam = self.beams.pop(0)
            if self.outside_grid(current_beam.location):
                # self.beams.pop(0)
                continue
            beam_location_cell = self.datagrid[current_beam.location.x][current_beam.location.y]
            self.beams.extend(current_beam.encounter_cell(beam_location_cell))
        
            
    def outside_grid(self, location):
        return location.x < 0 or location.x >= len(self.datagrid[0]) or location.y < 0 or location.y >= len(self.datagrid)



Part_1.set_solution(Solution)

if __name__ == "__main__":
    Part_1.run_display_all()
    