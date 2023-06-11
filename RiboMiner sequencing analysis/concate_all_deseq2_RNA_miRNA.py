#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
Hailong create this scripts to batch prepare the file for DESeq2 analysis.

'''

import sys, os
import numpy as np
import pandas as pd
import glob
from pathlib import Path
''' The glob module in python is used to retrieve files or pathnames matching a specified pattern'''
##### import the file
# importing packages
  

file_list = sorted(Path('/opt/home/thompsonlab/Riboseq_HY/ribominer/ribosome_distribution/RNA/miRNA').glob('*.csv'))
# names = [os.path.basename(f).split('.')[0][23:] for f in file_list]
#print (names)
## index_col will tell us which column as the index column
# main_dataframe = pd.DataFrame(pd.read_csv(file_list[0], usecols=[0, 2], keep_default_na = False))
# main_dataframe.columns.values[0] = 'transcript_id'
# main_dataframe.set_index('transcript_id', inplace = True)
# name_1 = os.path.basename(file_list[0]).split('.')[0][23:]
# main_dataframe.rename('_')
# print (name_1)
# print (main_dataframe)

main_dataframe = []
for f in file_list:
    # names = [os.path.basename(f).split('.')[0][23:]]
    data = pd.read_csv(f, usecols=[0, 2], keep_default_na = False)
    df = pd.DataFrame(data)
    df.columns.values[0] = 'transcript_id'
    f_name = os.path.basename(f).split('.')[0][23:]
    df.columns.values[1] = 'log2FoldChange' + f_name
    df.set_index('transcript_id', inplace = True)
    main_dataframe.append (df)

df_all = pd.concat(main_dataframe, axis = 1)
df_all.to_csv('final_logFC_RNA_miRNA.txt', index = True, sep = '\t', header = True)

    # df.set_index('transcript_id', inplace = True)
    # add filename to column and i use df.add_suffixes and df.add_prefix t
    # df.add_suffix(names)
    # df.to_csv('{names}_logFC.txt', index = True, sep = '\t', header = True)
    ## axis =1 will tell us to merge based on the index names
    #main_dataframe = pd.concat([main_dataframe, df], axis = 1, keys = names)
    # main_dataframe = pd.concat([main_dataframe, df], axis = 1)
# print(main_dataframe)
  
# creating a new csv file with
# the dataframe we created
# main_dataframe.to_csv('final_logFC.txt', index = True, sep = '\t', header = True)

# for c in main_dataframe.columns:
    #main_dataframe[c].to_csv(c + '.txt', index = True, sep = '\t', header = False)