#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2016, day 06.
#=======================================================================

from collections import Counter


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    lines = []
    with open(filename,'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    my_input = get_input("day06_input.txt")
#    my_input = get_input("day06_example.txt")

    col_strings = []
    freqs = []
    msg = ''
    for s in range(len(my_input[0])):
        col_strings.append('')

    for s in my_input:
        for i in range(len(s)):
            col_strings[i] += s[i]

    for i in range(len(col_strings)):
        col_strings[i] = sorted(col_strings[i])
        freqs = Counter(col_strings[i]).most_common()
        msg += freqs[0][0]

    print("Problem1:", msg)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    my_input = get_input("day06_input.txt")
#    my_input = get_input("day06_example.txt")

    col_strings = []
    freqs = []
    msg = ''
    for s in range(len(my_input[0])):
        col_strings.append('')

    for s in my_input:
        for i in range(len(s)):
            col_strings[i] += s[i]

    for i in range(len(col_strings)):
        col_strings[i] = sorted(col_strings[i])
        freqs = Counter(col_strings[i]).most_common()
        msg += freqs[-1][0]

    print("Problem2:", msg)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
