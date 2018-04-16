#!/usr/bin/env python

#proximate_snps.py
#Determines number of flanking snps within a specified window
#Determines closest SNP

import argparse
import pandas as pd 
import numpy as np
from time import gmtime, strftime

#input, output, range 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest="input", required=True, help="Sorted input file that must have Chr and Pos in first two columns")
    parser.add_argument('-o', '--output', dest="output", required=True, help="Name of output file")
    parser.add_argument('-r', '--range', type=int, dest="range", required=True, help= "Window +/- to count number of proximate SNPs ")
    parser.add_argument('-s', '--skip', type=int, dest="skip", default=1, help="Number of lines to skip in input file (e.g., if header present)")
    args = parser.parse_args()

startime=strftime("%Y-%m-%d %H:%M:%S", gmtime())
print("Running at"), 
print(startime)

f1 = open(args.output, "w")
chunksize = 500000
load=1
for chunk in pd.read_csv(args.input, delim_whitespace=True, chunksize=chunksize, skipinitialspace=args.skip, usecols=[0,1]):
    header1=np.asarray(chunk.iloc[:,0])
    counter=np.asarray(chunk.iloc[:,1])
    print("Block"),
    print(load) ,
    print("processing") ,
    print(len(counter)) ,
    print("records")

    iter=0
    for x in np.nditer(counter):
         lower=iter-args.range
         if lower <= 0 :
             lower =0
         higher=iter+args.range
         if iter > 0 :
             lowerD= counter[iter] - counter[iter-1]
         else:
             lowerD=10000
         if iter==(len(counter)-1):
             uppderD=lowerD
         else:
             upperD= counter[iter+1] - counter[iter]
         if upperD < 1 :
             upperD=10000
         fer=counter[lower:higher]
         d=str(min(np.array([upperD,lowerD])))
         c=str(len(np.where(np.logical_and(fer>=(x-args.range), fer<=(x+args.range)))[0]))
         b=str(x)
         a=str(header1[iter])
         Vout1=(a + " " + b + " " + c + " " + d )
         iter=iter+1
         f1.write("%s\n" % Vout1)
    load=load+1
f1.flush()
endtime=strftime("%Y-%m-%d %H:%M:%S", gmtime())
print("Done at"), 
print(endtime)
print("Output is [CHR], [POS], [N_SNPS], [BP_CLOSEST_SNP]")
