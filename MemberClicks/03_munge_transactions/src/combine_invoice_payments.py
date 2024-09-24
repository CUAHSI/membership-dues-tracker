import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file,index_col=0)

    return df

def combine_by_invoice_id(df):

    # define dictionary with instructions on how to aggregate columns
    combine_by_dict = {
                        'Transaction Date': 'first',
                        'Description': lambda x: ' | '.join(x), # use | as delimiter for different lines of payment within an invoice
                        'Amount': sum,
                        'Organization': 'first',
                        'Member Type':'first'
                            }
    

    # group by invoice ID with instructions in dictionary (set invoice ID as index)
    combined_df = df.groupby('Invoice ID').agg(combine_by_dict)
    # combined_df.set_index('Invoice ID',inplace=True)

    return combined_df

def save_output_file(df,out_file):
    
    df.to_csv(out_file)


def main(in_file,out_file):
    
    df = read_input_file(in_file)
    
    df_combined = combine_by_invoice_id(df)

    save_output_file(df_combined,out_file)


if __name__ == '__main__':

    # inputs
    in_filename = './03_munge_transactions/src/tmp/converted_transaction_report.csv'
    out_filename = './03_munge_transactions/src/tmp/combined_transaction_report.csv' 

    # main function
    main(in_filename,out_filename)   

    
