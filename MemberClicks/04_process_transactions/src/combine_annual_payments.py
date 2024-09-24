import pandas as pd

def read_munged_transaction_report(csv_file):

    df = pd.read_csv(csv_file)

    return df 

# def adjust_for_initiation_fees(row, amount_colname='Amount', initiation_year_colname='Initiation Year',initiation_fee_colname='Initiation Fee',membertype_colname='Member Type',year_colname='Transaction Year'):
#     """
#     Adjust the payment amount by subtracting the initiation fee if applicable.
#     """

#     # note these values will change in future
#     annual_dues_membertype_dict = {
#     'University Member': 200,
#     'Primarily Undergraduate Institution': 70,
#     'Non-profit Affiliate': 100,
#     'International Affiliate': 100
# }

#     # check if row corresponds to initiation fee transaction
#     if row[initiation_fee_colname]:

#         # replace initiation fee with yearly payment (note initiation fee includes one year of payment)
#         initiation_fee_amount = annual_dues_membertype_dict[row[membertype_colname]]

#         # return the actual amount paid for initiation fees, the initation year, and the intended initiation amount as defined in bylaws
#         return row[amount_colname], row[year_colname], initiation_fee_amount 
    
#     # if transaction does not correspond to initiation payment, return actual amount paid, and False for both the initiation year and intended intiation amount 
#     return row[amount_colname],False,False

def group_payments_by_year(df):

    # make new column for transaction year 
    df['Transaction Year'] = df['Transaction Date'].dt.year

    # define dictionary for how to aggregate columns
    groupby_instructions = {
        'Organization': 'first',
        'Member Type': 'first',
        'Description': lambda x: '//'.join(x), # use // as delimiter for different invoices within a year
        'Amount': sum
        }

    # # generate new keys/values for the actual amount paid for initiation fee in a given year, along with the initiation year. TThe amount column is replaced with the prescribed initiation fee (if applicable)
    # df[initiation_fee_colname],df[initiation_year_colname],df[amount_colname] = df.apply(adjust_for_initiation_fees,axis=1)

    grouped_df = df.groupby('Transaction Year').agg(groupby_instructions)
    # grouped_df.set_index('Transaction Year',inplace=True)

    # # sum payments over a given year, perserve index columns for organization name, member type, initiation/join year, and amount paid for iniation.
    # df.pivot_table(value='Normalized Amount',
    #                index=['Organization','Member Type'],
    #                columns='Transaction Year',
    #                aggfunc='sum',
    #                fill_value=0)
    
    return grouped_df



def save_aggregated_transactions(df,out_file,file_path='4_process/tmp/'):

    file_name = file_path + out_file

    df.to_csv(file_name)

def main(csv_file,out_file):

    df = read_munged_transaction_report(csv_file)

    df_summed = aggregate_payments_year(df)

    save_aggregated_transactions(df,out_file)
