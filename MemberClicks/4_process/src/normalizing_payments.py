import pandas as pd

def read_aggregated_transactions(csv_file):

    df = pd.read_csv(csv_file)

    return df 

def normalize_aggregated_transactions(df_row,amount_colname='Amount',membertype_colname='Member Type'):

    # note these values will change in future
    annual_dues_membertype_dict = {
    'University Member': 200,
    'Primarily Undergraduate Institution': 70,
    'Non-profit Affiliate': 100,
    'International Affiliate': 100
}

    annual_payment = annual_dues_membertype_dict[df_row[membertype_colname]]

    normalized_payment = df_row[amount_colname] / annual_payment

    return normalized_payment

def save_normalized_aggregated_transactions(df,out_file,out_path='4_process/tmp/'):

    file_name = out_path + out_file

    df.to_csv(file_name)

def main(csv_file,out_file,norm_amount_colname='Normalized Amount'):

    df = read_aggregated_transactions(csv_file)

    df[norm_amount_colname] = df.apply(normalize_aggregated_transactions,axis=1)

    df_summed = save_normalized_aggregated_transactions(df,norm_amount_colname)

    save_normalized_aggregated_transactions(df,out_file)








