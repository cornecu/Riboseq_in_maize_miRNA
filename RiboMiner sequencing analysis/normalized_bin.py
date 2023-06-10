#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
import os,sys
import numpy as np

# python python_sum_bin.py miRNA_target_ribodensity_NR1_cds_codon_density_new.txt miRNA_target_ribodensity_NR1_cds_codon_density_test.txt
# vi %s/\[//g; %s/\]//g; %s/, /\t/g
# when I average them, make sure to add transcript	NR1 to the first line
'''input file'''
input_file = open(sys.argv[1],'r')
library_factor = sys.argv[2]
output_file = open(sys.argv[3],'w')
''' process each line'''
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
  gene_new_new = list(map(int, gene_new[1:]))
  if len(gene_new_new)<60:
   pass
  else:
  # convert integers of list to float of list
   # N = np.array(gene_new_new, dtype="float64")
   # print (gene_new_new)
   new_list = np.divide(gene_new_new, library_factor, dtype="float64", casting='unsafe')
   new_list_new = np.multiply (new_list, 10 ** 6, dtype="float64", casting='unsafe')
  # new_list = [x / library_factor * (10 ** 6) for x in N]
  # insert gene id at index 0 (the beginning of list)
  # new_list.insert(0, gene_new[0])
  #add comma into the list
   my_string = ','.join(map(str, new_list_new)) 
   output_line_format = "%s\t%s\n" % (gene_new[0], my_string)
   output_file.write(output_line_format)

output_file.close() 
input_file.close()
