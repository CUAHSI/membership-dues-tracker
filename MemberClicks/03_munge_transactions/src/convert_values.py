import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file,index_col=['Invoice ID','Payment Line'])

    return df

def convert_date_to_datetime(df):

    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

    # add new column for transaction year
    df['Transaction Year'] =df['Transaction Date'].dt.year

    return df 

def covert_amount_to_positive(df):

    df['Amount'] = df['Amount'].abs()

    return df

def save_output_file(df,out_file):
    
    df.to_csv(out_file)

def main(in_file,out_file):
    
    df = read_input_file(in_file)

    # df_converted = convert_transaction_date(df)
    
    df_converted = convert_date_to_datetime(df)

    df_converted = covert_amount_to_positive(df_converted)

    save_output_file(df_converted,out_file)

if __name__ == '__main__':

    # inputs from snakefile
    in_filename = snakemake.input['in_filename']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_filename,out_filename)