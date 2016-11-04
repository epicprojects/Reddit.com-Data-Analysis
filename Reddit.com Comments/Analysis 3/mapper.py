#!/usr/bin/env python

import csv
from datetime import datetime
import sys

def mapper():
    for row in sys.stdin:
        row = row.strip()
        data = next(csv.reader([row], delimiter='\t'))
        mentioned = 0

        if len(data) != 8:
            continue

        sub, _, body, created_utc, _, _, _, _ = data

        dt = datetime.utcfromtimestamp(float(created_utc))
        date = dt.strftime('%Y-%m-%d')

        if sub != 'nfl':
            continue

        if 'deflategate' in body.lower():
            mentioned = 1
        elif 'brady' in body.lower():
            mentioned = 1

        print('{}\t{}\t{}'.format(sub, date, mentioned))

if __name__ == "__main__":
    mapper()