avalible_toppings = ['mushrooms','olives','green peppers', 'extra cheese','garlic']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avalible_toppings:
        print(f"adding {requested_topping}.")
    else:
        print(f"sorry we dont have the{requested_topping}.")

print("\nFinished making your pizza!")

