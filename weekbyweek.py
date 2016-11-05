#!/usr/bin/python
from collections import defaultdict
import sys
import datetime
weeks = defaultdict(dict)
for line in sys.stdin.readlines():
        #remove leading and trailing whitespace
        line = line.strip()
    # split the line into words
        row = line.split(',')
        try:
            mag=float(row[4])
            var=row[0].split("T")
            datevar=var[0]
            dayvar=datevar.split('-')
           
            #week=datetime.tdate.isocalendar()
            #print("yes")
            
        
        except:
            continue
        #print("%s\t%s")%(tdate,mag)
        tdate = datetime.date(int(dayvar[0]),int(dayvar[1]),int(dayvar[2]))
        _, week_number, day_number = tdate.isocalendar()
        week = "week_{}".format(week_number)
        print("%d-%d-%s\t%r")%(int(dayvar[0]),int(dayvar[1]),week,mag)