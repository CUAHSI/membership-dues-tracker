import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file,index_col=['Organization','Member Type','Initiation Year'])

    return df

def get_expiration_year(df_row,annual_payment_membertype):

    # retrieve member type information (in second element)
    member_type = df_row.name[1]

    # iterate over columns (years) to see when their last full payment was 
    years = df_row.index.values.tolist()
    # initialize expiration year as first year in MC
    expiration_year = int(years[0])

    # start loop
    for year in years:
        if df_row[year] >= annual_payment_membertype[member_type]:
            expiration_year = int(year)

    return expiration_year 

def get_current_status(df_row,annual_payment_membertype,statuses,current_year=2024):
    
    # retrieve member type information (in second element)
    member_type = df_row.name[1]

    # check first if they are active this year
    if df_row[str(current_year)] >= annual_payment_membertype[member_type]:
        return statuses[0] # active
    # # then see if they were active last year (lapsed)
    # elif df_row[str(current_year-1)] == annual_payment_membertype[member_type]:
    #     return statuses[1] # lapsed
    # otherwise they are lapsed
    else:
        return statuses[1] #long_lapsed

def save_output_file(df,out_file):
    
    df.to_csv(out_file)

def main(in_file,out_file,statuses):

    # note these values will change in future
    annual_payment_membertype = {
    'University Member': 200,
    'Primarily Undergraduate Institution': 70,
    'Non-profit  Affiliate Members': 100,
    'International Affiliate Members': 100
}

    df = read_input_file(in_file)

    # add current member status in a new index column
    df['Member Status'] = df.apply(get_current_status,args=([annual_payment_membertype,statuses]), axis=1)
    # append to index here
    df.set_index('Member Status',append=True,inplace=True)

    # report expiration year in a new index column
    df['Expiration Year'] = df.apply(get_expiration_year,args=([annual_payment_membertype]), axis=1)
    # set as index here
    df.set_index('Expiration Year',append=True,inplace=True)

    save_output_file(df,out_file)


if __name__ == '__main__':

    # inputs from snakefile
    in_filename = snakemake.input['in_filename']
    member_statuses = snakemake.params['statuses']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_filename,out_filename,member_statuses)