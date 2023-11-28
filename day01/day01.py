#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2016, day 01.
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
    if curr == "West":
        if m == "L":
            return "South"
        if m == "R":
            return "North"

    if curr == "East":
        if m == "L":
            return "North"
        if m == "R":
            return "South"

    if curr == "North":
        if m == "L":
            return "West"
        if m == "R":
            return "East"

    if curr == "South":
        if m == "L":
            return "East"
        if m == "R":
            return "West"


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_position(curr, d, x, y):
    if curr == "North":
        y = y - d

    if curr == "South":
        y = y + d

    if curr == "West":
        x = x - d

    if curr == "East":
        x = x + d

    return (x, y)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    my_input = get_input("day01_input.txt")
    my_moves = get_moves(my_input)

    xd = 0
    yd = 0
    curr_dir = "North"

    for m, d in my_moves:
        curr_dir = get_direction(m, curr_dir)
        (xd, yd) = get_position(curr_dir, d, xd, yd)

    print("Problem1:")
    print("Total distance: %d" % (abs(xd) + abs(yd)))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
#    my_input = get_input("day01_example1.txt")
    my_input = get_input("day01_input.txt")
    my_moves = get_moves(my_input)

    # Start at pos 0,0 and add it to visited positions
    # We face north when starting.
    x = 0
    y = 0
    curr_dir = "North"
    visited = set()
    visited.add((x, y))
    done = False

    for (m, d) in my_moves:
        new_dir = get_direction(m, curr_dir)

        # Walk the path, generate and check all positions.
        for delta in range(1, d + 1):
            pos = get_position(new_dir, delta, x, y)

            if pos in visited and not done:
                revisited = pos
                done = True
            visited.add(pos)

        # Set last delta position as new position.
        # Update direction we are facing.
        (x, y) = pos
        curr_dir = new_dir

    print("Problem2:")
    print("Distance to first revisited position:", (abs(revisited[0]) + abs(revisited[1])))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
