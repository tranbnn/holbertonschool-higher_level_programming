#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    new_list = my_list[:]

    for pointer in new_list:
        if pointer % 2 == 0:
            new_list[pointer] = True
        else:
            new_list[pointer] = False
        
    return new_list
