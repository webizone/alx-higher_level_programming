#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
     c = 0
     for i in range(x):
    try:
    
            print(my_list[index], end="")
            c += 1
            print()
    except IndexError:
        break
        print()
        return c
