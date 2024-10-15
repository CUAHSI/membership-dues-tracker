import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file)

    return df

def modify_column_names(df):

    old_columns = ['[Name | Last]','[Name | First]','[Organization]','[Email | Primary]','[Member Type]','[Last Modified Date]']
    new_columns = ['Last Name','First Name','Organization','Email','Member Type','Last Modified Date']

    for i in range(len(old_columns)):
        df.rename(columns={f'{old_columns[i]}':f'{new_columns[i]}'},inplace=True)

    return df

def modify_institution_names(df):

    # remove special unicode characters
    df['Organization'] = df['Organization'].str.encode('utf-8').str.decode('ascii', 'ignore')

    # create dictionary of instituion values to be updated
    # note we are treating UNC system as one institution (as opposed to segmenting by campus (e.g. Chapel Hill))
    replace_vals = {
        'University of North Carolina': 'University of North Carolina System'
        }
    
    # update institution names
    df['Organization'] = df['Organization'].replace(replace_vals)

    return df

def save_output_file(df,out_file):

    df.to_csv(out_file,index=False)
    
def main(in_file,out_file):
    
    df = read_input_file(in_file)
    
    df = modify_column_names(df)

    df_cleaned = modify_institution_names(df)

    save_output_file(df_cleaned,out_file)

if __name__ == '__main__':

    # inputs from snakefile
    in_filename = snakemake.input['in_filename']
    out_filename = snakemake.output['out_filename']

    # main function
    main(in_filename,out_filename)    