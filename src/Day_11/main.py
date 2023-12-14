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


Part_2 = utils.AdventOfCodePart(Day, 2)

class Solution2(Solution):
    MULTIPLIER = 1_000_000 - 1
    def __init__(self):
        super().__init__()
        self.expansion_rows = []
        self.expansion_columns = []

    def main(self, input_data):
        self.get_expansion_data(input_data)
        self.universe_data = input_data
        self.parse_in_galaxies()
        self.pair_galaxies()
        total = 0
        for gp in self.galaxy_pairs:
            total += self.distance(gp)
        return total


    def get_expansion_data(self, data):
        self.expansion_rows = self.get_expansion_rows(data)
        self.expansion_columns = self.get_expansion_rows(list(map(list, zip(*data))))

    def get_expansion_rows(self, data):
        exp_rows = []
        for index, row in enumerate(data):
            if all(x=="." for x in row):
                exp_rows.append(index)
        return exp_rows
    
    def distance(self, pair):
        g1, g2 = pair
        min_x = min(g1[0], g2[0])
        max_x = max(g1[0], g2[0])
        min_y = min(g1[1], g2[1])
        max_y = max(g1[1], g2[1])
        count = 0
        for index in range(min_x, max_x):
            if index in self.expansion_rows:
                count += 1
        for index in range(min_y, max_y):
            if index in self.expansion_columns:
                count += 1
        return max_x + max_y - min_x - min_y + count * self.MULTIPLIER
    
Part_2.set_solution(Solution2)

if __name__ == "__main__":
    Part_1.run_display_all()
    Part_2.run_display_all()