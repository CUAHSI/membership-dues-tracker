import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file,index_col=['Invoice ID','Payment Line'])

    return df

def add_offline_transactions(df):

    offline_transactions = [
        {
            'Invoice ID': '1_offline',
            'Payment Line': 1,
            'Company': 'Smith College',
            'Amount': -315,
            'Transaction Date': '10/7/2024  5:15:00 PM',
            'Description': 'Check for PUI 5-year renewal (Retroactive to 2022)',
            'Profile ID': 1000893402
            }   
    ]

    # add new rows to dataframe for offline transactions
    for transaction in offline_transactions:
        df_offline = pd.DataFrame(transaction,index=[0])
        df_offline.set_index(['Invoice ID', 'Payment Line'], inplace=True)
        df = pd.concat([df,df_offline])

    return df

def add_waived_transactions(df):

    waived_transactions = [
        {
            'Invoice ID': '1_waived',
            'Payment Line': 0,
            'Company': 'Suez Canal University',
            'Amount': -100,
            'Transaction Date': '9/1/2024  12:00:00 AM',
            'Description': 'Waived 2024 Membership Renewal, International Affiliate',
            'Profile ID': 1002566947
            },
        {
            'Invoice ID': '2_waived',
            'Payment Line': 0,
            'Company': 'University of Sidi Mohamed ben Abdellah',
            'Amount': -100,
            'Transaction Date': '9/1/2024  12:00:00 AM',
            'Description': 'Waived 2024 Membership Renewal, International Affiliate',
            'Profile ID': 1002566967
            }
    ]

    # add new rows to dataframe for waived transactions
    for transaction in waived_transactions:
        df_waived = pd.DataFrame(transaction,index=[0])
        df_waived.set_index(['Invoice ID', 'Payment Line'], inplace=True)
        df = pd.concat([df,df_waived])

    return df

def modify_transaction_date(df):

    # convert transaction date for retroactive payments
    retroactive_transactions = {
        # smith is an assumed retroactive paymet
        'Smith College':
        {
            'Invoice ID': '1_offline',
            'Payment Line': 1,
            'Retroactive Transaction Date': '1/1/2022  12:00:00 AM',
        }
        # # see link to invoice in question for Northern Arizona University in question: https://cuahsi.memberclicks.net/administrator/index.php?option=com_mcpaymentmanagement#/view-invoice/200684290
        # # I think Invoice ID 421, payment line 1 is paying for 2019 even though invoice was paid on 2/20/20 (see description field)
        # ,
        # 'Northern Arizona University':
        # {
        #     'Invoice ID': 421,
        #     'Payment Line': 1,
        #     'Retroactive Transaction Date': '1/16/2019 12:00:00 AM',
        # }      
    }

    for institution in retroactive_transactions.keys():
        invoice_id = retroactive_transactions[institution]['Invoice ID']
        payment_line = retroactive_transactions[institution]['Payment Line']
        print(invoice_id,payment_line)
        df.loc[(invoice_id,payment_line),'Transaction Date'] = retroactive_transactions[institution]['Retroactive Transaction Date']

    return df

def save_output_file(df,out_file):
    
    df.to_csv(out_file)


def main(in_file,out_file):
    
    df = read_input_file(in_file)

    df_modified = modify_transaction_date(add_waived_transactions(add_offline_transactions(df)))

    save_output_file(df_modified,out_file)

if __name__ == '__main__':

    # inputs from snakefile
    in_filename = snakemake.input['in_filename']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_filename,out_filename)