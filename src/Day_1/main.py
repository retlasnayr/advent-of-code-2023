import utils
Day = utils.AdventOfCodeDay(1)
Part_1 = utils.AdventOfCodePart(Day, 1)

class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)

    def main(self, input_data):
        total = 0
        for row in input_data:
            total += self.process_row(row)
        return total

    @staticmethod
    def process_row(row):
        nums = []
        for character in row:
            try:
                num = int(character)
            except ValueError:
                continue
            nums.append(num)
        return int(f"{nums[0]}{nums[-1]}")

Part_1.set_solution(Solution)

Part_2 = utils.AdventOfCodePart(Day, 2)
class Solution2(Solution):
    def __init__(self):
        Solution.__init__(self)
    
    @staticmethod
    def process_row(row):
        num_words = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
        nums = []
        for index, character in enumerate(row):
            try:
                nums.append(int(character))
            except ValueError:
                for word, value in num_words.items():
                    try:
                        if row[index:index+len(word)] == word:
                            nums.append(value)
                    except IndexError:
                        continue
        return int(f"{nums[0]}{nums[-1]}")
Part_2.set_solution(Solution2)

if __name__ == "__main__":
    
    Part_1.run_example()
    Part_1.display_example()
    Part_1.run_real()
    Part_1.display_real()

    Part_2.run_example()
    Part_2.run_real()
    Part_2.display_results()
    