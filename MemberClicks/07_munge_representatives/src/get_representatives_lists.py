import re
import os
import glob
import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file)

    return df

def get_institution_files(in_institutions_path,date):

    institution_files = glob.glob(in_institutions_path+f'*{date}*')

    return institution_files

def join_representatives(df_representatives,df_institutions):

    # drop all the columns outside of initiation and expiration year
    preserved_columns = ['Organization','Member Type','Initiation Year','Expiration Year']
    df_institutions = df_institutions[preserved_columns]

    # do a join on organization name and return representatives information
    df_merged_representatives = pd.merge(df_representatives,df_institutions,left_on='Organization',right_on='Organization',how='right',validate='many_to_one')

    return df_merged_representatives

def save_output_file(df,out_file):
    
    df.to_csv(out_file,index=False)

def main(in_institutions_file,in_representatives_file,out_representatives_file):

    # read in files
    df_institutions = read_input_file(in_institutions_file)
    df_representatives = read_input_file(in_representatives_file)

    # do join to merge representatives
    df_merged_representatives = join_representatives(df_representatives,df_institutions)

    # save data to file
    save_output_file(df_merged_representatives,out_representatives_file)

if __name__ == '__main__':

    # inputs from snakefile
    in_institutions_filename =  snakemake.input['in_institutions_filename']
    in_representatives_filename = snakemake.input['in_representatives_filename']
    out_representatives_filename = snakemake.output['out_representatives_filename']

    # main function
    main(in_institutions_filename,in_representatives_filename,out_representatives_filename)