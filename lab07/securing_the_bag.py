balance = 10000
interest_rate = 0.14
tax_rate = 0.25         
years = 40
deposit = 1000

print(f"at the start you have,{balance:.2f}")
for year in range(1, years + 1):
    interest_earned = balance * interest_rate
    taxes = interest_earned * tax_rate
    balance += taxes
    balance += deposit
    balance += interest_earned
    print(f"After year {year} you have {balance:.2f}")