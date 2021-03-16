#!/usr/bin/python3

import sys
import time


def bubbleSort(alist):
    arrayTemp = alist
    for x in range(len(alist)-1, 0, -1):
        for i in range(x):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return arrayTemp


def readFile(lines):
    arrayTemp = []
    f = open("numeros.txt").read().splitlines()
    # print(f)
    for x in range(0, lines):
        arrayTemp.append(int(f[x]))
    return arrayTemp


start_time = time.time()
print("Number of lines:", '{0:,}'.format(int(sys.argv[1])).replace(',', '.'))
lines = int(sys.argv[1])
array = []

array = readFile(lines)
print(array)

array = bubbleSort(array)
print(array)

print("Runtime: %s seconds" % (time.time() - start_time))
