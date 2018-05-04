#!/usr/bin/env python

#Use a [CHR,SEQ,FPRIMER,RPRIMER] file to predict amplicon and success of primer

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest="input", required=True, help="Input Primer CSV")
    parser.add_argument('-o', '--output', dest="output", required=True, help="File with stats on primer picks")
    parser.add_argument('-r', '--range', type=int, dest="range", required=True, help= "Integer range around snp for probe")
    args = parser.parse_args()


f1 = open(args.output, "w")
heading= "Chr SEQ FP RP Amplicon Probe Len2SNP LenProbe NSNP NPOLY NDEL Warnings"
f1.write("%s\n" % heading)
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
repeats=(['GTGTGTGT','GAGAGAGA' , 'CTCTCTCT' , 'TATATATA' , 'TCTCTCTC' , 'ACACACAC' , 'GCGCGCGC'])
dictsF = {}
dictsR = {}
with open(args.input) as snp_list:
    iter=1
    for line in snp_list:
        chr, seq, Fp, Rp = line.rstrip().split()
        RpRC=''.join([complement[base] for base in Rp[::-1]])
        string_F = seq.split(Fp)[1]
        string_R = string_F.split(RpRC)[0]
        #Length to SNP
        seqL=len(string_R.split("X")[0])
        #Get number of variants in amplicon
        xct=string_R.count("X")
        lct=line.count("X")
        pct=string_R.count("P")
        dct=string_R.count("D")
        #Get position of SNP
        xpos=string_R.find('X')
        #Generate warnings
        xwarn=""; pwarn="" ;dwarn="";prwarn="";fwarn="";nwarn="";awarn="";rwarn=""
        if any(x in Fp for x in repeats):
            rwarn=("[PRIMER_STR]")
        if any(x in RpRC for x in repeats):
            rwarn=("[PRIMER_STR]")
        if (seqL> 70):
            fwarn=("[SNP_DISTANCE]")
        if (xct > 1):
            xwarn=("[SNP_NUMBER]")
        if Fp in dictsF.viewvalues():
            prwarn=("[DUP_PRIMER]")
        if RpRC in dictsR.viewvalues():
            prwarn=("[DUP_PRIMER]")
        dictsF[iter] = Fp
        dictsR[iter] = RpRC
        if ((xpos < 1) or (xpos + 1) == len(string_R)):
            pwarn=("[SNP_LOCATION]")
        string_X= string_R.replace("D","P")
        try:
            upS = string_X.split("X")[1][:(args.range)]
        except IndexError:
            upS = ''
        try:
            dwS = string_X.split("X")[0][-(args.range):]
        except IndexError:
            dwS = ''
        try:
            upS2 = upS.split ("P")[0][:(args.range)]
            DP1= float((len(upS2) + 0.01) / (len(upS) +0.01))
            if (DP1 <= 0.25):
                nwarn=("[POLY_PROXY]")
        except IndexError:
            upS2 = upS
        try:
            dwS2 = dwS.split ("P")[::-1][0][-(args.range):]
            DP2= float((len(dwS2) + 0.01) / (len(dwS) +0.01))
            if (DP2 <= 0.25):
                nwarn=("[POLY_PROXY]")
        except IndexError:
            dwS2 = dwS
        amplicon=(dwS2 + "X" + upS2)
        alen=len(amplicon)
        if ((alen-1) > 0):
            aca=float(amplicon.count("A"))/(alen-1) ; acc=float(amplicon.count("C"))/(alen-1)
            act=float(amplicon.count("T"))/(alen-1) ; acg=float(amplicon.count("G"))/(alen-1)
            diverse=[aca,act,acg,acc]
            d1=1
            d2=1
            if (sum(i > 0.5 for i in diverse) >0 ):
                d1=0
            if (sum(i > 0 for i in diverse) <4):
                d2=0
            if ((d1+d2)==0):
                 dwarn=("[DIVERSITY]")
            if (alen < 10):
                 awarn=("[PROBE_LENGTH]")
        warnings=(xwarn + pwarn + dwarn + prwarn + fwarn + nwarn + awarn + rwarn)
        if (len(string_R) < 2) or (string_R == "") or (amplicon == "")  :
            amplicon=("NA")
            string_R=("NA")
            warnings=("[BAD_AMPLICON]")
        hout=(chr + " " + seq + " " + Fp + " " + Rp +" " + string_R + " " + amplicon + " " + str(seqL) + " " + str(alen) + " " + str(xct) + " " + str(pct) + " " + str(dct) + " " + warnings)
        f1.write("%s\n" % hout)
        iter=iter+1
f1.flush()
print("Done")
