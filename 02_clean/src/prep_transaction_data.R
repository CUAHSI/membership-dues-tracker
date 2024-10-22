

format_transaction_data_columns <- function(transaction_data) {
  transaction_data %>% 
    rename(invoice_id = `Invoice ID`,
           memberclicks_id = `Profile ID`) %>% 
    mutate(date = as.Date(`Transaction Date`, format='%m/%d/%Y'),
           payment_year = year(date),
           amount = abs(Amount)) %>% 
    select(payment_year, memberclicks_id, 
           invoice_id, date, amount, details = Description) %>% 
    arrange(payment_year, memberclicks_id, invoice_id, desc(amount))
}

