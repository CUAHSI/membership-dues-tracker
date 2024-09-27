
# Load the input data - transactions, known member fees, university types, representatives

p1 <- list(
  
  tar_target(p1_transaction_report_csv, 
             'transaction-report-09-23-2024.csv', 
             format='file'),
  tar_target(p1_transaction_report, read_csv(p1_transaction_report_csv,
                                             show_col_types = FALSE))
  
)
