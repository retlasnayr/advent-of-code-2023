import utils, copy
Day = utils.AdventOfCodeDay(14)
Part_1 = utils.AdventOfCodePart(Day, 1)

class DataGrid:
    def __init__(self, data):
        self.data = data
    
    def __hash__(self) -> int:
        return(hash(tuple(tuple(x) for x in self.data)))
    
    def __eq__(self, other):
        return self.data == other.data


class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)
        self.data = []

    def main(self, input_data):
        self.store_input(input_data)
        self.roll_north()
        return self.total_load()
    
    def store_input(self, input_data):
        self.data = [[x for x in row] for row in input_data]
        self.data.insert(0, ["#" for _ in self.data[0]])

    def roll_north(self):
        for row_num, row in enumerate(self.data):
            for col_num, character in enumerate(row):
                if character == "O":  # Round rock
                    for index in range(row_num-1, -1, -1):
                        if self.data[index][col_num] != ".":
                            self.data[row_num][col_num] = "."
                            self.data[index+1][col_num] = 'O'
                            break

        # print("\n".join("".join(row) for row in self.data))

    def total_load(self):
        load = 0
        for row_num, row in enumerate(self.data):
            for rock in row:
                if rock == "O":
                    load += self.rock_load(row_num)
        return load

    def rock_load(self, row):
        return len(self.data) - row 
Part_1.set_solution(Solution)

Part_2 = utils.AdventOfCodePart(Day, 2)

class Solution2(Solution):
    def __init__(self):
        super().__init__()

    def main(self, input_data):
        self.store_input(input_data)
        self.store_input(self.rotate_data())
        self.store_input(self.rotate_data())
        self.store_input(self.rotate_data())
        self.rotate_data()
        # print(self.display_grid(self.data))
        prev = [copy.deepcopy(self.data)]
        cycles_to_run = 1000000000
        for _ in range(cycles_to_run):
            prev.append(copy.deepcopy(self.data))
            self.run_cycle()
            # print(self.display_grid(self.data))
            if self.data in prev:
                repeat_length = len(prev) - prev.index(self.data)
                cycles_remaining = cycles_to_run - len(prev)
                remainder = cycles_remaining % repeat_length
                break
        for _ in range(remainder + 1):
            self.run_cycle()
        return self.total_load()

        # print(self.data)
        # print(self.rotate_data())
        # self.roll_north()
        # return self.total_load()

    def run_cycle(self):
        for _ in range(4):
            self.roll_north()
            self.rotate_data()

    def rotate_data(self):
        new_data = [[] for _ in self.data[0]]
        for row in self.data[::-1]:
            for index, col in enumerate(row):
                new_data[index].append(col)
        self.data = new_data
        return new_data
    
    @staticmethod
    def display_grid(grid):
        return "\n".join("".join(row) for row in grid)

    @staticmethod
    def grid_diff(g1, g2):
        for row, (r1, r2) in enumerate(zip(g1, g2)):
            for col, (c1, c2) in enumerate(zip(r1, r2)):
                if c1 != c2:
                    print(row, col, c1, c2)

    def rock_load(self, row):
        return len(self.data) - row - 1  # ignore the extra row of #s at the bottom
    
Part_2.set_solution(Solution2)

if __name__ == "__main__":
    Part_1.run_display_all()
    Part_2.run_display_all()
    