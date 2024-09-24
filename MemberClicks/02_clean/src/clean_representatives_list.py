import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file, index_col=0)

    return df

def modify_column_names(df):

    old_columns = ['[Name | Last]','[Name | First]','[Organization]','[Email | Primary]','[Member Type]','[Last Modified Date]']
    new_columns = ['First Name','Last Name','Organization','Email','Member Type','Last Modified Date']

    for i in range(len(df.columns)):
        df.rename(columns={f'{old_columns[i]}':f'{new_columns[i]}'},inplace=True)

    return df

def save_output_file(df,out_file):

    df.to_csv(out_file)
    
def main(in_file,out_file):
    
    df = read_input_file(in_file)
    
    df_cleaned = modify_column_names(df)

    save_output_file(df_cleaned,out_file)

if __name__ == '__main__':

    # inputs
    in_filename = './01_fetch/src/tmp/representatives_list.csv'
    out_filename = './02_clean/src/tmp/cleaned_representatives_list.csv' 

    # main function
    main(in_filename,out_filename)   