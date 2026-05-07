savings = 5000.00
interest_rate = 0.06  # 6%

years_to_double = 72 / (interest_rate * 100)
doubled_balance = savings * 2

print("Your current savings is " + str(savings) + ".")
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be worth "
      + format(doubled_balance, ".2f") + " in " + format(years_to_double, ".1f") + " years")