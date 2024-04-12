#!/usr/bin/env Rscript

library("data.table")
library("dplyr")
library("plinkFile")
library("genio")
library("ggplot2")
library("glue")
library('readxl')
library(writexl)


dta_fn <- '/Users/mmir/Library/CloudStorage/Dropbox/corrs.xlsx'

dta <- read_excel(dta_fn)

colnames(dta)[3] <- 'Info'

dta$se = dta$std / sqrt(dta$n_snps)
dta$Info = dta$Info / 100

l1 <- c("Siblings (Dosages)", 'Parent-Offspring (Dosages)', 'Siblings (Hard Call)', 'Parent-Offspring (Hard Call)')
l2 <- c("Siblings", "Parent-Offspring")

# plot correlations
ggplot(dta, aes(x = Info, y = mean, color=interaction(InfType, Genotype), shape=InfType)) +
  geom_point() +
  geom_errorbar(aes(ymin=mean-1.96*se, ymax=mean+1.96*se), width=.01) +
  geom_line() +
  geom_hline(yintercept=0.5, linetype="dashed") +
  scale_color_discrete(labels=l1) +
  scale_shape_discrete(labels=l2) + 
  theme_classic() +
  labs(x = "INFO Score", y = "Mean Genotype Correlation")


  
ofn <- '/Users/mmir/Library/CloudStorage/Dropbox/mean_gt_corr.png'

ggsave(ofn)


ofn <- '/Users/mmir/Library/CloudStorage/Dropbox/C1-P-G/A1-Git-SF/summary-stats-plot-4-pairs-corr-240405-SF/out/corrs.xlsx'

write_xlsx(dta, ofn)




