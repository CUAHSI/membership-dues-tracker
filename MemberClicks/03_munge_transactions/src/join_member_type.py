import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file,index_col=0)

    return df


def join_by_member_type(df_institution,df_transaction):

    # perform left join
    df_merged = pd.merge(df_transaction,df_institution,on='Profile ID',how='left',validate='many_to_one')

    return df_merged

def save_output_file(df,out_file):
    
    df.to_csv(out_file)
    
def main(in_institutions_file,in_transactions_file,out_file):
    
    df_institution = read_input_file(in_institutions_file)
    df_transaction = read_input_file(in_transactions_file)
    
    df_joined = join_by_member_type(df_institution,df_transaction)

    save_output_file(df_joined,out_file)

if __name__ == '__main__':

    # inputs
    in_institutions_filename = './02_clean/src/tmp/cleaned_institutions_list.csv' 
    in_transactions_filename = './02_clean/src/tmp/cleaned_transaction_report.csv'
    out_filename = './03_munge_transactions/src/tmp/joined_transaction_report.csv' 

    # main function
    main(in_institutions_filename,in_transactions_filename,out_filename)   

