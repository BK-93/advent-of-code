import pathlib


def get_position(course: list[str]):
    horizontal_pos = 0
    depth = 0
    aim = 0

    for c in course:
        if c.split()[0] == 'forward':
            horizontal_pos = horizontal_pos + int(c.split()[1])
            depth_inc = aim * int(c.split()[1])
            depth = depth + depth_inc
        if c.split()[0] == 'up':
            # Uncomment line 16 for part 1 and uncomment line 17 for part 2
            # depth = depth - int(c.split()[1])
            aim = aim - int(c.split()[1])
        if c.split()[0] == 'down':
            # Uncomment line 20 for part 1 and uncomment line 21 for part 2
            # depth = depth + int(c.split()[1])
            aim = aim + int(c.split()[1])

    print(horizontal_pos * depth)


def get_course_list() -> list[str]:
    lines = pathlib.Path('input_day2.txt').read_text().rstrip().split('\n')
    return lines


get_position(get_course_list())
