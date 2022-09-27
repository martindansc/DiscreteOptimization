#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Any
from dataclasses import dataclass, field
import random
import sys
from collections import namedtuple

random.seed(1)


def simple_greedy(adjMatrix):
    node_count = len(adjMatrix)
    solution = [-1] * node_count
    not_assigned = list(range(0, node_count))
    random.shuffle(not_assigned)
    max_colors = set([1])

    while len(not_assigned):
        current_colors = max_colors.copy()
        next_node = not_assigned.pop(0)
        adjs = adjMatrix[next_node]

        for adj in adjs:
            adj_color = solution[adj]
            if adj_color != -1 and adj_color in current_colors:
                current_colors.remove(adj_color)

        if len(current_colors) == 0:
            current_color = len(max_colors) + 1
            max_colors.add(current_color)
        else:
            current_color = current_colors.pop()

        solution[next_node] = current_color

    return len(max_colors), solution


Value = namedtuple("Value", ["id", "possible_colors", "n_vertex"])


def try_with_n_colors(max_colors, adjMatrix):
    node_count = len(adjMatrix)
    solution = [-1] * node_count

    possibles = {}
    for i in range(node_count):
        possible_colors = list(range(max_colors))
        possibles[i] = Value(
            id=i, possible_colors=possible_colors, n_vertex=len(adjMatrix[i]))

    while len(possibles) > 0:
        next_node = None
        min_options = -1
        for i in possibles:
            possible_next_node = possibles[i]
            possible_min_options = len(
                possible_next_node.possible_colors) - possible_next_node.n_vertex
            if next_node == None or possible_min_options < min_options:
                next_node = possible_next_node
                min_options = possible_min_options

        del possibles[next_node.id]
        best_color = None
        best_counter = -1
        for color in next_node.possible_colors:
            color_counter = 0
            for v in adjMatrix[next_node.id]:
                if v in possibles:
                    if color in possibles[v].possible_colors:
                        color_counter += 1
                        if len(possibles[v].possible_colors) == 1:
                            color_counter += 3
                        if len(possibles[v].possible_colors) == 2:
                            color_counter += 1
            if best_color == None or color_counter < best_counter:
                best_counter = color_counter
                best_color = color

        for v in adjMatrix[next_node.id]:
            if v in possibles:
                try:
                    possibles[v].possible_colors.remove(best_color)
                except ValueError:
                    pass

                if len(possibles[v].possible_colors) <= 0:
                    return None

        solution[next_node.id] = best_color

    return solution


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    adjMatrix = [[] for i in range(node_count)]

    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        v1 = int(parts[0])
        v2 = int(parts[1])
        adjMatrix[v1].append(v2)
        adjMatrix[v2].append(v1)

    # build a trivial solution
    # every node has its own color
    best_num = node_count
    best_solution = range(1, node_count + 1)
    for i in range(1, 10):
        used_colors, solution = simple_greedy(adjMatrix)
        if used_colors < best_num:
            best_num = used_colors
            best_solution = solution

    while best_num > 1:
        try_better = try_with_n_colors(best_num - 1, adjMatrix)
        if try_better == None:
            break
        best_solution = try_better
        best_num = best_num - 1

    # prepare the solution in the specified output format
    output_data = str(best_num) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, best_solution))

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
