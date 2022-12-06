from advent.io import read
from advent.puzzle import day06 as day


if __name__ == "__main__":
    data = read("day06.txt")
    print(day.Puzzle.resolve_part_01(data))
    print(day.Puzzle.resolve_part_02(data))
