import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file)

    return df

def remove_columns(df):

    columns_to_remove = ['Transaction Type',
                         'Payment Method',
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

def add_payment_line(df):

    # group by invoice ID and assign a sequential number to each payment line
    df['Payment Line'] = df.groupby('Invoice ID').cumcount() + 1
    
    return df

def modify_institution_names(df):

    # remove special unicode characters
    df['Company'] = df['Company'].str.encode('utf-8').str.decode('ascii', 'ignore')

    # create dictionary of instituion values to be updated
    # note we are treating UNC system as one institution (as opposed to segmenting by campus (e.g. Chapel Hill))
    replace_vals = {
        'University of North Carolina': 'University of North Carolina System'
        }
    
    # update institution names
    df['Company'] = df['Company'].replace(replace_vals)

    return df

def save_output_file(df,out_file):
    
    df.to_csv(out_file,index=False)
    
def main(in_file,out_file):
    
    df = read_input_file(in_file)

    df_cleaned = modify_institution_names(df)

    df_cleaned = add_payment_line(df_cleaned)  
    
    df_cleaned = remove_columns(df_cleaned)

    save_output_file(df_cleaned,out_file)

if __name__ == '__main__':

    # inputs from snakefile
    in_filename = snakemake.input['in_filename']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_filename,out_filename)