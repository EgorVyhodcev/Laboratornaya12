#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache


@lru_cache
def fib(number):
    if number == 0 or number == 1:
        return number
    else:
        return fib(number - 2) + fib(number - 1)


if __name__ == '__main__':
    n = int(input("Enter n: "))
    print(f"Fibonacci's  number  of {n} is : {fib(n)}")
