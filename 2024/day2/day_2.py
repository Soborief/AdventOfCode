import sys
import math
int_list = []

# part 1


def safe_reports(levels):
    count = 0
    safe = 0
    pos = 0
    neg = 0

    # for sublist in levels:
    # int_list.extend(sublist)
    # print(levels)
    # for i in range(len(levels)-1):
    #     list = levels[i].split()
    #     print(list)
    # for x in range(len(levels)-1):
    #     int_list.append(int(levels[x]))
    # print(int_list)
    for lev in levels:
        for y in range(len(lev)-1):
            if lev[y] - lev[y+1] > 0 and lev[y] - lev[y+1] < 4:
                pos += 1
                neg = 0

                # if pos == 4:
                #     safe += 1
                #     pos = 0
                #     neg = 0

                # print(
                # f"działanie1: {lev[y]} - {lev[y+1]} = {lev[y] - lev[y+1]}", pos)
                # print(safe)

            elif lev[y] - lev[y+1] < 0 and lev[y] - lev[y+1] > -4:
                neg += 1
                pos = 0

                # if neg == 4:
                #     safe += 1
                #     neg = 0
                #     pos = 0

                # print(
                # f"działanie2: {lev[y]} - {lev[y+1]} = {lev[y] - lev[y+1]}", neg)
                # print(safe)

            else:
                pos = 0
                neg = 0

                # print(
                # f"działanie3: {lev[y]} - {lev[y+1]} = {lev[y] - lev[y+1]}", pos, neg)
                # print(safe)
        if pos == (len(lev)-1) or neg == (len(lev)-1):
            safe += 1
            pos = 0
            neg = 0
    return safe
    # if int(list[i]) - int(list[i+1]) < 4:
    # safe = +1
    # for x in range(len(list)):
    # int_list = int(list[x])

    # for x in range(len(list)-1):

    #     if int(list[i]) - int(list[i+1]) < 4:
    #         safe = +1
    #     elif int(list[i+1]) - int(list[i]) < 4:
    #         safe = +1


# reports = int(int_list.strip())

# if levels[i] - levels[i+1] < 4:
#   safe = +1
# elif levels[i+1] - levels[i] < 4:
#   safe = +1

# print(safe)

# return safe


'''
# part 2

def safe_reports(levels):
    count = 0
    safe = 0
    pos = 0
    neg = 0

    for lev in levels:
        for y in range(len(lev)-1):
            if lev[y] - lev[y+1] > 0 and lev[y] - lev[y+1] < 4:
                pos += 1
                neg = 0

                # if pos == 4:
                #     safe += 1
                #     pos = 0
                #     neg = 0

                # print(
                # f"działanie1: {lev[y]} - {lev[y+1]} = {lev[y] - lev[y+1]}", pos)
                # print(safe)

            elif lev[y] - lev[y+1] < 0 and lev[y] - lev[y+1] > -4:
                neg += 1
                pos = 0

                # if neg == 4:
                #     safe += 1
                #     neg = 0
                #     pos = 0

                # print(
                # f"działanie2: {lev[y]} - {lev[y+1]} = {lev[y] - lev[y+1]}", neg)
                # print(safe)
            elif lev[y] == lev[y+1]:
                
            
            
            else:
                pos = 0
                neg = 0

                # print(
                # f"działanie3: {lev[y]} - {lev[y+1]} = {lev[y] - lev[y+1]}", pos, neg)
                # print(safe)
        if pos == (len(lev)-1) or neg == (len(lev)-1):
            safe += 1
            pos = 0
            neg = 0
    return safe
'''


def parse_input(input):
    lists = []
    for line in input:
        split_input = line.split()
        int_list = [int(x) for x in split_input]
        # print(int_list[2])
        lists.append(int_list)

    # print(input)

    # print(lists[2])
    # print(lists[1])
    # print(lists)
    return lists


def main():
    if len(sys.argv) == 2:
        input_file = str(sys.argv[1])
    else:
        input_file = './input.txt'

    with open(f'{input_file}', 'r') as f:
        input = f.readlines()
    # int_lines = [int(i) for i in input]

    levels = parse_input(input)

    result = safe_reports(levels)
    print(result)


if __name__ == "__main__":
    main()
