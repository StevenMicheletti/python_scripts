#!/usr/bin/env python

#Use a snp position list to pull flanking sequence from a reference FASTA file

from pyfaidx import Fasta
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest="input", required=True, help="Input FASTA file")
    parser.add_argument('-o', '--output', dest="output", required=True, help="File with SNP positions, CHR SNP")
    parser.add_argument('-p', '--positions',dest="positions", required=True, help= "File with CHR and SNP positions")
    parser.add_argument('-r', '--range', type=int, dest="range", required=True, help= "Integer range to grab up and downstream from SNP")
    parser.add_argument('-f', '--format', type=str, dest="format", required=False, help= "Output format; csv or fasta")
    args = parser.parse_args()

print("Pulling from FASTA")
f1 = open(args.output, "w")
with open(args.positions) as snp_list:
    with Fasta(args.input) as fasta:
        for line in snp_list:
            pos, snp = line.rstrip().split()
            downer=(int(snp) - (args.range +1))
            if(downer < 1):
                 downer=1
            upper=(int(snp) + args.range)
            if (args.format == "csv"):
                hout=(str(pos) + "_" + str(snp) + " " + str(fasta[pos][downer:upper]))
                f1.write("%s\n" % hout)
            else:
                hout=(">"+ str(pos) + "_" + str(snp))
                sout=(fasta[pos][downer:upper])
                f1.write("%s\n" % hout) ; f1.write("%s\n" % sout)
f1.flush()
print("Done")