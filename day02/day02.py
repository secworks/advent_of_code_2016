#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2016, day 02.
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
def get_number(s):
    if s == (0,0):
        return 1

    if s == (1,0):
        return 2

    if s == (2,0):
        return 3


    if s == (0,1):
        return 4

    if s == (1,1):
        return 5

    if s == (2,1):
        return 6


    if s == (0,2):
        return 7

    if s == (1,2):
        return 8

    if s == (2,2):
        return 9


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def update_state(s, d):
    (x,y) = s

    if d == 'L':
        if x == 0:
            return s
        else:
            return (x - 1, y)

    if d == 'R':
        if x == 2:
            return s
        else:
            return (x + 1, y)

    if d == 'U':
        if y == 0:
            return s
        else:
            return (x, y - 1)

    if d == 'D':
        if y == 2:
            return s
        else:
            return (x, y + 1)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_diamond_code(s):
    if s == (2,0):
        return '1'


    if s == (1,1):
        return '2'

    if s == (2,1):
        return '3'

    if s == (3,1):
        return '4'


    if s == (0,2):
        return '5'

    if s == (1,2):
        return '6'

    if s == (2,2):
        return '7'

    if s == (3,2):
        return '8'

    if s == (4,2):
        return '9'


    if s == (1,3):
        return 'A'

    if s == (2,3):
        return 'B'

    if s == (3,3):
        return 'C'


    if s == (2,4):
        return 'D'


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def update_diamond_state(s, d):
    (x,y) = s

    if d == 'L':
        if s in [(2, 0), (1, 1), (0, 2), (1, 3), (2, 4)]:
            return s
        else:
            return (x - 1, y)

    if d == 'R':
        if s in [(2, 0), (3, 1), (4, 2), (3, 3), (2, 4)]:
            return s
        else:
            return (x + 1, y)

    if d == 'U':
        if s in [(2, 0), (1, 1), (3, 1), (0, 2), (4, 2)]:
            return s
        else:
            return (x, y - 1)

    if d == 'D':
        if s in [(0, 2), (4, 2), (1, 3), (3, 3), (2, 4)]:
            return s
        else:
            return (x, y + 1)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    my_input = get_input("day02_input.txt")
#    my_input = get_input("day02_example1.txt")

    # Start in the middle of the keypad, i.e. number five.
    state = (1,1)
    number = ""

    for line in my_input:
        for d in line:
            state = update_state(state, d)
        number += str(get_number(state))

    print("Problem1:")
    print("Number:", number)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    my_input = get_input("day02_input.txt")
#    my_input = get_input("day02_example1.txt")

    # Start in the middle of the keypad, i.e. number five.
    state = (0,2)
    code = ""

    for line in my_input:
        for d in line:
            state = update_diamond_state(state, d)
        code += (get_diamond_code(state))

    print("Problem2:")
    print("Code:", code)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
