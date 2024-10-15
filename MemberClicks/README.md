# Analysis workflow for institution and representative membership tracking in MemberClicks


## Retrieval of relevant exports in MemberClicks (MC)

All inputs to this pipeline are generated through MemberClicks exports through the [CUAHSI administrator account](https://cuahsi.memberclicks.net/administrator#/login), and must be stored in [2_clean/src/in](2_clean/src/in) prior to starting the analysis workflow. Snapshots of example input queries from MC can be found in the [images/inputs](images/inputs) folder.


## Execution of analysis workflow

This data analysis workflow uses Snakemake (installation instructions [here](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html)) as a pipelining tool for this analysis workflow. 

First, create a Conda environment with all the required packages by running the following command: `conda env create -f environment.yaml`

Then we can go into the new environment with the following command: `conda activate membership-analysis-workflow`

Once in the new environment, we can execute the snakemake pipeline with this command: `snakemake --cores 1 -s Snakefile.smk`. A DAG of the workflow can be found [here](dag.png).

When the jobs are done, the following output files are useful for inspection and dissemination: 
- A CSV file of payments spread through 2028 (tabular file used to inspect the actual payment amounts) in a newly created `out` folder in [04_process_transactions](04_process_transactions)
- Two CSV files of representatives from both active and lapsed institutions in a newly created `out` folder in [07_process_transactions](07_process_transactions)



