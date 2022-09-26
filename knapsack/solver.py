#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    optimal = 1

    divisor = 1
    too_large = pow(10, 4)
    if(capacity > too_large):
        divisor = capacity / too_large
        capacity = math.floor(capacity / divisor)
        optimal = 0

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(
            i-1,
            int(parts[0]),
            math.ceil(int(parts[1]) / divisor)
        ))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    taken = [([0] * (capacity + 1)) for i in range(item_count+1)]

    for j in range(1, capacity + 1):
        for item in items:
            i = item.index + 1
            new_value_if_not_taken = taken[i - 1][j]
            new_value_if_taken = 0
            if j - item.weight >= 0:
                new_value_if_taken = taken[i - 1][j - item.weight] + item.value

            if new_value_if_not_taken > new_value_if_taken:
                taken[i][j] = new_value_if_not_taken
            else:
                taken[i][j] = new_value_if_taken

    solution = [0] * item_count
    i = item_count
    j = capacity
    while(taken[i][j] != 0):
        if taken[i][j] != taken[i - 1][j]:
            j = j - items[i - 1].weight
            solution[i - 1] = 1
        i = i - 1

    # prepare the solution in the specified output format
    output_data = str(taken[item_count][capacity]) + \
        ' ' + str(optimal) + '\n'
    output_data += ' '.join(map(str, solution))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
