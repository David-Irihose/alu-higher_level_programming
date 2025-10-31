#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Shift elements to remove the element at idx
    for i in range(idx, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    my_list.pop()  # remove the last duplicate
    return my_list
