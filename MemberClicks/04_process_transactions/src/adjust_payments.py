import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file,index_col=0)

    return df

def adjust_for_initiation_payment(df_row):


    if df_row['Initiation Payment'] == True:

        # note these values will change in future
        # make into csv file in future membertype (think about combining into one table) to
        # be easy to modify
        initiation_payment_membertype = {
        'University Member': 2000,
        'Primarily Undergraduate Institution': 700,
        'Non-profit Affiliate': 500,
        'Non-profit  Affiliate Members':500,
        'International Affiliate': 500
    }
        # note these values will change in future
        annual_payment_membertype = {
        'University Member': 200,
        'Primarily Undergraduate Institution': 70,
        'Non-profit Affiliate': 100,
        'Non-profit  Affiliate Members':100,
        'International Affiliate': 100
    }
        # accounting for cases where initiation fee is paid over multiple invoices (happens frequently)
        print(df_row)
        multipler = df_row['Amount'] / initiation_payment_membertype[df_row['Member Type']]
        adjusted_amount  = df_row['Amount'] - multipler * (initiation_payment_membertype[df_row['Member Type']] + annual_payment_membertype[df_row['Member Type']])
    else:
        adjusted_amount = df_row['Amount']

    return adjusted_amount

def adjust_for_discount_payment(df_row):

    if df_row['Discount Payment'] == True:

        # define discount amount for five year prepay (note nonprofit and intl affiliates don't have 5-year pre-pay discount)
        discount_membertype = {
        'University Member': 100,
        'Primarily Undergraduate Institution': 35,
    }
        adjusted_amount = df_row['Amount'] + discount_membertype[df_row['Member Type']]

    else:

        adjusted_amount = df_row['Amount']

    return adjusted_amount

def save_output_file(df,out_file):
    
    df.to_csv(out_file)

def main(in_file,out_file):

    df = read_input_file(in_file)

    df['Amount'] = df.apply(adjust_for_initiation_payment,axis=1)
    df['Amount'] = df.apply(adjust_for_discount_payment,axis=1)

    save_output_file(df,out_file)

if __name__ == '__main__':

    # inputs
    in_filename = './03_munge_transactions/src/tmp/tracked_transaction_report.csv'
    out_filename = './04_munge_transactions/src/tmp/adjusted_transaction_report.csv' 

    # main function
    main(in_filename,out_filename)