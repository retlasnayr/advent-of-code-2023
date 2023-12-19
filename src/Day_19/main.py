import utils
Day = utils.AdventOfCodeDay(19)
Part_1 = utils.AdventOfCodePart(Day, 1)

class Workflow:
    def __init__(self, raw_string):
        self.name, self.instructions = self.parse_string(raw_string)


    def parse_string(self, string):
        wf_name, instructions = string[:-1].split("{")
        instructions = instructions.split(",")
        return wf_name, [self.parse_instruction(x) for x in instructions]

    def parse_instruction(self, inst):
        if ":" in inst:
            instruction, target = inst.split(":")
        else:
            return lambda x: inst
        
        if "<" in instruction:
            cat, val = instruction.split("<")
            return lambda x: target if x[cat] < int(val) else None
        cat, val = instruction.split(">")
        return lambda x: target if x[cat] > int(val) else None

    def run_workflow(self, part):
        for instruction in self.instructions:
            target = instruction(part)
            if target is not None:
                return target
        

class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)
        self.workflows = {}
        self.parts = []

    def main(self, input_data):
        self.parse_input(input_data)
        return self.iterate_parts()

    def iterate_parts(self):
        total = 0
        for part in self.parts:
            total += self.process_part(part)
        return total
    
    def parse_input(self, input_data):
        parts = False
        for row in input_data:
            if not row:
                parts = True
                continue
            if not parts:
                new_workflow = Workflow(row)
                self.workflows[new_workflow.name] = new_workflow
                continue
            self.parts.append(self.parse_part(row))

    def parse_part(self, part):
        part_dict = {
            category.split("=")[0]: int(category.split("=")[1])   
            for category in part[1:-1].split(",")
        }
        return part_dict
    
    def process_part(self, part):
        workflow: Workflow = self.workflows["in"]
        while True:
            result = workflow.run_workflow(part)
            if result == "A":
                return self.part_score(part)
            if result == "R":
                return 0
            workflow = self.workflows[result]

    def part_score(self, part):
        return sum(part.values())

Part_1.set_solution(Solution)

if __name__ == "__main__":
    Part_1.run_display_all()
    