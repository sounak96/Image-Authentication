
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:45:19 2019

@author: sounak
"""
import cv2
import numpy as np


def check():
    file = (input("Enter file name\t"))
    img = cv2.imread(file, 0)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    r1, r2 = img.shape
    cp = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    d1 = digest(img, r1, r2, cp, 3, 3)
    file2 = input("Enter tampered image name\t")
    img2 = cv2.imread(file2, 0)
    '''for i in range(r1):
        for j in range(r2):
            if i > j:
                img2[i][j] = img2[i][j] +i'''
    cv2.imshow("change", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    t1, t2 = img2.shape
    d2 = digest(img2, t1, t2, cp, 3, 3)
    # print(d1,d2)
    if np.array_equal(d1, d2):
        print("true")
    else:
        print("false")
    
    length = len(d2)
    count = 0
    for i in range(length):
        if d1[i] != d2[i]:
            count += 1
            print(i, end=",")
    percentage1 = (count / len(d1)) * 100
    print("change percentage=", percentage1)
    print("Unchange percentage=", 100 - percentage1)


def digest(img, n1, n2, cp, x, y):
    import crt    
#    pixel_map=img.load()
    ar = [0 for i in range(x * y)]
    x1, y1, r, a, b = 0, 0, 0, 0, 0
    if (n1 % x) != 0 and (n2 % y) != 0:
        m1 = n1 + x - (n1 % x)
        m2 = n2 + y - (n2 % y)
    else:
        m1 = n1
        m2 = n2
    t = []
    while (x1+x) < m1:
        while (y1+y) < m2:
            for i in range(x1, x1+x):
                for j in range(y1, y1+y):
                    ar[r] = img[i][j]
                    r += 1
                    # print(ar)
            z = crt.findx(r, ar, cp)
            # print(z)
            ar = [0 for i in range(1000)]
            r = 0
            t.append(z)
            a += 1
            y1 = y1+y
        x1 = x1+x
        y1 = 0
    return t


def encrypt():
    file = (input("Enter file name\t"))
    img = cv2.imread(file, 0)
    #    print(img)
    r1, r2 = img.shape
    #    print(r1,r2)
    #    b=bytearray(img)
    cp = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    digest(img, r1, r2, cp, 3, 3)


check()
