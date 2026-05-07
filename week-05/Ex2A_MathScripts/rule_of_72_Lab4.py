savings = 5000.00
interest_rate = 0.06

years_to_double = 72 / (interest_rate * 100)
doubled_balance = savings * 2

print(f"Your current savings is {savings}.")
print(f"At a {interest_rate:.0%} interest rate, your savings account will be worth {doubled_balance:.2f} in {years_to_double:.1f} years")