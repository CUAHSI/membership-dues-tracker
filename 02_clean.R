
# Handle eccentricities of the payment data - collapse multiple invoice rows 
# into one, assign the correct payment type to each transaction

# Load modular function files
source('02_clean/src/prep_transaction_data.R')

p2 <- list(
  
  tar_target(p2_transaction_data_ready, format_transaction_data_columns(p1_transaction_data_raw))
  
)
