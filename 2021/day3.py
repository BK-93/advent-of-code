import pathlib

power_consumption = 0
gamma_rate = 0
epsilon_rate = 0


def get_power_rate(binaries: list[str]):
    gamma_list = []
    epsilon_list = []
    count = 0

    while count <= 11:
        temp_list = []

        for b in binaries:
            l = split(b)
            print(l[count])

        count += 1

    # print(binaries)


def bina_to_deci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))


def split(word):
    return [char for char in word]


def get_bin_list() -> list[str]:
    lines = pathlib.Path('input_day3.txt').read_text().rstrip().split('\n')
    return lines


get_power_rate(get_bin_list())

