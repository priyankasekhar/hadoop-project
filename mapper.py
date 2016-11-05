#!/usr/bin/env python
import sys


for line in sys.stdin.readlines():
    #remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    row = line.split(',')
    try:
        row=float(row[1])
    except:
        continue
    i=[0,1,2,3]
    j=[1,2,3,4]
    for x,y in zip(i,j):
        if row[1]=0:
            print("deaths[%d-%d]\t %s") % (x,y,1)

        elif row[1]=1:
            print("survivors[%d-%d]\t %s") % (x,y,1)