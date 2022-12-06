from advent import io
from advent.puzzle import day01, day02, day03, day04, day05


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


def test_day04():
    data = io.read("day04_test01.txt")
    result = day04.Puzzle.resolve_part_01(data)
    assert result == 2
    result = day04.Puzzle.resolve_part_02(data)
    assert result == 4


def test_day05():
    data = io.read("day05_test01.txt")
    result = day05.Puzzle.resolve_part_01(data)
    assert result == "CMZ"
    result = day05.Puzzle.resolve_part_02(data)
    assert result == "MCD"
