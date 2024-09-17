import pandas as pd


def read_transaction_report(csv_file):
    
    df = pd.read_csv(csv_file)

    return df

def convert_to_datetime(df,transaction_date_colname='Transaction Date'):

    df['transaction_date_colname'] = pd.to_datetime(df[transaction_date_colname])

    # df['transaction_year_colname'] = df[transaction_date_colname].dt.year

    return df 

def make_transaction_amount_positive(df, amount_colname = 'Amount'):

    df[amount_colname] = df[amount_colname].abs()

    return df


