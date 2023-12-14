import utils
Day = utils.AdventOfCodeDay(11)
Part_1 = utils.AdventOfCodePart(Day, 1)


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
        for index, galaxy in enumerate(self.galaxies):
            for galaxy2 in self.galaxies[index+1:]:
                self.galaxy_pairs.append((galaxy, galaxy2))
                

    def distance(self, pair):
        row_diff = abs(pair[0][0] - pair[1][0])
        col_diff = abs(pair[0][1] - pair[1][1])
        return row_diff + col_diff


Part_1.set_solution(Solution)

if __name__ == "__main__":
    Part_1.run_display_all()
    