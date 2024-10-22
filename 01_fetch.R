
# Load the input data - transactions, known member fees, university types, representatives

p1 <- list(
  
  # Load a recent transaction report manually exported from MemberClicks
  tar_target(p1_transaction_data_csv, 
             'transaction-report-09-23-2024.csv', 
             format='file'),
  tar_target(p1_transaction_data_raw, read_csv(p1_transaction_data_csv,
                                               col_types = list('Profile ID' = 'c'),
                                               show_col_types = FALSE)),
  
  # Load the known membership fees data
  tar_target(p1_membership_fees_csv, 
             '01_fetch/in/membership_fees.csv',
             format = 'file'),
  tar_target(p1_membership_fees,  read_csv(p1_membership_fees_csv,
                                           show_col_types = FALSE))
  
)
