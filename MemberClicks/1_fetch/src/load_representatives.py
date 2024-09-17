import pandas as pd

def read_representatives_list(csv_file):
    """
    Read csv containing profiles of non-inactive representatives from MC.

    Parameters
    ----------
    csv_file : string
        Path to csv file containing profiles of non-inactive representatives from MC export.

    Returns
    -------
    df : Pandas dataframe
        Dataframe containing profiles of non-inactive representatives.

    """
    
    df = pd.read_csv(csv_file)

    return df

def save_representatives_list(df,out_file,path='./1_fetch/tmp/'):
    """
    Save representatives list dataframe to a csv file.

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

    df = read_representatives_list(csv_file)
    
    save_representatives_list(df,out_file)

if __name__ == '__main__':
    
    # use snakemake here
    out_filename = 'representatives_list.csv'
    csv_file_path = str(snakemake)
    
    main(csv_file_path,out_filename)