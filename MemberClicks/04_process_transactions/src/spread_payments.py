import pandas as pd

def read_input_file(in_file):
    
    # index are first three columns (organization, member type and initiation year)
    df = pd.read_csv(in_file,index_col=['Organization','Member Type','Initiation Year'])

    return df

def spread_payments(df):

    # note these values will change in future
    annual_payment_membertype = {
    'University Member': 200,
    'Primarily Undergraduate Institution': 70,
    'Non-profit  Affiliate Members': 100,
    'International Affiliate Members': 100
}

    # get current year from column name
    current_year = int(float(df.columns.tolist()[-1]))
    # we are considering prepayments five years into future
    max_year = current_year + 5  
    
    # create list of projected years and concatenate to dataframe (initialize to zero)
    projected_years = list(range(current_year + 1, max_year))
    df = pd.concat([df, pd.DataFrame(data=0, columns=projected_years, index=df.index)], axis=1)
    
    # create list of years analyzed
    year_columns = df.columns.values.tolist()
    
    # iterate over each row in dataframe to spread payment
    for idx, row in df.iterrows():

        # define annual payment for each row based on member type
        member_type = idx[1]
        annual_payment = annual_payment_membertype[member_type]

        # initialize remaining payment
        remaining_payment = 0
        
        # loop through each year column excluding the last projected year
        for year in year_columns[:-1]:
            payment = row[year] + remaining_payment

            # if institution has prepaid years, set cell value to one and calculate remaining payment
            if payment > annual_payment:
                df.at[idx, year] = annual_payment
                remaining_payment = payment - annual_payment
            else:
                df.at[idx, year] = payment
                remaining_payment = 0
        
        # add any remaining payment to the last year
        final_year = year_columns[-1]
        df.at[idx, final_year] += remaining_payment
    
    return df

def save_output_file(df,out_file):
    
    df.to_csv(out_file)

def main(csv_file,out_file):

    df = read_input_file(csv_file)

    df_spread = spread_payments(df)

    save_output_file(df_spread,out_file)

if __name__ == '__main__':

    # inputs from snakefile
    in_filename = snakemake.input['in_filename']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_filename,out_filename)