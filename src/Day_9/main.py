import utils
Day = utils.AdventOfCodeDay(9)
Part_1 = utils.AdventOfCodePart(Day, 1)

class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)

    def main(self, input_data):
        total = 0
        for row in input_data:
            row_list = self.parse_row(row)
            total += self.process_sequence(row_list)
        return total
    
    def parse_row(self, row):
        return list(map(int, row.split()))

    def process_sequence(self, seq):
        if all(x == 0 for x in seq):
            return 0
        return seq[-1] + self.process_sequence(self.calc_diffs(seq))
    
    def calc_diffs(self, seq):
        pairs = zip(seq, seq[1:])
        return [x[1] - x[0] for x in pairs]

Part_1.set_solution(Solution)

class Solution2(Solution):
    def __init__(self):
        super().__init__()
    
    def parse_row(self, row):
        return super().parse_row(row)[::-1]

    
Part_2 = utils.AdventOfCodePart(Day, 2)
Part_2.set_solution(Solution2)

if __name__ == "__main__":
    Part_1.run_display_all()
    Part_2.run_display_all()
    