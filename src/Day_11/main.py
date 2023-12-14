import utils
Day = utils.AdventOfCodeDay(11)
Part_1 = utils.AdventOfCodePart(Day, 1)


class Pair:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def __eq__(self, other):
        if not isinstance(other, Pair):
            raise TypeError
        return (self.x1 == other.x1 and self.x2 == other.x2) or (self.x1 == other.x2 and self.x2 == other.x1)
    
class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)
        self.universe_data = None
        self.galaxies = []
        self.galaxy_pairs = []

    def main(self, input_data):
        self.universe_data = self.expand_universe(input_data)
        self.parse_in_galaxies()
        self.pair_galaxies()
        total = 0
        for gp in self.galaxy_pairs:
            total += self.distance(gp)
        return total


    def expand_universe(self, data):
        new_data = self.expand_rows(data)
        transposed_data = list(map(list, zip(*new_data)))
        new_data = self.expand_rows(transposed_data)
        return list(map(list, zip(*new_data)))
    
    def expand_rows(self, data):
        new_data = []
        for row in data:
            new_data.append(row)
            if all(x=="." for x in row):
                new_data.append(row)
        return new_data
    
    def parse_in_galaxies(self):
        for row_num, row in enumerate(self.universe_data):
            for col_num, col in enumerate(row):
                if col == "#":
                    self.galaxies.append((row_num, col_num))
    
    def pair_galaxies(self):
        for galaxy in self.galaxies:
            for galaxy2 in self.galaxies:
                if galaxy != galaxy2:
                    pair = Pair(galaxy, galaxy2)
                    if pair not in self.galaxy_pairs:
                        self.galaxy_pairs.append(pair)

    def distance(self, pair):
        row_diff = abs(pair.x1[0] - pair.x2[0])
        col_diff = abs(pair.x1[1] - pair.x2[1])
        return row_diff + col_diff


Part_1.set_solution(Solution)

if __name__ == "__main__":
    Part_1.run_display_all()
    