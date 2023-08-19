#!/bin/bash

cd
cd ~/old_machine_stuff/thompsonlab/Riboseq_HY/Riboseq_merge_sep18_19/split_fq_mapping/
### start to get file

for file in fztR1*
do
  mv "${file}" "${file//\_S4_R1_001_merge.3adapter4clips.5adapter4clips.length1.noNCBIrRNAnotRNA/}"
done
sleep 2s
for file in fztR2*
do
  mv "${file}" "${file//\_S5_R1_001_merge.3adapter4clips.5adapter4clips.length1.noNCBIrRNAnotRNA/}"
done
sleep 2s
for file in fztR3*
do
  mv "${file}" "${file//\_S6_R1_001_merge.3adapter4clips.5adapter4clips.length1.noNCBIrRNAnotRNA/}"
done
sleep 2s
for file in NR1*
do
  mv "${file}" "${file//\_S1_R1_001_merge.3adapter4clips.5adapter4clips.length1.noNCBIrRNAnotRNA/}"
done
sleep 2s
for file in NR2*
do
  mv "${file}" "${file//\_S2_R1_001_merge.3adapter4clips.5adapter4clips.length1.noNCBIrRNAnotRNA/}"
done
sleep 2s
for file in NR3*
do
  mv "${file}" "${file//\_S3_R1_001_merge.3adapter4clips.5adapter4clips.length1.noNCBIrRNAnotRNA/}"
done