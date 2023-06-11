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

file_list = sorted(Path('/opt/home/thompsonlab/Riboseq_HY/ribominer/ribosome_distribution/Ribo/non_miRNA').glob('*.csv'))

main_dataframe = []
for f in file_list:
    data = pd.read_csv(f, usecols=[0, 2], keep_default_na = False)
    df = pd.DataFrame(data)
    df.columns.values[0] = 'transcript_id'
    f_name = os.path.basename(f).split('.')[0][23:]
    df.columns.values[1] = 'log2FoldChange' + f_name
    df.set_index('transcript_id', inplace = True)
    main_dataframe.append (df)

df_all = pd.concat(main_dataframe, axis = 1)
df_all.to_csv('final_logFC_Ribo_nonmiRNA.txt', index = True, sep = '\t', header = True)
