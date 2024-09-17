import pandas as pd

def read_munged_transaction_report(csv_file):


    df = pd.read_csv(csv_file)

    return df 



def normalize_payments_by_membertype(df_row,amount_colname='Amount',membertype_colname='Member Type'):

    # note these values will change in future
    annual_membertype_payment_dict = {
    'University Member': 200,
    'Primarily Undergraduate Institution': 70,
    'Non-profit Affiliate': 100,
    'International Affiliate': 100
}

    annual_payment = annual_membertype_payment_dict[df_row[membertype_colname]]

    normalized_payment = df_row[amount_colname] / annual_payment

    return normalized_payment

def sum_payments_by_year(df,norm_amount_colname,org_colname='Company',membertype_colname='Member Type',date_colname='Transaction Date'):
    
    year_colname = 'Transaction Year'

    df[year_colname] = df[date_colname].dt.year

    df.pivot_table(value=norm_amount_colname,
                   index=[org_colname,membertype_colname],
                   columns=year_colname,
                   aggfunc='sum',
                   fill_value=0)
    
    return df



def save_transaction_data(df,out_file,out_path='4_process/tmp/'):

    file_name = out_path + out_file

    df.to_csv(file_name)

def main(df,out_file,norm_amount_colname='Normalized Amount'):

    df[norm_amount_colname] = df.apply(normalize_payments_by_membertype,axis=1)

    df_summed = sum_payments_by_year(df,norm_amount_colname)

    save_transaction_data(df,out_file)








