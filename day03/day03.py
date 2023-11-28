#!/usr/bin/env python3
#=======================================================================
#
# day03.py
# --------
# Solutions to Advent of Code 2016, day 03.
#
#=======================================================================


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(line.strip())
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_sides(i):
    graphs = []
    for s in i:
        (one, two, three) = s.split(',')
        graphs.append((int(one), int(two), int(three)))
    return graphs

#-------------------------------------------------------------------
# Extract triangles three rows at a time.
#-------------------------------------------------------------------
def get_sides3(i):
    graphs = []
    for r in range(0, len(i), 3):
        (l00, l01, l02) = i[r].split(',')
        (l10, l11, l12) = i[r + 1].split(',')
        (l20, l21, l22) = i[r + 2].split(',')

        graphs.append((int(l00), int(l10), int(l20)))
        graphs.append((int(l01), int(l11), int(l21)))
        graphs.append((int(l02), int(l12), int(l22)))
    return graphs


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def count_triangles(graphs):
    triangles = 0

    for g in graphs:
        (one, two, three) = g

        if (one + two > three) and (one + three > two) and (two + three > one):
            triangles += 1

    return triangles


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")
    my_input = get_input("day03_input.txt")
    my_graphs = get_sides(my_input)
    num_triangles = count_triangles(my_graphs)
    print("number of triangles:", num_triangles)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")
    my_input = get_input("day03_input.txt")
#    my_input = get_input("day03_example.txt")

    my_graphs = get_sides3(my_input)
    num_triangles = count_triangles(my_graphs)

    print("")
    print("number of triangles:", num_triangles)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2016, day 03")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
