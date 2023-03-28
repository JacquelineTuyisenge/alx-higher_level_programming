#!/usr/bin/pyton3
# function that prints first 'x' element of a list and onl integer

def safe_print_list_integers(my_list=[], x=0):
    m = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i], end="")
            m += 1
        except (TypeErroe, ValueError):
            continue
            print("")
            return (m)
