import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file,index_col=0)

    return df

def track_initiation_payments(df):


    initiation_payment_flags = ['initiation',
                                'fee']
    
    initiation_payment_pattern = '|'.join(initiation_payment_flags)

    initiation_payment_check = df['Description'].str.contains(rf'{initiation_payment_pattern}', case=False, na=False)

    return initiation_payment_check

def track_discount_payments(df):

    discounted_payment_flags = ['5 year',
                                '5-year',
                                'five year',
                                'discount']
    
    discount_payment_pattern = '|'.join(discounted_payment_flags)

    # check both description and amount columns
    discount_payment_description_check = df['Description'].str.contains(rf'{discount_payment_pattern}', case=False, na=False)
    discount_payment_amount_check = df['Amount'].isin([900, 315]) # GI and PUI
    # return True if one of the checks was flagged, False otherwise
    discount_payment_check = discount_payment_description_check | discount_payment_amount_check

    return discount_payment_check

def save_output_file(df,out_file):
    
    df.to_csv(out_file)

def main(in_file,out_file):

    df = read_input_file(in_file)

    df['Initiation Payment'] = track_initiation_payments(df)
    df['Discount Payment'] = track_discount_payments(df)

    save_output_file(df,out_file)

if __name__ == '__main__':

    # inputs
    in_filename = './03_munge_transactions/src/tmp/combined_transaction_report.csv'
    out_filename = './03_munge_transactions/src/tmp/tracked_transaction_report.csv' 

    # main function
    main(in_filename,out_filename)   


