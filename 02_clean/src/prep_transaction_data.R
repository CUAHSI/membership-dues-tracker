

format_transaction_data <- function(transaction_data, institution_type_xwalk) {
  transaction_data %>% 
    rename(invoice_id = `Invoice ID`,
           memberclicks_id = `Profile ID`) %>% 
    mutate(date = as.Date(`Transaction Date`, format='%m/%d/%Y'),
           payment_year = year(date),
           # We know this is a charge to them, so make those positives (don't
           # use absolute value just in case there is a refund included)
           amount = Amount*-1) %>% 
    # Add in the institution type information
    left_join(institution_type_xwalk, by = "memberclicks_id") %>% 
    # Sort data by year of the payment and institution, then invoice and amount
    arrange(payment_year, memberclicks_id, invoice_id, desc(amount)) %>% 
    # Keep only columns we need
    select(payment_year, 
           memberclicks_id, 
           institution_nm, 
           institution_type,
           invoice_id, 
           date, 
           amount, 
           details = Description)
}

