#!/bin/bash
# create one folder for splitting fq files mapping
cd
cd ~/old_machine_stuff/thompsonlab/Riboseq_HY/Riboseq_merge_sep18_19/
mkdir split_fq_mapping
cd

cd ~/old_machine_stuff/thompsonlab/Riboseq_HY/Riboseq_merge_sep18_19/trimmed_fq/split_fq/
### start to get file
for f2 in *.fastq
do
  ~/old_machine_stuff/thompsonlab/programs/STAR-2.7.7a/bin/Linux_x86_64_static/STAR --runThreadN 16 --genomeDir ~/old_machine_stuff/thompsonlab/Riboseq_HY/reference_v4_Riboseq_chr_ctg_STAR/ \
   --readFilesIn ~/old_machine_stuff/thompsonlab/Riboseq_HY/Riboseq_merge_sep18_19/trimmed_fq/split_fq/"$f2" \
   --alignIntronMin 20 --outSAMtype BAM Unsorted --sjdbGTFfile ~/old_machine_stuff/thompsonlab/Riboseq_HY/v4/Zea_mays.B73_RefGen_v4.49.ribocode_step7_noPtMt.gtf \
   --sjdbOverhang 49 --outFilterScoreMinOverLread 0 --outFilterMatchNminOverLread 0 --outFilterMatchNmin 12 --outFilterMultimapNmax 1 \
   --quantMode TranscriptomeSAM --outSAMattributes All --outFileNamePrefix ~/old_machine_stuff/thompsonlab/Riboseq_HY/Riboseq_merge_sep18_19/split_fq_mapping/"${f2%.*}"/
done
