import sys
import math

# part 1


def what_distance(location_id_list1: list, location_id_list2: list):
    distance = []
    total = 0
    sorted_list1 = sorted(location_id_list1)
    sorted_list2 = sorted(location_id_list2)

    for i in range(len(location_id_list2)):
        distance.append(abs(sorted_list1[i] - sorted_list2[i]))

    for i in range(len(distance)):
        total += distance[i]

    return total

# part 2


def compare(location_id_list1: list, location_id_list2: list):
    total = 0

    for i in range(len(location_id_list1)):
        times_occured = location_id_list2.count(location_id_list1[i])
        total += times_occured*location_id_list1[i]

    return total


def parse_input(input):
    list1 = []
    list2 = []
    for i in range(len(input)):
        split_input = input[i].split()
        list1.append(int(split_input[0]))
        list2.append(int(split_input[1]))

    return list1, list2


def main():
    if len(sys.argv) == 2:
        input_file = str(sys.argv[1])
    else:
        input_file = './input.txt'

    with open(f'{input_file}', 'r') as f:
        input = f.readlines()

    (location_id_list1, location_id_list2) = parse_input(input)

    # Call the function and print the result
    # result = what_distance(location_id_list1, location_id_list2)
    # print(result)
    result = compare(location_id_list1, location_id_list2)
    print(result)


if __name__ == "__main__":
    main()
