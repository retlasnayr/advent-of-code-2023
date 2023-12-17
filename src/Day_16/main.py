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

    def __repr__(self) -> str:
        return "#" if self.energized else "."

class Beam:
    def __init__(self, direction = Pair(1, 0), location = Pair(0, 0)):
        self.direction = direction
        self.location = location
        self.path = []

    def encounter_cell(self, cell: Cell):
        if (self.location, self.direction) in self.path:
            return []
        self.path.append((self.location, self.direction))
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
        self.path = []

    def main(self, input_data):
        self.parse_input(input_data)
        self.iterate()
        self.display_energized()
        return self.total_energized_cells()
    
    def total_energized_cells(self):
        return sum(sum(x.energized for x in row) for row in self.datagrid)

    def parse_input(self, input_data):
        self.datagrid = []
        for row in input_data:
            self.datagrid.append([Cell(x) for x in row])

    def iterate(self):
        while len(self.beams) > 0:
            current_beam = self.beams.pop(0)
            if self.outside_grid(current_beam.location) or self.already_visited(current_beam):
                # self.beams.pop(0)
                continue
            self.path.append((current_beam.location, current_beam.direction))
            beam_location_cell = self.datagrid[current_beam.location.y][current_beam.location.x]
            self.beams.extend(current_beam.encounter_cell(beam_location_cell))
            # self.display_energized()
            continue
        
            
    def outside_grid(self, location):
        return location.x < 0 or location.x >= len(self.datagrid) or location.y < 0 or location.y >= len(self.datagrid[0])
    
    def already_visited(self, beam):
        return (beam.location, beam.direction) in self.path
        

    def display_energized(self):
        print("\n")
        for row in self.datagrid:
            print("".join(str(x) for x in row))


class Solution2(Solution):
    def __init__(self):
        self.num_rows = None
        self.num_cols = None
        self.max_energized = 0

    def main(self, input_data):
        self.parse_input(input_data)
        num_rows = len(self.datagrid)
        num_cols = len(self.datagrid[0])
        # self.run_full_iteration(Pair(3, 0), Pair(0, 1))
        for col in range(num_cols):
            print(f"Column {col}")
            self.run_full_iteration(Pair(col, 0), Pair(0, 1))
            self.run_full_iteration(Pair(col, num_rows - 1), Pair(0, -1))
        for row in range(num_rows):
            print(f"Row {row}")
            self.run_full_iteration(Pair(0, row), Pair(1, 0))
            self.run_full_iteration(Pair(num_cols - 1, row), Pair(-1, 0))
        return self.max_energized

    def run_full_iteration(self, location, direction):
        self.reset_datagrid()
        self.beams = [Beam(direction, location)]
        self.path = []
        self.iterate()
        # self.display_energized()
        if self.total_energized_cells() > self.max_energized:
            self.max_energized = self.total_energized_cells()

    def reset_datagrid(self):
        for row in self.datagrid:
            for cell in row:
                cell.energized = False

Part_1.set_solution(Solution)

Part_2 = utils.AdventOfCodePart(Day, 2)
Part_2.set_solution(Solution2)

if __name__ == "__main__":
    # Part_1.run_display_all()
    Part_2.run_display_all()
    