#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2016, day 04.
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
def problem1():
    my_input = get_input("day04_input.txt")
#    my_input = get_input("day04_example.txt")

    my_room_data = get_room_data(my_input)

    real_rooms = 0
    sector_sum = 0
    for i in range(len(my_room_data)):
        (name, sector_id, csum) = my_room_data[i]

        expected_csum = calc_csum(name)

        if csum == expected_csum:
            real_rooms += 1
            sector_sum += int(sector_id)
            print("Room", name, sector_id, csum, "is real")
        else:
            print("Room", name, sector_id, csum, "is NOT real")

    print("Problem1:")
    print("Number of real rooms:", real_rooms, "sum of all sector IDs:", sector_sum)
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
