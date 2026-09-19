balance=1000
interest_rate=.07
years=20 

print("At the start you have", balance)
for year in range(1, years + 1):
    interest_earned = balance * interest_rate
    balance += interest_earned
    print("after year",year,"you have",balance)