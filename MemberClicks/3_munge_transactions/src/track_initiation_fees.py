import pandas as pd

def read_transaction_report(csv_file):
    
    df = pd.read_csv(csv_file)

    return df

def check_for_initiation_fees(df,initiation_fee_colname = 'Initiation Fee'):

    df[initiation_fee_colname] = df['Description'].str.contains(r'fee|initiation', case=False, na=False)

    return df

def save_transaction_report(df,out_file,path='3_munge_transactions/tmp/'):

    file_name = path + out_file

    df.to_csv(file_name)

def main(csv_file,out_file):

    df = check_for_initiation_fees(df)

    save_transaction_report(df,out_file)



