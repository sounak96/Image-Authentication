# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:03:05 2019

@author: sounak
"""

def inverse(x,n):
    
    w1, w2, z1, z2 = n, x, 0, 1
    while w2 != 0:
        q = w1//w2
        w = w1-q*w2
        w1 = w2
        w2 = w
        t = z1-q*z2
        z1 = z2
        z2 = t
    return z1


def findx(n, y, p):
    P = 1
    for i in range(n):
        P = P * p[i]
    
    s = 0
    for i in range(n):
        pp = P//p[i]
        s += y[i]*pp*inverse(pp, p[i])
    x = s % P
    return x
# y=[2,3,1]
# p=[3,4,5]
# print("x= ",findx(3,y,p))