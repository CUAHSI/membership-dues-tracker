import pandas as pd

def read_transaction_report(csv_file):
    """
    Read csv containing transaction report from MC.

    Parameters
    ----------
    csv_file : string
        Path to csv file containing transaction report from MC export.

    Returns
    -------
    df : Pandas dataframe
        Dataframe containing transaction report.

    """
    
    df = pd.read_csv(csv_file)

    return df

def save_transaction_report(df,out_file,path='./1_fetch/tmp/'):
    """
    Save transaction report dataframe to a csv file.

    Parameters
    ----------
    df : Pandas dataframe
        Dataframe containing transaction report.

    Returns
    -------
    None.

    """

    file = path + out_file
    
    df.to_csv(file)
    
def main(csv_file,out_file):
    
    df = read_transaction_report(csv_file)
    
    save_transaction_report(df,out_file)

if __name__ == '__main__':
    
    # use snakemake here
    out_filename = 'transaction_report.csv'
    csv_file_path = str(snakemake)
    
    main(csv_file_path,out_filename)
    
    
