# Analysis workflow for institution and representative membership tracking in MemberClicks


## Retrieval of relevant exports in MemberClicks (MC)

All inputs to this pipeline are generated through MemberClicks exports through the [CUAHSI administrator account](https://cuahsi.memberclicks.net/administrator#/login), and must be stored in [2_clean/src/in](2_clean/src/in) prior to starting the analysis workflow. Snapshots of example input queries from MC can be found in the [images/inputs](images/inputs) folder.


## Execution of analysis workflow

This data analysis workflow uses Snakemake (installation instructions [here](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html)) as a pipelining tool for this analysis workflow. 

First, create a Conda environment with all the required packages by running the following command: `conda env create -f environment.yaml`

Once in the new environment, we can execute the snakemake pipeline with this command: `snakemake --cores 1 -s Snakefile.smk`

When the jobs are done, an intermediate file of payments spread through 2028 (tabular file used to inspect the actual payment amounts) can be found in `out` folder in [04_process_transactions](04_process_transactions).


