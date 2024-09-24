import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file,index_col=0)

    return df

def read_transaction_report(csv_file):
    
    df = pd.read_csv(csv_file)

    return df

def convert_date_to_datetime(df):

    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

    return df 

def covert_amount_to_positive(df):

    df['Amount'] = df['Amount'].abs()

    return df

def save_output_file(df,out_file):
    
    df.to_csv(out_file)

def main(in_file,out_file):
    
    df = read_input_file(in_file)
    
    df_converted = convert_date_to_datetime(df)

    df_converted = covert_amount_to_positive(df_converted)

    save_output_file(df_converted,out_file)


if __name__ == '__main__':

    # inputs
    in_filename = './03_munge_transactions/src/tmp/joined_transaction_report.csv'
    out_filename = './03_munge_transactions/src/tmp/converted_transaction_report.csv' 

    # main function
    main(in_filename,out_filename)   
