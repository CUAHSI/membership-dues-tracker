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
        'Non-profit  Affiliate Members': 500,
        'International Affiliate Members': 500
    }
        # note these values will change in future
        annual_payment_membertype = {
        'University Member': 200,
        'Primarily Undergraduate Institution': 70,
        'Non-profit  Affiliate Members': 100,
        'International Affiliate Members': 100
    }

        adjusted_amount = df_row['Amount'] - initiation_payment_membertype[df_row['Member Type']] + annual_payment_membertype[df_row['Member Type']]
    else:
        adjusted_amount = df_row['Amount']

    return adjusted_amount

def adjust_for_discount_payment(df_row):

    # note these values will change in future
    annual_payment_membertype = {
    'University Member': 200,
    'Primarily Undergraduate Institution': 70,
    'Non-profit  Affiliate Members': 100,
    'International Affiliate Members': 100
}
    # assume that nonprofts and int'l affiliates are given five year discount
    # though I haven't seen offical documentation here
    discounted_payment_membertype = {
    'University Member': 900,
    'Primarily Undergraduate Institution': 315,
    'International Affiliate Members': 450,
    'Non-profit  Affiliate Members': 450
}
    
    actual_payment_membertype = {
    'University Member': 1000,
    'Primarily Undergraduate Institution': 350,
    'International Affiliate Members': 500,
    'Non-profit  Affiliate Members': 500
}
    
    member_type = df_row['Member Type']

    # where transaction is discounted payment (includes one year of membership)
    if df_row['Amount'] == discounted_payment_membertype[df_row['Member Type']]:   
        adjusted_amount = actual_payment_membertype[df_row['Member Type']]
    # some institutions pay initiation fee and five year renewal in same year
    # these cases will be handled as six years total
    elif df_row['Amount'] == discounted_payment_membertype[df_row['Member Type']] + annual_payment_membertype[df_row['Member Type']]:
        adjusted_amount = 6*annual_payment_membertype[df_row['Member Type']]
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

    # inputs from snakefile
    in_filename = snakemake.input['in_filename']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_filename,out_filename)