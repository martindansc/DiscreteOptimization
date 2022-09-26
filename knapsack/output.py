#!/bin/env python3
import sys

if __name__ == '__main__':
    filename = sys.argv[1].strip()
    with open(filename, 'r') as INFILE:
        input_data = INFILE.read()

        # parse the input
        lines = input_data.split('\n')

        parts = lines[0].split()
        item_count = int(parts[0])
        capacity = int(parts[1])
        values = []
        weights = []

        for i in range(item_count):
            line = lines[i+1]
            parts = line.split()
            values.append(int(parts[0]))
            weights.append(int(parts[1]))

    parts = sys.stdin.readline().split()
    yourValue = int(parts[0])
    yourOpt = int(parts[1])
    parts = sys.stdin.readline().split()
    taken = [int(x) for x in parts]

    calcWeight = sum(weights[i]*taken[i] for i in range(item_count))
    calcValue = sum(values[i]*taken[i] for i in range(item_count))
    for pos, wasTaken in enumerate(taken):
        if wasTaken:
            print("Took item:", pos, "with weight:",
                  weights[pos], "and value:", values[pos])
    print("calc weight:", calcWeight, "is", [
          "greater than", "within"][calcWeight <= capacity], "the capacity of", capacity)
    print("calc_value:", calcValue, ["does not equal", "equals"]
          [calcValue == yourValue], "value of", yourValue, "provided")
