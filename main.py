def happiness(integers, set_a, set_b):
    h = 0
    for i in integers:
        if i in set_a:
            h += 1
        elif i in set_b:
            h -= 1

    return h


def main():
    with open('input.txt', 'r') as f:
        first_line = f.readline()
        second_line = f.readline()
        third_line = f.readline()
        fourth_line = f.readline()

        # Get n and m
        split_first = first_line.split(' ')
        n = int(split_first[0])
        m = int(split_first[1])

        # Get array of integers
        split_second = second_line.split(' ')
        integers = list(map(lambda x: int(x), split_second))

        # Get set A
        split_third = third_line.split(' ')
        set_a = set(map(lambda x: int(x), split_third))

        # Get set B
        split_fourth = fourth_line.split(' ')
        set_b = set(map(lambda x: int(x), split_fourth))

        # print(f'n = {n}')
        # print(f'm = {m}')
        # print(f'Array of integers = {integers}')
        # print(f'Set A = {set_a}')
        # print(f'Set B = {set_b}')

        if not (1 <= n <= 100000):
            raise ValueError("That was no valid number: 1 <= n <= 100000")

        if not (1 <= m <= 100000):
            raise ValueError("That was no valid number: 1 <= m <= 100000")

        if not (1 <= max(integers) <= 1000000000) or not (1 <= min(integers) <= 1000000000):
            raise ValueError("That was no valid number: 1 <= integers <= 1000000000")

        if not len(integers) == n:
            raise ValueError(f"The length of array of integers must be {n}")

        if not len(set_a) == m or not len(set_b) == m:
            raise ValueError(f"The length of set A and B must be {m}")

        if not set_a.isdisjoint(set_b):
            raise ValueError("Set A and B must be disjoint")

        print(happiness(integers, set_a, set_b))


if __name__ == '__main__':
    main()
