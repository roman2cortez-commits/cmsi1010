import random
import statistics

starting_money = 10000
monthly_contribution = 500
years = 30


average_return = 0.07


volatility = 0.15


simulations = 10000



final_balances = []

for simulation in range(simulations):

    balance = starting_money

    for year in range(years):

        
        yearly_return = random.gauss(
            average_return,
            volatility
        )

        
        balance = balance * (1 + yearly_return)

        
        balance = balance + (monthly_contribution * 12)

    final_balances.append(balance)



final_balances.sort()

median = statistics.median(final_balances)

worst_case = final_balances[int(simulations * 0.05)]
best_case = final_balances[int(simulations * 0.95)]

average = statistics.mean(final_balances)


print("--------------------------------")
print("MONTE CARLO SIMULATION")
print("--------------------------------")

print(f"Starting money: ${starting_money:,.2f}")
print(f"Monthly contribution: ${monthly_contribution:,.2f}")
print(f"Years invested: {years}")
print(f"Simulations: {simulations}")

print("\nRESULTS")
print("--------------------------------")

print(f"Average final balance: ${average:,.2f}")
print(f"Median final balance: ${median:,.2f}")

print(f"\n5th percentile: ${worst_case:,.2f}")
print(f"95th percentile: ${best_case:,.2f}")