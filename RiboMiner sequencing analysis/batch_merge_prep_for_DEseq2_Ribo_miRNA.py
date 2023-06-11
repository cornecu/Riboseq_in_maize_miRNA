#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
Hailong create this scripts to batch prepare the file for DESeq2 analysis.
'''

import sys, os
import numpy as np
import pandas as pd
import glob
''' The glob module in python is used to retrieve files or pathnames matching a specified pattern'''
  
folder_path = '/opt/home/thompsonlab/Riboseq_HY/ribominer/ribosome_distribution/Ribo/miRNA'
file_list = glob.glob(folder_path + "/*.txt")
## index_col will tell us which column as the index column
main_dataframe = pd.DataFrame(pd.read_table(file_list[0], index_col = 'transcript_id'))
  
for i in range(1,len(file_list)):
    data = pd.read_table(file_list[i], index_col = 'transcript_id')
    df = pd.DataFrame(data)
    ## axis =1 will tell us to merge based on the index names
    main_dataframe = pd.concat([main_dataframe, df], axis = 1)
  
for c in main_dataframe.columns:
    main_dataframe[c].to_csv(c + '.txt', index = True, sep = '\t', header = False)
