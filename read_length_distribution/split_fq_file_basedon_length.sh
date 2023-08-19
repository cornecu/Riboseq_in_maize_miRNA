#!/bin/bash
cd old_machine_stuff/thompsonlab/Riboseq_HY/Riboseq_merge_sep18_19/trimmed_fq/
# create one folder for splitting fq files
mkdir split_fq

### start to get file
for f2 in *noNCBIrRNAnotRNA.fastq
do
  cutadapt -m 14 -M 14 -o split_fq/"${f2%.*}_14.fastq" "$f2"
  cutadapt -m 15 -M 15 -o split_fq/"${f2%.*}_15.fastq" "$f2"
  cutadapt -m 16 -M 16 -o split_fq/"${f2%.*}_16.fastq" "$f2"
  cutadapt -m 17 -M 17 -o split_fq/"${f2%.*}_17.fastq" "$f2"
  cutadapt -m 18 -M 18 -o split_fq/"${f2%.*}_18.fastq" "$f2"
  cutadapt -m 19 -M 19 -o split_fq/"${f2%.*}_19.fastq" "$f2"
  cutadapt -m 20 -M 20 -o split_fq/"${f2%.*}_20.fastq" "$f2"
  cutadapt -m 21 -M 21 -o split_fq/"${f2%.*}_21.fastq" "$f2"
  cutadapt -m 22 -M 22 -o split_fq/"${f2%.*}_22.fastq" "$f2"
  cutadapt -m 23 -M 23 -o split_fq/"${f2%.*}_23.fastq" "$f2"
  cutadapt -m 24 -M 24 -o split_fq/"${f2%.*}_24.fastq" "$f2"
  cutadapt -m 25 -M 25 -o split_fq/"${f2%.*}_25.fastq" "$f2"
  cutadapt -m 26 -M 26 -o split_fq/"${f2%.*}_26.fastq" "$f2"
  cutadapt -m 27 -M 27 -o split_fq/"${f2%.*}_27.fastq" "$f2"
  cutadapt -m 28 -M 28 -o split_fq/"${f2%.*}_28.fastq" "$f2"
  cutadapt -m 29 -M 29 -o split_fq/"${f2%.*}_29.fastq" "$f2"
  cutadapt -m 30 -M 30 -o split_fq/"${f2%.*}_30.fastq" "$f2"
  cutadapt -m 31 -M 31 -o split_fq/"${f2%.*}_31.fastq" "$f2"
  cutadapt -m 32 -M 32 -o split_fq/"${f2%.*}_32.fastq" "$f2"
  cutadapt -m 33 -M 33 -o split_fq/"${f2%.*}_33.fastq" "$f2"
  cutadapt -m 34 -M 34 -o split_fq/"${f2%.*}_34.fastq" "$f2"
  cutadapt -m 35 -M 35 -o split_fq/"${f2%.*}_35.fastq" "$f2"
  cutadapt -m 36 -M 36 -o split_fq/"${f2%.*}_36.fastq" "$f2"
  cutadapt -m 37 -M 37 -o split_fq/"${f2%.*}_37.fastq" "$f2"
  cutadapt -m 38 -M 38 -o split_fq/"${f2%.*}_38.fastq" "$f2"
  cutadapt -m 39 -M 39 -o split_fq/"${f2%.*}_39.fastq" "$f2"
  cutadapt -m 40 -M 40 -o split_fq/"${f2%.*}_40.fastq" "$f2"
  cutadapt -m 41 -M 41 -o split_fq/"${f2%.*}_41.fastq" "$f2"
  cutadapt -m 42 -M 42 -o split_fq/"${f2%.*}_42.fastq" "$f2"
  cutadapt -m 43 -M 43 -o split_fq/"${f2%.*}_43.fastq" "$f2"
done
