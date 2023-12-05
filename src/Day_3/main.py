import utils
Day = utils.AdventOfCodeDay(3)
Part_1 = utils.AdventOfCodePart(Day, 1)

class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)
        self.data_grid = []
        self.max_row = None
        self.max_col = None

    def main(self, input_data):
        self.data_grid = [x.replace("\n", "") for x in input_data]
        self.max_row = len(self.data_grid)
        self.max_col = len(self.data_grid[0])
        chars = set()
        nums = [str(x) for x in range(10)]
        for row in self.data_grid:
            for col in row:
                if col not in nums:
                    chars.add(col)
        # return chars
        return self.iterate_data_grid()

    def iterate_data_grid(self):
        current_number = ""
        is_part_number = False
        total_part_nos = 0
        for row_num, row in enumerate(self.data_grid):
            if is_part_number:
                total_part_nos += int(current_number)
                # print(current_number)
            current_number = ""
            is_part_number = False
            for col_num, value in enumerate(row):
                try:
                    int_val = int(value)
                    current_number += value
                    is_part_number = is_part_number or self.check_adjacencies(row_num, col_num)
                    
                except ValueError:
                    if is_part_number:
                        total_part_nos += int(current_number)
                        # print(current_number)

                    current_number = ""
                    is_part_number = False
                    continue
        return total_part_nos

    def check_adjacencies(self, row_num, col_num):
        adjacencies = self.get_adjacencies(row_num, col_num)
        for row, col in adjacencies:
            character = self.data_grid[row][col]
            # if character == ".":
            #     continue
            characters = {'-', '&', '=', '%', '#', '+', '*', '@', '$', '/'}
            if character in characters:
                return True
        return False

    def get_adjacencies(self, row, col):
        adjs = []
        diffs = (-1, 0, 1)
        for r_diff in diffs:
            for c_diff in diffs:
                new_row = row + r_diff
                new_col = col + c_diff
                if (0 <= new_row) and (new_row < self.max_row) and (0 <= new_col) and (new_col < self.max_col):
                    adjs.append((new_row, new_col))
        return adjs

Part_1.set_solution(Solution())

class Solution2(Solution):
    def __init__(self):
        Solution.__init__(self)
    
    def iterate_data_grid(self):
        gears = {}
        current_number = ""
        is_part_number = False
        gear_loc = ()
        for row_num, row in enumerate(self.data_grid):
            if is_part_number:
                if gear_loc not in gears:
                    gears[gear_loc] = []
                gears[gear_loc].append(int(current_number))
                # print(current_number)
            current_number = ""
            is_part_number = False
            gear_loc = ()
            for col_num, value in enumerate(row):
                try:
                    int_val = int(value)
                    current_number += value
                    curr_is_part_number, curr_gear_loc = self.check_adjacencies(row_num, col_num)
                    gear_loc = gear_loc if gear_loc else curr_gear_loc
                    is_part_number = is_part_number or curr_is_part_number
                    
                except ValueError:
                    if is_part_number:
                        if gear_loc not in gears:
                            gears[gear_loc] = []
                        gears[gear_loc].append(int(current_number))
                        # print(current_number)
                    current_number = ""
                    is_part_number = False
                    gear_loc = ()
                    continue
        double_gears = [x for x in gears.values() if len(x) == 2]
        return sum(x * y for x, y in double_gears)

    def check_adjacencies(self, row_num, col_num):
        adjacencies = self.get_adjacencies(row_num, col_num)
        for row, col in adjacencies:
            character = self.data_grid[row][col]
            if character == "*":
                return True, (row, col)
        return False, ()

Part_2 = utils.AdventOfCodePart(Day, 2)
Part_2.set_solution(Solution2())

if __name__ == "__main__":
    
    Part_1.run_display_all()
    Part_2.run_display_all()


    