import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file,index_col=0)

    return df

def flag_initiation_payments(df):

    # list of flag in description and amount fields for initiation payments
    initiation_flags_description = ['initiation']
    initiation_flags_amount = [3000]

    # flag initiation payment from description
    initiation_pattern = '|'.join(initiation_flags_description)
    initiation_check = df['Description'].str.contains(rf'{initiation_pattern}', case=False, na=False)

    # flag initiation payment from amount
    for i in range(len(initiation_flags_amount)):
        # Make the initation payment value True for the rows that are flagged
        initiation_check |= df['Amount'].isin(initiation_flags_amount)

    return initiation_check

def save_output_file(df,out_file):
    
    df.to_csv(out_file)

def main(in_file,out_file):

    df = read_input_file(in_file)
    
    df['Initiation Payment'] =flag_initiation_payments(df)

    save_output_file(df,out_file)

if __name__ == '__main__':

    # inputs from snakefile
    in_filename = snakemake.input['in_filename']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_filename,out_filename)