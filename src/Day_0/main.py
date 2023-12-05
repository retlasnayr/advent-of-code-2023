import utils

Day = utils.AdventOfCodeDay(0)
Part_1 = utils.AdventOfCodePart(Day, 1)

class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)

    def main(self, input_data):
        return input_data



Part_1.set_solution(Solution())

if __name__ == "__main__":
    
    Part_1.run_example()
    Part_1.display_example()
    Part_1.run_real()
    Part_1.display_real()
