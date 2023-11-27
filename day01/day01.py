#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2016, day 1.
#=======================================================================

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    with open(filename,'r') as f:
        for line in f:
            l = line.strip()
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_moves(s):
    m = ""
    for c in s:
        if c != " ":
            m += c
    l = m.split(",")

    moves = []
    for c in l:
        m = c[0]
        d = int(c[1:])
        moves.append((m, d))
    return(moves)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_direction(m, curr):
    if curr == "":
        if m == "L":
            return "left"
        else:
            return "right"

    if curr == "left":
        if m == "L":
            return "down"
        if m == "R":
            return "up"

    if curr == "right":
        if m == "L":
            return "up"
        if m == "R":
            return "down"

    if curr == "up":
        if m == "L":
            return "left"
        if m == "R":
            return "right"

    if curr == "down":
        if m == "L":
            return "right"
        if m == "R":
            return "left"


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_position(curr, d, x, y):
    if curr == "up":
        y = y - d

    if curr == "down":
        y = y + d

    if curr == "left":
        x = x - d

    if curr == "right":
        x = x + d

    return (x, y)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    my_input = get_input("day01_input.txt")
    my_moves = get_moves(my_input)

    xd = 0
    yd = 0
    curr_dir = ""

    for m, d in my_moves:
        curr_dir = get_direction(m, curr_dir)
        (xd, yd) = get_position(curr_dir, d, xd, yd)

    print("Problem1:")
    print("Total distance: %d" % (abs(xd) + abs(yd)))
    print("")

    print("Problem2:")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    my_input = get_input("day01_input.txt")
    my_moves = get_moves(my_input)

    xd = 0
    yd = 0
    curr_dir = ""
    visited = set()

    for m, d in my_moves:
        curr_dir = get_direction(m, curr_dir)
        (xd, yd) = get_position(curr_dir, d, xd, yd)

        if (xd, yd) not in visited:
            visited.add((xd, yd))
        else:
            print((xd, yd))

    print("Problem2:")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
