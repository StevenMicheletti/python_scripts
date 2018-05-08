#!/usr/bin/env python

#Turn a 2-column csv into fasta format

import argparse

#input, output, range 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest="input", required=True, help="Input csv with id and sequence")
    parser.add_argument('-o', '--output', dest="output", required=True, help="Name of output file")
    parser.add_argument('-s', '--skip', type=int, dest="skip", default=0, help="Number of lines to skip in input file (e.g., if header present)")
    args = parser.parse_args()

f1 = open(args.output, "w")

with open (args.input) as f:
    if ((args.skip) > 0):
       next (f)
    for line in f:
         pos, seq = line.rstrip().split()
         f1.write("%s\n" % (">" + pos))
         f1.write("%s\n" % seq)
f1.flush()
print("Done")
