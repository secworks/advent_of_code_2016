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
def check_chars(a, b, my_db):
    if (a not in my_db) or (b not in my_db):
        return False

    if my_db[a] > my_db[b]:
        return True

    elif (my_db[a] == my_db[b]) and (ord(a) < ord(b)):
        return True

    else:
        return False

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def real_room(csum, my_db):
    return check_chars(csum[0], csum[1], my_db) and \
        check_chars(csum[1], csum[2], my_db) and \
        check_chars(csum[2], csum[3], my_db) and \
        check_chars(csum[3], csum[4], my_db)



#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    my_input = get_input("day04_input.txt")
#    my_input = get_input("day04_example.txt")

    my_room_data = get_room_data(my_input)
    my_room_data_stats = get_room_data_stats(my_room_data)

    real_rooms = 0
    sector_sum = 0
    for i in range(len(my_room_data)):
        (name, sector_id, csum) = my_room_data[i]
        my_db = my_room_data_stats[i]

        if real_room(csum, my_db):
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
