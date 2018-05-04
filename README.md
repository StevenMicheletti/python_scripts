# Python2 scripts for memory-efficient genomic analysis

Each script comes with its own help description

## proximate_snps.py
Determine the number of nearby SNPs using a SNP table. Useful for designing primers.  

Run with arguments from command line

Input: Table with sorted SNP positions. First two columns must be 1)Chromosome 2)Position  
Output: For each SNP, the number of nearby SNPs in a specified window, and the location of the closest SNP

## replace_fasta.py
Mask a reference assembly by a list of snp positions (CHR,POS). Replace the allele at a given position with a user-specified allele

Useful for primer design or masking known problematics regions of a assembly

NOTE: makes replacements within FASTA file - it is recommended to backup the FASTA file first. 

### Arguments
-i input: Input FASTA file  
-p positions file: Table with [CHR POS] to mask  
-a allele mask: Letter to mask bases with   

## grab_fasta.py
Pull sequences from a FASTA file around user-specificed SNP positions.

Useful for primer design.

### Arguments
-i input: Input FASTA file  
-o output file: Output table with sequences  
-p positions: 

