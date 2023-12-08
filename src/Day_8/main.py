import utils, math
Day = utils.AdventOfCodeDay(8)
Part_1 = utils.AdventOfCodePart(Day, 1)

class Solution(utils.AdventOfCodeSolution):
    def __init__(self, starting_node = "AAA"):
        utils.AdventOfCodeSolution.__init__(self)
        self.instructions = ""
        self.instruction_index = -1
        self.nodes = {}
        self.starting_node = starting_node

    def main(self, input_data):
        self.parse_input(input_data)
        return self.iterate_instructions()

    def parse_input(self, input_data):
        self.instructions = input_data[0]
        for row in input_data[2:]:
            node_name, l, r = self.parse_row(row)
            self.nodes[node_name] = l, r

    def parse_row(self, row):
        node, data = row.split(" = ")
        left, right = data.split(",")
        return node, left.strip(" ()"), right.strip(" ()")
    
    def next_instruction(self):
        self.instruction_index += 1
        if self.instruction_index == len(self.instructions):
            self.instruction_index = 0
        return 0 if self.instructions[self.instruction_index] == "L" else 1
    
    def next_node(self, node, instruction):
        return self.nodes[node][instruction]

    def iterate_instructions(self, starting_node = "AAA"):
        current_node = starting_node
        steps = 0
        while current_node != "ZZZ":
            current_node = self.next_node(current_node, self.next_instruction())
            steps += 1
        return steps
    
Part_1.set_solution(Solution)

class Solution2(Solution):
    def __init__(self):
        super().__init__()
    
    def main(self, input_data):
        self.parse_input(input_data)
        starting_nodes = [node for node in self.nodes if node[-1] == "A"]
        node_lengths = {}
        for node in starting_nodes:
            node_lengths[node] = self.iterate_instructions(node)
        return math.lcm(*list(node_lengths.values()))

    def iterate_instructions(self, starting_node = "AAA"):
        current_node = starting_node
        steps = 0
        while current_node[-1] != "Z":
            current_node = self.next_node(current_node, self.next_instruction())
            steps += 1
        return steps

Part_2 = utils.AdventOfCodePart(Day, 2)
Part_2.set_solution(Solution2)

if __name__ == "__main__":
    Part_1.run_display_all()
    Part_2.run_display_all()
