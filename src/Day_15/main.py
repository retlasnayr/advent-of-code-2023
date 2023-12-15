import utils
Day = utils.AdventOfCodeDay(15)
Part_1 = utils.AdventOfCodePart(Day, 1)

class HASH:
    def __init__(self, string):
        self.raw_string = string
        self.hash_value = 0
        self.hash_string()

    def hash_string(self):
        for character in self.raw_string:
            self.hash_character(character)

    def hash_character(self, character):
        self.hash_value += ord(character)
        self.hash_value *= 17
        self.hash_value = self.hash_value % 256

class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)
        self.steps = []

    def main(self, input_data):
        init_seq = self.parse_input(input_data[0])
        total = 0
        for step in init_seq:
            val = self.hash_string(step)
            self.steps.append((step, val))
            total += val
        return total

    
    def parse_input(self, data):
        return data.split(",")

    def hash_string(self, string):
        return HASH(string).hash_value

Part_1.set_solution(Solution)
class Lens:
    def __init__(self, label: str, focal_length: int = None):
        self.label = label
        self.focal_length = None if focal_length is None else int(focal_length)
        self.box_number = HASH(label).hash_value

    def __eq__(self, other):
        if isinstance(other, str):
            return self.label == other
        return self.label == other.label and self.focal_length == other.focal_length

class Box:
    def __init__(self, box_number):
        self.lenses = []
        self.box_number = box_number

    def remove_lens(self, label):
        if label in self.lenses:
            self.lenses.remove(label)
    
    def replace_lens(self, lens: Lens):
        if lens.label in self.lenses:
            index = self.lenses.index(lens.label)
            self.lenses[index] = lens
        else:
            self.lenses.append(lens)

    def focusing_power(self):
        bn_power = self.box_number + 1
        lens_powers = 0
        for index, lens in enumerate(self.lenses):
            lens_powers += (index + 1) * lens.focal_length
        return bn_power * lens_powers
            


class Boxes:
    def __init__(self):
        self._boxes: dict[int, Box] = {}
    
    def get_box(self, box_number):
        if box_number not in self._boxes:
            self.add_box(box_number)
        return self._boxes[box_number]

    def add_box(self, box_number):
        if box_number not in self._boxes:
            self._boxes[box_number] = Box(box_number)


    def remove_lens(self, lens_label):
        box_no = Lens(lens_label).box_number
        self.get_box(box_no).remove_lens(lens_label)

    def replace_lens(self, lens_label, focal_length):
        lens = Lens(lens_label, focal_length)
        self.get_box(lens.box_number).replace_lens(lens)

    def focusing_power(self):
        total_fp = 0
        for _, box in self._boxes.items():
            total_fp += box.focusing_power()
        return total_fp

Part_2 = utils.AdventOfCodePart(Day, 2)

class Solution2(Solution):
    def __init__(self):
        super().__init__()
        self.boxes = Boxes()

    def main(self, input_data):
        init_seq = self.parse_input(input_data[0])
        for step in init_seq:
            self.process_step(step)
        return self.boxes.focusing_power()


    def process_step(self, step):
        if "-" in step:
            self.boxes.remove_lens(step.split("-")[0])
        elif "=" in step:
            label, focal_length = step.split("=")
            self.boxes.replace_lens(label, focal_length)

Part_2.set_solution(Solution2)

if __name__ == "__main__":
    Part_1.run_display_all()
    Part_2.run_display_all()
    