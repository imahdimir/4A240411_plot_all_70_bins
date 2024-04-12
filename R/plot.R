#!/usr/bin/env Rscript

library("data.table")
library("dplyr")
library("plinkFile")
library("genio")
library("ggplot2")
library("glue")
library('readxl')



plot_corr <- function(dta_fp, pair_name, gtype_name, info_score, fpo) 
  {
  df <- read_excel(dta_fp, col_names = T)
  names(df) = c('snp', 'corr')
  df <- na.omit(df)
  
  n_snps <- nrow(df)
  dn = info_score / 100
  
  ggplot(data.frame(df), aes(x = corr)) +
    geom_histogram(binwidth = 0.02, fill = "#56B4E9", colour = "#56B4E9", alpha = 0.5) +
    labs(title = glue('{pair_name}, {gtype_name}, SNPS with INFO = {dn} - {dn+0.01} (n = {n_snps})'),
         x = "Genotype Correlation",
         y = "Count") +
    geom_vline(xintercept=0.5, linetype="dotted") +
    geom_vline(xintercept=mean(df$corr), linetype="dashed", color = 'red') +
    theme_classic() +
    theme(legend.position="none")
  
  ggsave(fpo)
  }

info <- seq(30, 99, 1)

in_0 <- '/Users/mmir/Library/CloudStorage/Dropbox/inp'
out_0 <- '/Users/mmir/Library/CloudStorage/Dropbox/temp'

dirn <- 'FS_DSG'

dta_dir <- glue('{in_0}/{dirn}')
out_dir <- glue('{out_0}/{dirn}')

prd <- expand.grid(out_dir, dta_dir, 'Full Sibs', 'Dosages', info)


dirn <- 'FS_HC'

dta_dir <- glue('{in_0}/{dirn}')
out_dir <- glue('{out_0}/{dirn}')

prd1 <- expand.grid(out_dir, dta_dir, 'Full Sibs', 'Hard-Call', info)

prd <- rbind(prd, prd1)


dirn <- 'PO_DSG'

dta_dir <- glue('{in_0}/{dirn}')
out_dir <- glue('{out_0}/{dirn}')

prd1 <- expand.grid(out_dir, dta_dir, 'Parent-Offspring', 'Dosages', info)

prd <- rbind(prd, prd1)

dirn <- 'PO_HC'

dta_dir <- glue('{in_0}/{dirn}')
out_dir <- glue('{out_0}/{dirn}')

prd1 <- expand.grid(out_dir, dta_dir, 'Parent-Offspring', 'Hard-Call', info)

prd <- rbind(prd, prd1)

x <- 1
pair_name = prd[x, 'Var3']
gtype_name = prd[x, 'Var4']
info_score = prd[x, 'Var5']
dta_fp = glue("{prd[x, 'Var2']}/i{info_score}.xlsx")
fpo = glue("{prd[x, 'Var1']}/i{info_score}.png")

plot_corr(dta_fp,pair_name,gtype_name,info_score, fpo)

for (x in 1:nrow(prd))
  {
  pair_name = prd[x, 'Var3']
  gtype_name = prd[x, 'Var4']
  info_score = prd[x, 'Var5']
  dta_fp = glue("{prd[x, 'Var2']}/i{info_score}.xlsx")
  fpo = glue("{prd[x, 'Var1']}/i{info_score}.png")
  
  plot_corr(dta_fp,pair_name,gtype_name,info_score, fpo)
  }

