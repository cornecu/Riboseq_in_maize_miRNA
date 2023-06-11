library("DESeq2")
library("vsn")
library("pheatmap")
library("RColorBrewer")

directory <- "~/path/to/folder"

sampleFiles <-c('N1_bin_*.txt','N2_bin_*.txt','N3_bin_*.txt','fzt1_bin_*.txt','fzt2_bin_*.txt','fzt3_bin_*.txt')
condition <- c('N','N','N','fzt','fzt','fzt')
sampleTable <- data.frame(sampleName = sampleFiles,
                          fileName = sampleFiles,
                          condition = condition)

ddsHTSeq <- DESeqDataSetFromHTSeqCount(sampleTable = sampleTable, directory = directory, design= ~ condition)

#Note on factor levels
ddsHTSeq$condition <- factor(ddsHTSeq$condition, levels = c("N","fzt"))
ddsHTSeq$condition <- relevel(ddsHTSeq$condition, ref="N")
#DEG analysis
dds <- DESeq(ddsHTSeq)
# head(dds)
res<-results(dds)
# extract normalized count in each condition
# foo <- counts(dds, normalized = TRUE)
# write.csv(foo, file="dds_norm_counts_bin_*.csv") 
# plot MAplot with adjust value less than 0.05
# plotMA(dds,alpha = 0.05)
# write stats output table
write.csv(as.data.frame(res), file = "fzt_vs_N_3bioreplicate_bin_*.csv")
