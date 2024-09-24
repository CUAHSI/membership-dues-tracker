def classify_annual_payment(df):

    # set values in dataframe based on the amount paid relative to annual dues

    # did not make annual payment
    df = df.applymap(lambda x: '' if x < 1 else x)
    # made annual payment
    df = df.applymap(lambda x: 'paid' if x == 1 else x)
    # overpaid annual payment (only in 2028)
    df = df.applymap(lambda x: 'overpaid' if x > 1 else x)

    return df