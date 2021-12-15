#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find_max(seq, max_so_far):
    if not seq:
        return max_so_far
    if max_so_far < seq[0]:
        return find_max(seq[1:], seq[0])
    else:
        return find_max(seq[1:], max_so_far)


if __name__ == '__main__':
    a = [i for i in range(10) if i % 2 != 0]
    print(a)
    print(find_max(a, a[0]))
