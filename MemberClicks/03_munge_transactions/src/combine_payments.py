import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file)

    return df



def combine_payments_by_year(df):

    # define dictionary with instructions on how to aggregate columns
    combine_by_dict = {
                        'Description': lambda x: ' | '.join(x), # use | as delimiter for different lines of payment (within or between invoices)
                        'Amount': sum,
                        'Member Type':'first',
                            }
    

    # group by invoice ID with instructions in dictionary (set invoice ID as index)
    combined_df = df.groupby(['Organization','Transaction Year']).agg(combine_by_dict)
    # combined_df.set_index('Invoice ID',inplace=True)

    return combined_df

def save_output_file(df,out_file):
    
    df.to_csv(out_file)


def main(in_file,out_file):
    
    df = read_input_file(in_file)

    df_combined = combine_payments_by_year(df)

    save_output_file(df_combined,out_file)


if __name__ == '__main__':

    # inputs from snakefile
    in_filename = snakemake.input['in_filename']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_filename,out_filename)