#!/usr/bin/env python
from __future__ import division
import sys

def reducer():

    love_count = 0
    hate_count = 0
    old_sub = None
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 3:
            continue

        this_sub, love, hate = data

        if old_sub and old_sub != this_sub:

            full_love = (love_count - hate_count)/(love_count + hate_count)
            print("{}\t{}".format(old_sub, full_love))

            love_count = 0
            hate_count = 0

        old_sub = this_sub
        love_count += int(love)
        hate_count += int(hate)
    else:
        full_love = (love_count - hate_count)/(love_count + hate_count)
        print("{}\t{}".format(old_sub, full_love))

if __name__ == "__main__":
    reducer()