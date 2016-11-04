#!/usr/bin/env python

import csv
import sys

def mapper():
    for row in sys.stdin:
        #row = row.strip()
        data = next(csv.reader([row], delimiter='\t'))
        love, hate = 0, 0

        if len(data) != 8:
            continue

        sub, _, body, _, _, _, _, _ = data

        if 'love' in body.lower():
            love = 1

        if 'hate' in body.lower():
            hate = 1

        print('{}\t{}\t{}'.format(sub, love, hate))

if __name__ == "__main__":
    mapper()