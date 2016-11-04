#!/usr/bin/env python

import csv
import sys

def mapper():
    for row in sys.stdin:
        row = row.strip()
        data = next(csv.reader([row], delimiter='\t'))

        if len(data) != 8:
           continue

        _, author, body, _, ups, downs, _, _ = data 

        print('{}\t{}\t{}'.format(author, ups, len(body.split(' '))))

if __name__ == "__main__":
    mapper()