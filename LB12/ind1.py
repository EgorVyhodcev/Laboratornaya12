#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def subset(mySet, check=None):
    if check is None:
        check = []
    if len(mySet) != 0 and mySet not in check:
        check.append(mySet)
        print(set(mySet))
        for i, elem in enumerate(mySet):
            subset(mySet[0:i] + mySet[i + 1:len(mySet)], check)


if __name__ == '__main__':
    my_set = {int(i) for i in input("Enter the set: ").split()}
    list_set = list(my_set)
    subset(list_set)
