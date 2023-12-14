import utils
Day = utils.AdventOfCodeDay(14)
Part_1 = utils.AdventOfCodePart(Day, 1)

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

if __name__ == "__main__":
    Part_1.run_display_all()
    