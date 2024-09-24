import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file, index_col=0)

    return df


def remove_columns(df):

    columns_to_remove = ['Transaction Type',
                         'Payment Method',
                         'Company',
                         'Cardholder Name',
                         'Transaction Status',
                         'Response Text',
                         'Reference Number',
                         'Revenue Account',
                         'Credit Account',
                         'Debit Account',
                         'First Name',
                         'Last Name']
    
    df = df.drop(columns=columns_to_remove)

    return df

def save_output_file(df,out_file):
    
    df.to_csv(out_file)
    
def main(in_file,out_file):
    
    df = read_input_file(in_file)
    
    df_cleaned = remove_columns(df)

    save_output_file(df_cleaned,out_file)

if __name__ == '__main__':

    # inputs
    in_filename = './01_fetch/src/tmp/transaction_report.csv'
    out_filename = './02_clean/src/tmp/cleaned_transaction_report.csv' 

    # main function
    main(in_filename,out_filename)   
