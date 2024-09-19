# need to find reliable way to capture payments that have discount applied (for five year advance payments)

# Idea is to flag values in description column to see if they contain the following (all case insensitive)
# 5 year
# 5-year
# Five year
# five year
# discount

# note advance and pre pay are not good flags as you can pre pay up to 5 years, but only the 5 year advance recevies a discount. 
# thinking of doing flags and searching for payments of 315 and 900 dollars also in "amount" column