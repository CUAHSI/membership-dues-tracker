import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file)

    return df


def insert_initiation_year(df_row, df, memory):

    # record initiation year where column value is flagged
    if df_row['Initiation Payment'] == True:
        memory[df_row['Organization']] = df_row['Transaction Year']
        return df_row['Transaction Year']
    
    # see if there is already an initiation year in memory
    elif df_row['Organization'] in memory:
        return memory[df_row['Organization']]
    
    # check future rows for the same organization to find an initiation payment
    future_rows = df[(df['Organization'] == df_row['Organization']) & (df['Transaction Year'] > df_row['Transaction Year'])]
    for _, future_row in future_rows.iterrows():
        if future_row['Initiation Payment'] == True:
            memory[df_row['Organization']] = future_row['Transaction Year']
            return future_row['Transaction Year']
    
    # If no initiation payment is found, return empty string
    return ' '

def propagate_initiation_year(df):
    # initialize a memory dictionary to store the initiation year for each organization
    memory = {}

    # apply the function row by row
    # dataframe and memory passed for look-ahead
    df['Initiation Year'] = df.apply(lambda row: insert_initiation_year(row, df, memory), axis=1)

    return df

def pivot_transaction_table(df):

    df_pivot = pd.pivot_table(df, 
                              values='Amount', 
                              index=['Organization', 'Member Type','Initiation Year'], 
                              columns='Transaction Year', 
                              fill_value=0)  # Replace NaNs with 0   
    
    return df_pivot

def save_output_file(df,out_file):
    
    df.to_csv(out_file)

def main(csv_file,out_file):

    df = read_input_file(csv_file)

    df = propagate_initiation_year(df) 

    df_pivot = pivot_transaction_table(df)

    save_output_file(df_pivot,out_file)

if __name__ == '__main__':

    # inputs from snakefile
    in_filename = snakemake.input['in_filename']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_filename,out_filename)