import sys
import math
int_list = []

# part 1
'''

def safe_reports(levels: list[list[int]]) -> int:
    count: int = 0
    safe: int = 0
    pos: int = 0
    neg: int = 0

    
    for lev in levels:
        for y in range(len(lev)-1):
            if lev[y] - lev[y+1] > 0 and lev[y] - lev[y+1] < 4:
                pos += 1
                neg = 0

                

            elif lev[y] - lev[y+1] < 0 and lev[y] - lev[y+1] > -4:
                neg += 1
                pos = 0

                

            else:
                pos = 0
                neg = 0

                
        if pos == (len(lev)-1) or neg == (len(lev)-1):
            safe += 1
            pos = 0
            neg = 0
    return safe
    

'''

# part 2


def is_monotonically_increasing(lev: list[int]) -> bool:
    return all(0 < lev[i + 1] - lev[i] < 4 for i in range(len(lev) - 1))


def is_monotonically_decreasing(lev: list[int]) -> bool:
    return all(-4 < lev[i + 1] - lev[i] < 0 for i in range(len(lev) - 1))


def safe_reports(levels: list[list[int]]) -> int:
    safe: int = 0

    for lev in levels:
        print(f"Processing sublist: {lev}")
        if is_monotonically_increasing(lev) or is_monotonically_decreasing(lev):
            safe += 1
            print(f"Sublist is safe, incrementing safe counter to {safe}")
            continue

        valid: bool = False
        for i in range(len(lev)):
            new_lev: list[int] = lev[:i] + lev[i + 1:]
            if is_monotonically_increasing(new_lev) or is_monotonically_decreasing(new_lev):
                valid = True
                break

        if valid:
            safe += 1
            print(
                f"Sublist is safe after removing one element, incrementing safe counter to {safe}")
        else:
            print("Sublist is not safe")

    return safe


def parse_input(input: list[str]) -> list[list[int]]:
    lists: list[list[int]] = []
    for line in input:
        split_input: list[str] = line.split()
        int_list: list[int] = [int(x) for x in split_input]
        lists.append(int_list)

    return lists


def main():
    if len(sys.argv) == 2:
        input_file: str = str(sys.argv[1])
    else:
        input_file: str = './input.txt'

    with open(f'{input_file}', 'r') as f:
        input: list[str] = f.readlines()

    levels: list[list[int]] = parse_input(input)

    result: int = safe_reports(levels)
    print(f"Total safe sublists: {result}")


if __name__ == "__main__":
    main()
