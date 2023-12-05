import utils
from functools import cache
Day = utils.AdventOfCodeDay(5)
Part_1 = utils.AdventOfCodePart(Day, 1)

class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)
        self.seeds = []
        self.maps = []

    def main(self, input_data):
        self.parse_input(input_data)
        return self.process_seeds()
    
    def parse_input(self, input_data):
        self.seeds = input_data[0].split(" ")[1:]
        current_mapping = []
        for row in input_data[1:]:
            if not row:
                continue
            row_data = row.split(" ")
            if "to" in row_data[0]:
                current_mapping = tuple(row_data[0].split("-to-"))
                self.maps.append([])
                continue
            self.maps[-1].append({
                "src_start": int(row_data[1]),
                "dest_start": int(row_data[0]),
                "rng_len": int(row_data[2]),
                "map_diff": int(row_data[0]) - int(row_data[1])
            })


    def process_seeds(self):
        results = set()
        for seed in self.seeds:
            result = self.process_seed((tuple(x) for x in self.maps), seed)
            results.add(result)
        return min(results)
    
    @staticmethod
    # @cache
    def process_seed(map, seed):
        curr_source = int(seed)
        for map_data in map:
            mapped = False
            for map_row in map_data:
                if mapped:
                    continue
                if map_row["src_start"] <= curr_source <= map_row["src_start"] + map_row["rng_len"]:
                    # print(f"{map_mame}: {curr_source}: {map_row}")
                    curr_source += map_row["map_diff"]
                    mapped = True
        return curr_source

Part_1.set_solution(Solution())

class Solution2(Solution):
    def __init__(self):
        super().__init__()

    def process_seeds(self):
        result = 10**1000
        seed_pairs = [[]]
        for seed in self.seeds:
            if len(seed_pairs[-1]) < 2:
                seed_pairs[-1].append(int(seed))
            else:
                seed_pairs.append([int(seed)])
        for x, y in seed_pairs:
            print(x, y)
            for seed in range(x, x+y+1):
                res = self.process_seed((tuple(x) for x in self.maps), seed)
                if res < result:
                    result = res
        return result

Part_2 = utils.AdventOfCodePart(Day, 2)
Part_2.set_solution(Solution2())

if __name__ == "__main__":
    
    Part_1.run_display_all()
    Part_2.run_display_all()
    