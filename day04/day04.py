#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2016, day 04.
#=======================================================================

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
def get_room_data_stats(room_data):
    stats = []

    for room in room_data:
        (room_enc_name, room_id, room_checksm) = room
        chr_stats = {}
        for c in room_enc_name:
            if c in chr_stats:
                chr_stats[c] += 1
            else:
                chr_stats[c] = 1
        stats.append(chr_stats)
    return stats


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
#    my_input = get_input("day04_input.txt")
    my_input = get_input("day04_example.txt")

    my_room_data = get_room_data(my_input)
    my_room_data_stats = get_room_data_stats(my_room_data)

    print("Room data:", my_room_data)
    print("Room data stats:", my_room_data_stats)

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
