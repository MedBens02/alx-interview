#!/usr/bin/python3
'''Minimum operations challenge.
'''


def minOperations(n):
    if n <= 1:
        return 0

    oper = 0
    fact = 2

    while n > 1:
        while n % fact == 0:
            oper += fact
            n //= fact
        fact += 1

    return oper
