#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from Bio import SeqIO
import time
import sys, os

inputFile = sys.argv[1]

names = [os.path.basename(inputFile).split('.')[0]]

start = time.time() 

seen = set()
records = []

for record in SeqIO.parse(inputFile, "fasta"):  
    if str(record.seq) not in seen:
        seen.add(record.seq)
        records.append(record)


#writing to a fasta file
SeqIO.write(records, '{names}_noduplicate.fa', "fasta")
end = time.time()

print(f"Run time is {(end- start)/60}") 