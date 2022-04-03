import pathlib
from itertools import pairwise
from typing import Iterator


def part1() -> int:
    return increase_count(get_numbers_list())


def part2() -> int:
    return increase_count(sum_of_three())


def increase_count(numbers: Iterator[int]) -> int:
    count_increase = (b > a for a, b in pairwise(numbers))
    return sum(count_increase)


def sum_of_three() -> Iterator[int]:
    numbers_list = list(get_numbers_list())
    return (sum(numbers_list[i - 2:i + 1]) for i in range(2, len(numbers_list)))


def get_numbers_list() -> Iterator[int]:
    lines = pathlib.Path('input_day1.txt').read_text().rstrip().split('\n')
    return (int(line) for line in lines)


print(part2())
