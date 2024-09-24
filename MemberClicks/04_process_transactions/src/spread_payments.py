import pandas as pd

def spread_payments_across_years(df):

    # we want to track payments from 2016 to 2028
    years = list(range(2016, 2029))

    # define years we are projecting
    projected_years = list(range(df.columns[-1],years[-1]))

    # concatenate new dataframe with projected years included
    df = pd.concat(df,pd.DataFrame(data=0,columns=projected_years),axis=1)

    # iterate over the dataframe rows
    for idx, row in df.iterrows():
        # iterate through list of years (columns)
        for year in years:
            # see if the value is greater than one (excess payment)
            value = row[year]
            if value > 1:
                # if so, set value of current year to 1 and calculate excess payment
                df.at[idx, year] = 1  
                excess = value - 1

                if year != years[-1]:
                    # add excess to next year
                    df.at[idx, year+1] += excess
                    # break if excess has been fully spread
                    if df.at[idx, year+1] <= 1:
                        break
                else:
                    # add excess to final year
                    df.at[idx, year] += excess

    return df






    



                        