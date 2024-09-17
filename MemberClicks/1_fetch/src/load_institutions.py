import pandas as pd

def read_institutions_list(csv_file):
    """
    Read csv containing profiles of all institutions in MC.

    Parameters
    ----------
    csv_file : string
        Path to csv file containing profiles of institutions from MC export.

    Returns
    -------
    df : Pandas dataframe
        Dataframe containing profiles of all institutions in MC.

    """
    
    df = pd.read_csv(csv_file)

    return df

def save_institutions_list(df,file_name):
    """
    Save institutions list dataframe to a csv file.

    Parameters
    ----------
    df : Pandas dataframe
        Dataframe containing institutions lists.

    Returns
    -------
    None.

    """

    out_file = './1_fetch/tmp/' + file_name
    
    df.to_csv(out_file)
    
def main(csv_file):
    
    df = read_institutions_list(csv_file)
    
    save_institutions_list(df)

if __name__ == '__main__':
    
    # use snakemake here
    out_filename = 'institutions_list.csv'
    csv_file_path = str(snakemake)