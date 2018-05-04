# Python2 scripts for memory-efficient genomic analysis

Each script comes with its own help description

# proximate_snps.py
Determine the number of nearby SNPs using a SNP table. Useful for designing primers.  

Run with arguments from command line

Input: Table with sorted SNP positions. First two columns must be 1)Chromosome 2)Position  
Output: For each SNP, the number of nearby SNPs in a specified window, and the location of the closest SNP

### Arguments
-i input: Input table that has 1)CHR 2)POS   
-o ouput: Output table  
-r range: Integer range of bases around SNP to look for other snps  
-s skip: Number of lines to skip for headings in input file. Default is that header is present(1)

# replace_fasta.py
Mask a reference assembly by a list of snp positions (CHR,POS). Replace the allele at a given position with a user-specified allele

Useful for primer design or masking known problematics regions of a assembly

NOTE: makes replacements within FASTA file - it is recommended to backup the FASTA file first. 

### Arguments
-i input: Input FASTA file  
-p positions file: Table with [CHR POS] to mask  
-a allele mask: Letter to mask bases with   

# grab_fasta.py
Pull sequences from a FASTA file around user-specificed SNP positions.

Useful for primer design.

### Arguments
-i input: Input FASTA file  
-o output file: Output table with sequences  
-p positions file: Table with [CHR POS] to pull sequences around  
-r sequence range: Integer; number of bases around SNP to grab  
-f output format: Output in FASTA format or CSV (two-column)  

# amplicon_stats.py
A script to analyze selected primers and design probe sequences.  
Requires a table of [CHR_POS, PRODUCT_SEQUENCE, F_PRIMER, R_PRIMER] for each locus

Use to design probes from amplicons and check primers 

### Arguments
-i input: Input CSV with: Col1: CHR_POS; Col2: Product sequence (5'-3'); Col3: Fprimer; Col4: Rprimer  
-o ouput table: Table with stats and warnings on primers  
-r probe range: Integer for desired sequence length around probe 
