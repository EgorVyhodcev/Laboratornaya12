#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def subset(my_set, check=None):
    if check is None:
        check = []
    if len(my_set) != 0 and my_set not in check:
        check.append(my_set)
        print(set(my_set))
        for i, elem in enumerate(my_set):
            subset(my_set[0:i] + my_set[i + 1:len(my_set)], check)


if __name__ == '__main__':
    start_set = {int(i) for i in input("Enter the set: ").split()}
    list_set = list(start_set)
    subset(list_set)
