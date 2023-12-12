import sys, os
from pathlib import Path

day_number = int(input("Day number: "))
root_dir = Path().parent.parent.resolve()
today_input_dir = Path(root_dir, "inputs", f"Day_{day_number}")
today_src_dir = Path(root_dir, "src", f"Day_{day_number}")
try:
    os.mkdir(today_input_dir)
    os.mkdir(today_src_dir)
except FileExistsError:
    sys.exit("Cannot create day for already existing day")
for part in (1, 2):
    for input_type in ("example", "real"):
        with open(Path(today_input_dir, f"input_part_{part}_{input_type}.txt"), "w") as f:
            pass
with open(Path(today_src_dir, "main.py"), "w") as f:
    f.write("import utils\n")
    f.write(f"Day = utils.AdventOfCodeDay({day_number})\n")
    f.write(
        """Part_1 = utils.AdventOfCodePart(Day, 1)

class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)

    def main(self, input_data):
        return input_data



Part_1.set_solution(Solution)

if __name__ == "__main__":
    Part_1.run_display_all()
    """)