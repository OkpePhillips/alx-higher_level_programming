#!/usr/bin/python
def new_in_list(my_list, idx, element):
    if idx > len(my_list) or idx < 0:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
