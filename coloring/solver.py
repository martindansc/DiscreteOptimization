#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys


def simple_greedy(adjMatrix):
    node_count = len(adjMatrix)
    solution = [-1] * node_count
    not_assigned = random.shuffle(range(0, node_count))
    max_colors = set([1])

    while len(not_assigned):
        current_colors = max_colors.copy()
        next_node = not_assigned.pop()
        adjs = adjMatrix[next_node]

        for adj in adjs:
            adj_color = solution[adj]
            if adj_color != -1:
                current_colors.pop(adj_color)

        if len(current_colors) == 0:
            current_color = len(max_colors)
            max_colors.add(current_color)
        else:
            current_color = current_colors.pop()

        solution[next_node] = current_color

    return solution


def try_with_n_colors(n, adjMatrix):
    possibles = [range(0, n) for i in range(len(adjMatrix))]


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    adjMatrix = [] * node_count

    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        v1 = int(parts[0])
        v2 = int(parts[1])
        edges.append(v1, v2)
        adjMatrix[v1].append(v2)
        adjMatrix[v2].append(v1)

    # build a trivial solution
    # every node has its own color
    solution = simple_greedy(adjMatrix)

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
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
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')
