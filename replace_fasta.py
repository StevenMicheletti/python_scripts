#!/usr/bin/env python

#proximate_snps.py
#Determines number of flanking snps within a specified window
#Determines closest SNP

from pyfaidx import Fasta
import sys
import re
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest="input", required=True, help="Input FASTA file")
    parser.add_argument('-p', '--positions', dest="positions", required=True, help="File with CHR and SNP positions")
    parser.add_argument('-a', '--allele', type=str, dest="allele", required=True, help= "Letter used to replace positions")
    args = parser.parse_args()

num_lines = sum(1 for line in open(args.positions))

print("Replacing fasta positions: "),
print(num_lines)

with open(args.positions) as mut_table:
    with Fasta(args.input, mutable=True) as fasta:
        for line in mut_table:
           pos, base = line.rstrip().split()
           base=(int(base)-1)
           fasta[pos][base] = args.allele
        print("Done")
