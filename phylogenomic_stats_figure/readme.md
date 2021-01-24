# What have we learned from the first 500 avian genomes? <br /> Annu. Rev. Ecol. Syst. Evol

G. A. Bravo, C. J. Schmitt, S. V. Edwards 
01/17/2021

## This script recreates figure 2 - Increase in the number of loci analyzed in phylogenetic studies of birds through time, based on a query conducted via the Web of Science portal on 31 December 2020 with the following search terms: “bird*” and “genom*” and “phylogen*”. A small number of papers not detected by the query were included manually. Each point represents a dataset from a published paper (multiple points per paper in some cases) and are color-coded according to marker type. The shape of each point indicates whether loci were derived a priori or a posterior. Finally, a small amount of ‘jitter’ was added to minimize overlapping points and improve visualization.

The data: phylogenomic_stats.csv

The R code:

``` {R}
## load packages
library(tidyverse)
library(ggthemes)
library(ggrepel)
library(cowplot)

## load dataset
phylogenomic_stats <- read.csv("/Users/schmitty/Documents/CJS/projects/bird_genome_review/phylogenomic_stats.csv")

## convert # of loci and # of spp to numeric
phylogenomic_stats$n_loci <- as.numeric(phylogenomic_stats$n_loci)
phylogenomic_stats$n_spp <- as.numeric(phylogenomic_stats$n_spp)

## plot log # of loci by year and color points by marker type
fig2a <- ggplot(data=phylogenomic_stats) +
  geom_smooth(aes(x=year,
                  y=log(n_loci)),
              method = 'glm',
              color = "black") +
  geom_point(aes(x=year, y=log(n_loci), fill=loci_type, shape = priori_posteriori),
             position = position_jitter(width = 0.1,
                                        height = 0.5,
                                        seed=8),
             size=2,
             alpha = .75) +
  labs(x="Year",
       y="ln ( number of loci )") +
  scale_fill_manual(values = c("3' UTR" = colorblind_pal()(8)[1],
                               "CNEE" = colorblind_pal()(8)[2],
                               "exon" = colorblind_pal()(8)[3],
                               "indel" = colorblind_pal()(8)[4],
                               "intron" = colorblind_pal()(8)[5],
                               "RADseq" = colorblind_pal()(8)[6],
                               "TE (presence/absence)" = colorblind_pal()(8)[7],
                               "UCE" = colorblind_pal()(8)[8])) +
  scale_shape_manual(values = c(24,21)) +
  guides(fill=guide_legend(title="Marker Type",
                           title.position="top",
                           title.hjust = 0.5,
                           nrow = 1,
                           override.aes=list(shape=21)),
         shape=guide_legend(title = "Marker Derivation",
                            title.position="top",
                            nrow = 1,
                            title.hjust = 0.5)) +
  scale_x_continuous(breaks=seq(2008,2020,4),
                     labels=seq(2008,2020,4)) +
  geom_label_repel(aes(x=year,
                       y=log(n_loci),
                       label = citation_for_plot),
                   position = position_jitter(width = 0.1,
                                              height = 0.5,
                                              seed=8),
                   box.padding = .75,
                   point.padding = 0.5,
                   segment.color = 'grey50',
                   min.segment.length = unit(0, 'lines'),
                   cex=2) +
  theme_bw() +
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank())

## plot log # of loci by log # of spp and color points by marker type
fig2b <- ggplot(data=phylogenomic_stats) + 
  geom_smooth(aes(x = log(n_spp),
                  y = log(n_loci)),
              method = 'glm',
              color = "black") +
  geom_point(aes(x = log(n_spp),
                 y = log(n_loci),
                 fill = loci_type,
                 shape = priori_posteriori),
             position = position_jitter(width = 0.2,
                                        height = 0.5,
                                        seed=8)) +
  labs(x="ln ( number of species)",
       y="ln ( number of loci )") +
  scale_fill_manual(values = c("3' UTR" = colorblind_pal()(8)[1],
                               "CNEE" = colorblind_pal()(8)[2],
                               "exon" = colorblind_pal()(8)[3],
                               "indel" = colorblind_pal()(8)[4],
                               "intron" = colorblind_pal()(8)[5],
                               "RADseq" = colorblind_pal()(8)[6],
                               "TE (presence/absence)" = colorblind_pal()(8)[7],
                               "UCE" = colorblind_pal()(8)[8])) +
  scale_shape_manual(values = c(24,21)) +
  guides(fill=guide_legend(title="Marker Type",
                           override.aes=list(shape=21),
                           title.position="top",
                           nrow = 1,
                           title.hjust = 0.5),
         shape=guide_legend(title = "Marker Derivation",
                            title.position="top",
                            nrow = 1,
                            title.hjust = 0.5)) +
  geom_label_repel(aes(x=log(n_spp),
                       y=log(n_loci),
                       label = citation_for_plot),
                   position = position_jitter(width = 0.2,
                                              height = 0.5,
                                              seed=8),
                   box.padding = .75,
                   point.padding = 0.5,
                   segment.color = 'grey50',
                   min.segment.length = unit(0, 'lines'),
                   cex=2) +
  theme_bw() +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())

# arrange the three plots in a single row
fig2 <- plot_grid( fig2a + theme(legend.position="none"),
                   fig2b + theme(legend.position="none"),
                   align = "vh",
                   labels = c("A", "B"),
                   hjust = -1,
                   nrow = 1)

# extract the legend from one of the plots
# (clearly the whole thing only makes sense if all plots
# have the same legend, so we can arbitrarily pick one.)
legend_a <- get_legend(fig2a + theme(legend.position = "bottom"))

# add the legend underneath the row we made earlier
# of one plot (via rel_heights).
fig2 <- plot_grid(fig2, legend_a, ncol = 1, rel_heights = c(.5, .075))
fig2
```
Figure 2: \
![Figure 2](https://github.com/edwards-bird-lab/bird_genomics_review/blob/main/phylogenomic_stats_figure/Fig2.png)
