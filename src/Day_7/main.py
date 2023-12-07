import utils
Day = utils.AdventOfCodeDay(7)
Part_1 = utils.AdventOfCodePart(Day, 1)

CARD_ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARD_ORDER2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

class CamelCardsHand():
    def __init__(self, raw_hand, card_order=CARD_ORDER):
        if type(raw_hand) != str:
            raise TypeError("Invalid raw_hand type")
        if len(raw_hand) != 5:
            raise ValueError("Invalid raw_hand length")
        self._raw_hand = raw_hand
        self._card_counts = {}
        self._hand_type = None
        self._card_order = card_order
        
        for ch in raw_hand:
            if ch not in self._card_counts:
                self._card_counts[ch] = 0
            self._card_counts[ch] += 1
        self.set_hand_type()
    

    def set_hand_type(self):
        hand_dict = self._card_counts
        if len(hand_dict) == 1:
            hand_rank = 1  # 5 of a kind
        elif len(hand_dict) == 2:
            if max(hand_dict.values()) == 4:
                hand_rank = 2  # 4 of a kind
            else:
                hand_rank = 3  # Full house
        elif len(hand_dict) == 3:
            if max(hand_dict.values()) == 3:
                hand_rank = 4  # 3 of a kind
            else:
                hand_rank = 5  # 2 pair
        elif len(hand_dict) == 4:
            hand_rank = 6  # 1 pair
        else:
            hand_rank = 7  # high card
        self._hand_type = hand_rank

    def __eq__(self, other):
        if not isinstance(other, CamelCardsHand):
            return False
        return self._raw_hand == other._raw_hand
    def __lt__(self, other):
        if not isinstance(other, CamelCardsHand):
            raise TypeError
        if self._hand_type != other._hand_type:
            return self._hand_type > other._hand_type
        return self.worse_of_equal_type_hands(self._raw_hand, other._raw_hand)
    def __repr__(self):
        return f"{self._raw_hand}: {self._hand_type}"
    def __contains__(self, value):
        return value in self._raw_hand
    
    def card_counts(self):
        return self._card_counts

    def worse_of_equal_type_hands(self, hand1, hand2):
        for c1, c2 in zip(hand1, hand2):
            if c1 == c2:
                continue
            return self._card_order.index(c1) > self._card_order.index(c2)
        return True
        raise ValueError(f"{hand1} and {hand2} are equal so cannot be compared")

class Solution(utils.AdventOfCodeSolution):

    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)
        self.num_hands = None
        self.hands = []

    def main(self, input_data):
        self.iterate_hands(input_data)
        return self.score_hands()

    def iterate_hands(self, input_data):
        self.num_hands = len(input_data)
        for row in input_data:
            self.hands.append(self.parse_row(row))
        self.hands.sort(key=lambda x: x[0])

    def score_hands(self):
        total_score = 0
        for index, (hand, bid) in enumerate(self.hands):
            # print(f"{index:4}, {hand}, {bid}")
            total_score += (index + 1) * bid
        return total_score

    def parse_row(self, row):
        hand, bid = row.split()
        return CamelCardsHand(hand), int(bid)

class CamelCardsHandWithJokers(CamelCardsHand):
    def __init__(self, raw_hand, card_order=CARD_ORDER2):
        super().__init__(raw_hand, card_order)
        self._possible_hands = []
        self._best_hand = None
        self._best_hand_type = None
        self.parse_jokers(self._raw_hand)
        


    def parse_jokers(self, hand):
        orig_hand = CamelCardsHand(hand)
        for card in orig_hand.card_counts():
            self._possible_hands.append(CamelCardsHand(hand.replace('J', card)))
        self._possible_hands.sort()
        self._best_hand = self._possible_hands[-1]
        self._best_hand_type = self._best_hand._hand_type
    
    def __lt__(self, other):
        if not isinstance(other, CamelCardsHandWithJokers):
            if isinstance(other, CamelCardsHand):
                if self._best_hand_type != other._hand_type:
                    return self._best_hand_type > other._hand_type
                return self.worse_of_equal_type_hands(self._raw_hand, other._raw_hand)
            raise TypeError
        if self._best_hand_type != other._best_hand_type:
            return self._best_hand_type > other._best_hand_type
        return self.worse_of_equal_type_hands(self._raw_hand, other._raw_hand)



class Solution2(Solution):
    def __init__(self):
        super().__init__()
    
    def parse_row(self, row):
        hand, bid = row.split()
        return CamelCardsHandWithJokers(hand), int(bid)

        

Part_1.set_solution(Solution)

Part_2 = utils.AdventOfCodePart(Day, 2)
Part_2.set_solution(Solution2)

if __name__ == "__main__":
    Part_1.run_display_all()
    Part_2.run_display_all()
