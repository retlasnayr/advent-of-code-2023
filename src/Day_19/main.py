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

Part_2 = utils.AdventOfCodePart(Day, 2)

class Solution2(utils.AdventOfCodeSolution):
    def __init__(self):
        super().__init__()
        self.workflows = {}
        self.parts = [{category: (1, 4001) for category in ("x", "m", "a", "s")}]
        self.complete_parts = []

    def main(self, input_data):
        self.parse_input(input_data)
        self.iterate_parts()
        return sum(self.part_length(part) for target, part in self.complete_parts if target == "A")
    
    def parse_input(self, input_data):
        for row in input_data:
            if not row:
                break
            name, inst = self.parse_workflow(row)
            self.workflows[name] = [self.parse_instruction(x) for x in inst]

    def parse_workflow(self, row):
        name, data = row[:-1].split("{")
        instructions = data.split(",")
        return name, instructions
    
    def parse_instruction(self, inst):
        if ":" not in inst:
            return None, None, None, inst
        condition, target = inst.split(":")
        category = condition[0]
        comp = condition[1]
        value = int(condition[2:])
        return category, comp, value, target
    
    @staticmethod
    def part_length(part: dict[str, tuple[int, int]]) -> int:
        total = 1
        for category, values in part.items():
            total *= (values[1] - values[0])
        return total
    
    def iterate_parts(self):
        while len(self.parts) > 0:
            new_parts = []
            for part in self.parts:
                new_parts.extend(self.process_part(part))
            self.parts = new_parts

    def process_part(self, part):
        workflow_name = "in"
        while True:
            changed_parts, data = self.apply_workflow_to_part(part, self.workflows[workflow_name])
            if changed_parts:
                return data
            workflow_name = data
            if workflow_name in ("A", "R"):
                break
        self.complete_parts.append([data, part])
        return []

    def apply_workflow_to_part(self, part, workflow):
        for instruction in workflow:
            changed, target = self.apply_instruction_to_part(part, instruction)
            if target is not None:
                return changed, target
        return changed, target

    def apply_instruction_to_part(self, part, inst):
        category, comp, value, target = inst
        if comp == "<":
            if part[category][0] < value < part[category][1]:
                part1 = part | {category: (part[category][0], value)}
                part2 = part | {category: (value, part[category][1])}
                return True, [part1, part2]
        elif comp == ">":
            if part[category][0] <= value < part[category][1] - 1:
                part1 = part | {category: (part[category][0], value+1)}
                part2 = part | {category: (value+1, part[category][1])}
                return True, [part1, part2]
        
        if comp == "<":
            if part[category][1] <= value:
                new_workflow = target
            else: 
                new_workflow = None
        elif comp == ">":
            if part[category][0] > value:
                new_workflow = target
            else:
                new_workflow = None
        else:
            new_workflow = target

        return False, new_workflow





Part_2.set_solution(Solution2)

if __name__ == "__main__":
    Part_1.run_display_all()
    Part_2.run_display_all()
    