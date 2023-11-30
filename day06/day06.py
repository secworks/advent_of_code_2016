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
def get_room_data(lines):
    room_data = []

    for line in lines:
        (tmp1, tmp2) = line.split('[')
        checksum = tmp2[:-1]

        tmp3 = tmp1.split('-')
        room_id = tmp3[-1]
        enc_name = ''.join(tmp3[:-1])

        room_data.append((enc_name, room_id, checksum))
    return room_data

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def calc_csum(name):
    freq_table = Counter(''.join(sorted(name))).most_common()
    csum = ''

    for i in range(5):
        csum += freq_table[i][0]
    return csum

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def rotx(name, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    decode = ''
    for c in name:
        i = alphabet.find(c)
        j = (i + rot) % len(alphabet)
        decode += alphabet[j]
    return decode


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    my_input = get_input("day06_input.txt")
    my_input = get_input("day06_example.txt")

    print("Problem1:")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem2:")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
