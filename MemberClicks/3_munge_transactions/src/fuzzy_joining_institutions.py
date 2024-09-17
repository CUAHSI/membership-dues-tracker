from fuzzywuzzy import process
import pandas as pd

def fuzzy_right_join_member_type(df_transaction, df_institution, transaction_on, institution_on, institution_member_type, threshold=80):
    """
    Perform a fuzzy right join between transaction data and institution data on specific columns.
    This will add the institution's member type to the transaction dataframe based on the best fuzzy match
    and only include matches that exceed a similarity threshold.

    Parameters:
    - df_transaction: The dataframe containing transaction data.
    - df_institution: The dataframe containing institution data.
    - transaction_on: Column name in df_transaction to fuzzy match on (e.g., institution name).
    - institution_on: Column name in df_institution to fuzzy match on (e.g., institution name).
    - institution_member_type: The column in df_institution to add to df_transaction (e.g., member type).
    - threshold: The minimum similarity score required to consider a match (default is 80).

    Returns:
    - A dataframe with the institution's member type and fuzzy match score added to df_transaction.
    """
    
    # Create lists to store the matched member type and match score
    matched_member_type = []
    # matched_scores = []
    
    # Iterate over each value in the transaction dataframe's matching column
    for transaction_value in df_transaction[transaction_on]:
        # Find the best match and score in the institution dataframe's matching column
        match, score = process.extractOne(transaction_value, df_institution[institution_on])
        
        # Check if the match meets the threshold
        if score >= threshold:
            # Step 1: Filter rows where institution_on equals the fuzzy match
            filtered_rows = df_institution[df_institution[institution_on] == match]

            # Step 2: Select the 'institution_member_type' column from the filtered rows
            selected_column = filtered_rows[institution_member_type]

            # Step 3: Convert the selected column to a NumPy array and extract the first value
            member_type_value = selected_column.values[0]
        else:
            # If the score is below the threshold, return None for the member type
            member_type_value = None
        
        # Step 4: Append the extracted member type and the score to the respective lists
        matched_member_type.append(member_type_value)
        # matched_scores.append(score)
    
    # Add the matched member type and scores as new columns in the transaction dataframe
    df_transaction[institution_member_type] = matched_member_type
    # df_transaction['fuzzy_match_score'] = matched_scores  # Add the match score column

    # remove institution name from transaction report
    df_transaction.drop([transaction_on],axis=1)
    
    return df_transaction

def save_joined_dataframe(df,file_name):


    out_file = './2_fetch/tmp/' + file_name
    
    df.to_csv(out_file)

