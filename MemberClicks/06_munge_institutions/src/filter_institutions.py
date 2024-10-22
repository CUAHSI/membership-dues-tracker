import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file,index_col=['Member Status'])

    return df

def save_output_file(df,out_name):

    df.to_csv(out_name)

def main(in_file,out_name,status):

    df = read_input_file(in_file)

    # filter institutions by member status and saved
    df_filtered = df[df.index == status]
    save_output_file(df_filtered,out_name)

if __name__ == '__main__':

    # inputs from snakefile
    in_filename = snakemake.input['in_filename']
    member_status = snakemake.params['member_status']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_filename,out_filename,member_status)