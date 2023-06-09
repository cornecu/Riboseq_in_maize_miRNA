#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
HY modification from @Author: Li Fajin
usage: python enrichement_FC.py miRNA_target_ribodensity_60bins_normalized_N_mean.txt,miRNA_target_ribodensity_60bins_normalized_fzt_mean.txt miRNA_target_ribodensity_60bins_normalized_N/fzt

'''

import sys
import numpy as np
# to supress error or warning
np.seterr(divide='ignore', invalid='ignore')
from functools import reduce
from collections import defaultdict
# The functionality of both dictionaries and defualtdict are almost
# same except for the fact that defualtdict never raises a KeyError.
# It provides a default value for the key that does not exists
# we can pass list to the defaultdict

def get_density_dict(densityFile):
 # initialize the empty dictionary
 density_dict={}
 with open(densityFile,'r') as f:
  i=0
  # read line by line and get the number of lines
  for line in f:
   i+=1
   if i==1:
    continue
   # delete the empty space before and end of each line and convert it
   # into one list
   tmp=line.strip().split("\t")
   # assign first element to transcript id
   trans_id=tmp[0]
   # form the dict, use one key as index of all the rest of list values 
   density_dict[trans_id]=[float(i) for i in tmp[1:]]
 return density_dict
 # will be like {id_1: [count,count,..], id_2: [count,count,..]}

def flatten(xs):
 for x in xs:
  # If the type parameter is a tuple, 
  # this function will return True if the object is one of the types in the tuple
  if isinstance(x,tuple):
   for xx in flatten(x):
    yield xx
  else:
   yield x

def meanDensity(inputFiles,outprefix):
 all_ratio_dict=defaultdict(list)
 for f in inputFiles:
  ratio_dict=get_density_dict(f)
  # get {id_1: [count,count,..], id_2: [count,count,..]}
  # ratio_dict.items() will return ratio_dict_items([('id1', [count,count,..]), ('id2', [count,count,..]), ..])
  for trans,ratio in ratio_dict.items():
   all_ratio_dict[trans].append(ratio)
   # will be like this defaultdict(<class 'list'>, {id1: [count,count,..], id2: [count,count,..], ..})
 with open(outprefix+"_FC_ratio.txt",'w') as fout:
  fout.write("%s\t%s\n" %("transcript","FC_ratio"))
  # all_ratio_dict.items() will return all_ratio_dict_items([('id1', [count,count,..]), ('id2', [count,count,..]), ..])
  for trans,ratio in all_ratio_dict.items():
   # reduce and map function differences https://stackoverflow.com/questions/49934992/main-difference-between-map-and-reduce
   a = [list(flatten(i)) for i in list(reduce(zip,all_ratio_dict[trans]))]
   # to check what it looks like
   # print (trans, a)
   # print (type(a))
   # read_counts_pair = []
   # for line in a:
       # read_counts_pair.append(line)
   # print (trans, read_counts_pair)
   # for i in read_counts_pair:
    # print (i)
   #for i in range(len(a)):
    #print (trans, a[i], a[i][1], type(a[i]), type(a[i][1]))
    # use np.float to avoid ZeroDivisionError: float division by zero
    # use traditional divide (np.divide is generally used for array dividing)
   FC_ratio=np.array(list(np.float64(a[i][1])/np.float64(a[i][0]) for i in range(len(a))))
   fout.write("%s\t" %(trans))
   for i in range(len(FC_ratio)):
    fout.write("%s\t" %str(FC_ratio[i]))
   fout.write("\n")

if __name__=="__main__":
 input_file = sys.argv[1]
 inputFiles = input_file.strip().split(",")
 outprefix = "miRNA_target_ribodensity_60bins_normalized_fzt_N"
 meanDensity(inputFiles,outprefix)
