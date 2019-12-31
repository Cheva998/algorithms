# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:56:25 2019

@author: Cheva998

Implementation of the Karatsuba multiplication algorithm
Input: two n-digit positive integers x and y.
Output: the product x·y.
Assumption: n is a power of 2.
"""

import math

def katatsuba_mult(x,y):
    if len(str(x)) == 1:
        return x * y
    else:
        n = len(str(x))
        n2 = n // 2
        a = int(str(x)[:n2])
        b = int(str(x)[n2:])
        c = int(str(y)[:n2])
        d = int(str(y)[n2:])
        p = a + b
        q = c + d
        ac = katatsuba_mult(a,c)
        bd = katatsuba_mult(b,d)
        pq = katatsuba_mult(p,q)
        adbc = pq - ac - bd
        mult = 10 ** n * ac + 10 ** (n2) * adbc + bd
        return mult


x = 150000
y = 200000
assert(len(str(x)) == len(str(y))), "Bad input, both integers must have equal\
numbers of digits"

assert(math.ceil(math.log(len(str(x)),2)) == math.floor(math.log(len(str(x)))))\
, "Bad input, the integers must have a number of digits equal to a power of 2"

print(katatsuba_mult(x,y))