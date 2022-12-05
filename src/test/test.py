from advent import io
from advent.puzzle import (
    day01,
    day02,
    day03
)


def test_day01():
    data = io.read("day01_test01.txt")
    result = day01.Puzzle.resolve_part_01(data)
    assert result == 24000
    result = day01.Puzzle.resolve_part_02(data)
    assert result == 45000


def test_day02():
    data = io.read("day02_test01.txt")
    result = day02.Puzzle.resolve_part_01(data)
    assert result == 15
    result = day02.Puzzle.resolve_part_02(data)
    assert result == 12

def test_day03():
    data = io.read("day03_test01.txt")
    result = day03.Puzzle.resolve_part_01(data)
    assert result == 157
    result = day03.Puzzle.resolve_part_02(data)
    assert result == 70