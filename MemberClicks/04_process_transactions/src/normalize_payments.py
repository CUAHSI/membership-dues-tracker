import pandas as pd

def read_aggregated_transactions(csv_file):

    df = pd.read_csv(csv_file)

    return df 


def normalize_by_annual_payment(df_row):

    # note these values will change in future
    annual_payment_membertype = {
    'University Member': 200,
    'Primarily Undergraduate Institution': 70,
    'Non-profit Affiliate': 100,
    'International Affiliate': 100
}
    normalized_payment = df_row['Amount'] / annual_payment_membertype[df_row['Member Type']]

    return normalized_payment

# def save_normalized_aggregated_transactions(df,out_file,out_path='4_process/tmp/'):

#     file_name = out_path + out_file

#     df.to_csv(file_name)

def main(csv_file,out_file,norm_amount_colname='Normalized Amount'):

    df = read_aggregated_transactions(csv_file)

    # # adjust for initiation payments
    # df['Amount'] = df.apply(adjust_for_initiation_payment,axis=1)
    # # adjust for discount payments
    # df['Amount'] = df.apply(adjust_for_discount_payment,axis=1)

    # create normalized payment (by annual payment)
    df['Normalized Amount'] = df.apply(normalize_by_annual_payment,axis=1)




    # df[norm_amount_colname] = df.apply(normalize_aggregated_transactions,axis=1)

    # df_summed = save_normalized_aggregated_transactions(df,norm_amount_colname)

    # save_normalized_aggregated_transactions(df,out_file)








