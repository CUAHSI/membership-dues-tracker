import pandas as pd

def insert_initiation_year(row):

    initiation_payment_flags = ['initiation',
                                'fee']
    
    initiation_payment_pattern = '|'.join(initiation_payment_flags)  

    if row['Description'].str.contains(rf'{initiation_payment_pattern}', case=False, na=False):

        return row['Transaction Year']
    
    else:

        return False

def pivot_transaction_table(df):

    df_pivot = pd.pivot_table(df, 
                              values='Normalized Amount', 
                              index=['Organization', 'Member Type','Initiation Year'], 
                              columns='Transaction Year', 
                              fill_value=0)  # Replace NaNs with 0   
    
    return df_pivot