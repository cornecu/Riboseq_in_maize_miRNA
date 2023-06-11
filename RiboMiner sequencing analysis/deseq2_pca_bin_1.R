library("DESeq2")
library("vsn")
library("pheatmap")
library("RColorBrewer")

directory <- "~/Documents/riboseq/sequencing_submit/2020_8_31/Ribosome_occupancy_distribution/Ribo/miRNA"

sampleFiles <-c('N1_bin_1.txt','N2_bin_1.txt','N3_bin_1.txt','fzt1_bin_1.txt','fzt2_bin_1.txt','fzt3_bin_1.txt')
condition <- c('N','N','N','fzt','fzt','fzt')
sampleTable <- data.frame(sampleName = sampleFiles,
                          fileName = sampleFiles,
                          condition = condition)

ddsHTSeq <- DESeqDataSetFromHTSeqCount(sampleTable = sampleTable, directory = directory, design= ~ condition)
# ddsHTSeq

# prefilter lower counts, don't filter based on authors
# keep <- rowSums(counts(ddsHTSeq)) >= 5
# ddsHTSeq <- ddsHTSeq[keep,]

#Note on factor levels
ddsHTSeq$condition <- factor(ddsHTSeq$condition, levels = c("N","fzt"))
ddsHTSeq$condition <- relevel(ddsHTSeq$condition, ref="N")
#DEG analysis
dds <- DESeq(ddsHTSeq)
# head(dds)
res<-results(dds)
# res
# extract normalized count in each condition
# foo <- counts(dds, normalized = TRUE)
# write.csv(foo, file="dds_norm_counts_bin_1.csv") 
# plot MAplot with adjust value less than 0.05
# plotMA(dds,alpha = 0.05)
# write stats output table
write.csv(as.data.frame(res), file = "fzt_vs_N_3bioreplicate_bin_1.csv")
#Extracting transformed values
# vsd <- vst(dds, blind=FALSE)
# rld <- rlog(dds, blind=FALSE)
# head(assay(vsd), 3)

#normalize data for clustering/heatmap analysis

# rld <- rlogTransformation(dds, blind=TRUE)
# ntd <- normTransform(dds)
# notAllZero <- (rowSums(counts(dds))>0)
# PCA

# library(ggplot2)
# z<-plotPCA(rld, intgroup=c("condition"))
# nudge <- position_nudge(y = 1)
# z + geom_text(aes(label = name), position = nudge)

