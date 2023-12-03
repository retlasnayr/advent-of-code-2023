import pathlib
class AdventOfCodeSolution:
    def __init__(self):
        self.result = None

    def run(self, input_data):
        self.result = self.main(self, input_data)

    def main(self, input_data):
        return None

    def solution(self):
        return self.result
    

class AdventOfCodeDay:
    def __init__(self, day_number):
        self.day_number = day_number


class AdventOfCodePart:
    def __init__(self, day: AdventOfCodeDay, part_number: int):
        self.day = day
        self.part_number = part_number
        self.input_example, self.input_real = self.load_inputs()
        self._solution = None
        self.result_example = None
        self.result_real = None

    @staticmethod
    def read_input(day, part, real = True):
        file_name = pathlib.Path(f"Day_{day}", f"input_part_{part}_{'real' if real else 'example'}.txt")
        # file_dir = pathlib.Path(__file__).parent.resolve()
        file_dir = pathlib.Path(pathlib.Path().resolve(), "inputs")
        with open(pathlib.Path(file_dir, file_name), encoding="UTF-8") as f:
            contents = f.readlines()
        return contents

    def load_inputs(self):
        part = self.part_number
        day = self.day.day_number
        example, real = self.read_input(day, part, False), self.read_input(day, part, True)
        if not (example and real):
            # If part 2 files are empty, reuse part 1
            example, real = self.read_input(day, 1, False), self.read_input(day, 1, True)
        return example, real

    def input_data(self, real):
        return self.input_real if real else self.input_example
    
    def set_solution(self, solution: AdventOfCodeSolution):
        self._solution = solution
        return self._solution

    def run_example(self):
        self._solution.run(self._solution, self.input_example)
        self.result_example = self._solution.result

    def run_real(self):
        self._solution.run(self._solution, self.input_real)
        self.result_real = self._solution.result

    def display_example(self):
        print(f"Example: {self.result_example}")
        
    def display_real(self):
        print(f"Real:    {self.result_real}")

    def display_results(self):
        self.display_example()
        self.display_real()

    def run_display_all(self):
        self.run_example()
        self.run_real()
        self.display_results()
        