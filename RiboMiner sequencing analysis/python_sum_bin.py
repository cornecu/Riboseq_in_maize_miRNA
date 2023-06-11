#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
import itertools
from itertools import groupby
import os,sys
import numpy as np
import pandas as pd

# python python_sum_bin.py miRNA_target_ribodensity_NR1_cds_codon_density_new.txt miRNA_target_ribodensity_NR1_cds_codon_density_test.txt
# vi %s/\[//g; %s/\]//g; %s/, /\t/g
'''input file'''
input_file = open(sys.argv[1],'r')
output_file = open(sys.argv[2],'w')
'''output_file.write('transcript_id\tbin_count%\n')'''

''' process each line'''
bins = 60
read_counts_vector = []
# read each line by line
with input_file as my_file:
   for line in my_file:
    read_counts_vector.append(line)
# for each element in the list, process each element as new list
for gene in read_counts_vector:
  # Converting string to list
  gene_new = gene.split('\t')
  # print (type(gene))
  # print (type(gene_new))
  # print (gene_new)
  # convert string of list to integer of list and drop transcriptid and \n
  gene_new_new = list(map(int, gene_new[1:-1]))
  # print (gene_new_new)
  if len(gene_new_new)<60:
   pass
  else:
   steps = int(len(gene_new_new)/bins)
   read_counts_vector_scaled=np.zeros(bins,dtype=np.int64)
   # sum all the read number in each bin
   tmp_read_counts_vector_scaled=[np.sum(gene_new_new[i:(i+steps)]) for i in np.arange(0,len(gene_new_new),steps)]
   read_counts_vector_scaled[:]+=tmp_read_counts_vector_scaled[:bins]
   read_counts_vector_scaled[-1]=np.sum(tmp_read_counts_vector_scaled[(bins-1):])
   # i can format like output_line = ["%s\t" % (str(read_counts_vector_scaled[i])) for i in range(bins)]
   output_line = [int(read_counts_vector_scaled[i]) for i in range(bins)]
   output_line_format = "%s\t%s\n" % (gene_new[0], output_line)
   output_file.write(output_line_format)

output_file.close() 
input_file.close()
