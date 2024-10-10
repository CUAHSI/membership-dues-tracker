
library(targets)

tar_option_set(
  packages = c(
    'tidyverse'
  ), 
  format = 'qs' # This format is more compressed than the default `rds`
)

# Source each phase script containing the target recipes
source('01_fetch.R')
source('02_clean.R')
source('03_munge.R')
source('04_summarize.R')
source('05_visualize.R')

# Combine all phase target lists
c(p1, p2, p3, p4, p5)
