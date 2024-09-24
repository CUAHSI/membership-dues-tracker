import pandas as pd

def read_input_file(in_file):
    
    df = pd.read_csv(in_file)

    return df

def save_output_file(df,out_file):
    
    df.to_csv(out_file)
    
def main(in_file,out_file):
    
    df = read_input_file(in_file)
    
    save_output_file(df,out_file)

if __name__ == '__main__':
    
    # inputs
    in_filename = './01_fetch/src/in/transaction-report-09-23-2024.csv'
    out_filename = './01_fetch/src/tmp/transaction_report.csv'

    # main function 
    main(in_filename,out_filename)
    
