import utils
Day = utils.AdventOfCodeDay(6)
Part_1 = utils.AdventOfCodePart(Day, 1)

class Solution(utils.AdventOfCodeSolution):
    def __init__(self):
        utils.AdventOfCodeSolution.__init__(self)
        self.boats = []

    def main(self, input_data):
        self.parse_input(input_data)
        return self.iterate_boats()
    
    def parse_input(self, input_data):
        times, distances = input_data
        times = times.split()[1:]
        distances = distances.split()[1:]
        self.boats = list(zip(map(int, times), map(int, distances)))
        print(self.boats)

    def iterate_boats(self):
        total_score = 1
        for time, dist in self.boats:
            total_score *= self.num_options(time, dist)
        return total_score

    def num_options(self, time, distance):
        opts = 0
        for t in range(1, time):
            if self.distance_travelled(t, time) > distance:
                opts += 1
        return opts

    @staticmethod
    def distance_travelled(held_time, total_time):
        speed = held_time
        travel_time = total_time - held_time
        return speed * travel_time


Part_1.set_solution(Solution())

class Solution2(Solution):
    def __init__(self):
        super().__init__()
    
    def parse_input(self, input_data):
        times, distances = input_data
        times = int("".join(times.split()[1:]))
        distances = int("".join(distances.split()[1:]))
        self.boats = [(times, distances)]
        print(self.boats)

Part_2 = utils.AdventOfCodePart(Day, 2)
Part_2.set_solution(Solution2())

if __name__ == "__main__":
    
    Part_1.run_display_all()
    Part_2.run_display_all()
    