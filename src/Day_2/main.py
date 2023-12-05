import utils
Day = utils.AdventOfCodeDay(2)
Part_1 = utils.AdventOfCodePart(Day, 1)

class Solution(utils.AdventOfCodeSolution):
    limits = {"red": 12, "green": 13, "blue": 14}
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)

    def main(self, input_data):
        id_sum = 0
        for row in input_data:
            id_sum += self.process_raw_row(row)
        return id_sum
    
    def process_raw_row(self, raw_row):
        game, data = raw_row.split(":")
        game_num = int(game[5:])
        hands = data.split(";")
        if all(self.process_hand(hand) for hand in hands):
            return game_num
        return 0
    
    def process_hand(self, hand):
        colours = hand.split(",")
        for item in colours:
            item = item.strip()
            num, col = item.split(" ")
            if int(num) > self.limits[col]:
                return False
        return True

Part_1.set_solution(Solution())

class Solution2(Solution):
    def __init__(self):
        Solution.__init__(self)
    
    def process_raw_row(self, raw_row):
        col_data = {"red":0, "green":0, "blue":0}
        _, data = raw_row.split(":")
        hands = data.split(";")
        for hand in hands:
            min_vals = self.process_hand(hand)
            col_data = self.update_dict(min_vals, col_data)
        return col_data["red"] * col_data["green"] * col_data["blue"]

    @staticmethod
    def update_dict(d1, d2):
        for key, val in d1.items():
            if d2[key] < val:
                d2[key] = val
        return d2
    
    def process_hand(self, hand):
        cols_dict = {}
        colours = hand.split(",")
        for item in colours:
            item = item.strip()
            num, col = item.split(" ")
            cols_dict[col] = int(num)
        return cols_dict

Part_2 = utils.AdventOfCodePart(Day, 2)
Part_2.set_solution(Solution2())


if __name__ == "__main__":
    
    Part_1.run_display_all()
    Part_2.run_display_all()
    