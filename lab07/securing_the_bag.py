def investment_value(start, interest_rate, tax_rate, deposit, years):
    balance = start
    for _ in range(1, years + 1):
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
    return balance
print(investment_value(1000, 0.05, 0, 0, 10))  # should be 1628.89
print(investment_value(1000, 0.05, 0, 100, 10))  # should be 2886.68
print(investment_value(10000, 0.13, 0.25, 1000, 30))  # should be 319883.75
print(investment_value(1, 1, 0, 0, 20)) # should be 1048576.0


{


    
}