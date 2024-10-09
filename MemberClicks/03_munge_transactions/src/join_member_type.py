import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file)

    return df

def join_by_organization_fields(df_institution,df_transaction):

    # do a left join by orgnaization
    df_merged_organization = pd.merge(df_transaction,df_institution,left_on='Company',right_on='Organization',how='left',validate='many_to_one')

    # do a left join by profile ID
    df_merged_id = pd.merge(df_transaction,df_institution,left_on='Profile ID',right_on='Organization ID',how='left',validate='many_to_one')

    # combine the dataframes 
    df_merged = df_merged_organization.combine_first(df_merged_id)

    return df_merged

def save_output_file(df,out_file):
    
    df.to_csv(out_file,index=False)
    
def main(in_institutions_file,in_transactions_file,out_file):
    
    df_institution = read_input_file(in_institutions_file)
    df_transaction = read_input_file(in_transactions_file)
    
    # join member type information by organization fields (name and profile ID)
    df_transaction_joined = join_by_organization_fields(df_institution,df_transaction)

    save_output_file(df_transaction_joined,out_file)

if __name__ == '__main__':

    # inputs from snakefile
    in_institutions_filename = snakemake.input['in_institutions_filename']
    in_transactions_filename = snakemake.input['in_transactions_filename']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_institutions_filename,in_transactions_filename,out_filename)