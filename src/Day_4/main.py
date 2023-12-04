import utils
Day = utils.AdventOfCodeDay(4)
Part_1 = utils.AdventOfCodePart(Day, 1)

class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)

    def main(self, input_data):
        total_score = 0
        for row in input_data:
            card_no, w, e = self.parse_row(self, row)
            total_score += self.score_row(self, w, e)
        return total_score
    
    def parse_row(self, raw_row):
        card_no, nums = raw_row.split(":")
        card_no = int(card_no.split(" ")[-1])
        winning_nums, elf_nums = nums.split("|")
        winning_nums = winning_nums.split(" ")
        elf_nums = elf_nums.split(" ")

        return card_no, self.remove_spaces(winning_nums), self.remove_spaces(elf_nums)
    
    @staticmethod
    def remove_spaces(l):
        return [x for x in l if x != ""]
    
    def score_row(self, winning_nums, elf_nums):
        matches = self.count_matches(self, winning_nums, elf_nums)
        score = 2**matches
        return score

    def count_matches(self, winning_nums, elf_nums):
        count = 0
        for num in elf_nums:
            if num in winning_nums:
                count += 1
        return count

Part_1.set_solution(Solution)

Part_2 = utils.AdventOfCodePart(Day, 2)

class Solution2(Solution):
    def __init__(self):
        Solution.__init__(self)

    def main(self, input_data):
        cards = {}
        for row in input_data:
            card_no, w, e = self.parse_row(self, row)
            cards[card_no] = {"matches": self.count_matches(self, w, e), "copies": 1}
        return self.process_cards(self, cards)
    
    def process_cards(self, cards):
        for card_no, data in cards.items():
            for i in range(data["matches"]):
                cards[card_no + i + 1]["copies"] += data["copies"]
        return sum(x["copies"] for x in cards.values())

Part_2.set_solution(Solution2)

if __name__ == "__main__":
    
    Part_1.run_display_all()
    Part_2.run_display_all()
    