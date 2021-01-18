# What have we learned from the first 500 avian genomes? <br /> Annu. Rev. Ecol. Syst. Evol

G. A. Bravo, C. J. Schmitt, S. V. Edwards 
01/17/2021

## This script recreates figure 2 - a plot showing the number of loci (on a natural log scale) through time for avian phylogenomic studies

The data: phylogenomic_stats.csv

The R code:

```
## load packages
library(tidyverse)
library(ggthemes)
library(ggrepel)

## load dataset
phylogenomic_stats <- read.csv("/Users/schmitty/Documents/CJS/projects/bird_genome_review/phylogenomic_stats.csv")

## convert # of loci and # of spp to numeric
phylogenomic_stats$n_loci <- as.numeric(phylogenomic_stats$n_loci)
phylogenomic_stats$n_spp <- as.numeric(phylogenomic_stats$n_spp)

## plot natural log # of loci by year and color points by marker type
ggplot(data=phylogenomic_stats) +
  geom_smooth(aes(x=year, y=log(n_loci)), method = 'glm', color = "black") +
  geom_point(aes(x=year, y=log(n_loci),fill=loci_type, shape = priori_posteriori),
             position = position_jitter(width = 0.1, height = 0.5, seed=8),
             size=2,
             width = .3,
             height = .3,
             alpha = .75) +
  labs(x="Year", y="log ( number of loci )") +
  scale_fill_manual(values = c("3' UTR" = colorblind_pal()(8)[1],
                               "CNEE" = colorblind_pal()(8)[2],
                               "exon" = colorblind_pal()(8)[3],
                               "indel" = colorblind_pal()(8)[4],
                               "intron" = colorblind_pal()(8)[5],
                               "RADseq" = colorblind_pal()(8)[6],
                               "TE (presence/absence)" = colorblind_pal()(8)[7],
                               "UCE" = colorblind_pal()(8)[8])) +
  scale_shape_manual(values = c(24,21)) +
  guides(fill=guide_legend(title="Marker Type", override.aes=list(shape=21)),
         shape=guide_legend(title = "Marker Derivation")) +
  scale_x_continuous(breaks=seq(2008,2020,4), labels=seq(2008,2020,4)) +
  geom_label_repel(aes(x=year, y=log(n_loci), label = citation_for_plot),
                   position = position_jitter(width = 0.1, height = 0.5, seed=8),
                   box.padding = 0.75,
                   point.padding = 0.5,
                   segment.color = 'grey50',
                   min.segment.length = unit(0, 'lines'), cex=2) +
  theme_bw()
```
Figure 2: \
![Figure 2](https://github.com/schmitt8/bird_genomics_review/blob/main/phylogenomic_stats_figure/Fig2.png)
