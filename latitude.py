#!/usr/bin/env python
import sys


def latitude(lat):
    rounded=round(lat)
    mod=rounded%5
    bottom=rounded-mod
    top=bottom+5
    return bottom,top
def day_by_day(date,mag):
    print("%s\t%s")%(date,mag)

for line in sys.stdin.readlinaes():
    #remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    row = line.split(',')
    try:
        mag=float(row[4])
        lat=float(row[1])
        date_time = row[0]
        date_var = date_time.split("T")
        date=date_var[0]
    except:
        continue
    # i=[0,1,2,3]
    # j=[1,2,3,4]
    # for x,y in zip(i,j):
    #     if x<=mag<y:
    #         print("magniude[%d,%d]\t %s") % (x,y,1)
    # lat_boundry=latitude(lat)
    # print("latitude[%d,%d]\t %s") % (lat_boundry[0],lat_boundry[1],1)
    day_by_day(date,mag)
[12:51 AM, 6/21/2016] Nanda: 