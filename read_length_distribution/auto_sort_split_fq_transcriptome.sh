#!/bin/bash
cd
cd ~/old_machine_stuff/thompsonlab/Riboseq_HY/Riboseq_merge_sep18_19/split_fq_mapping/

for file in *
do
  (cd "${file}" &&
  samtools sort -o "${file}"_ribo_transcriptome_sort.bam Aligned.toTranscriptome.out.bam &&
  samtools index "${file}"_ribo_transcriptome_sort.bam
  )
done