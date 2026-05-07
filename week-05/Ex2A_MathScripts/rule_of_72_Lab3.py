# Using input() lets the user supply values at runtime instead of hardcoding them.
# Pitfall: input() always returns a STRING. If you forget to convert with float(),
# math operations will fail or behave unexpectedly (e.g. "5" + "5" = "55", not 10).
# Another pitfall: the user could type letters or leave the field blank, which would
# cause a crash (ValueError) since float() can't convert non-numeric text.

savings = float(input("What is your current savings amount? "))
interest_rate_pct = float(input("What is your annual interest rate? "))

interest_rate = interest_rate_pct / 100
years_to_double = 72 / interest_rate_pct
doubled_balance = savings * 2

print("Your current savings is " + str(savings) + ".")
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be worth "
      + format(doubled_balance, ".2f") + " in " + format(years_to_double, ".1f") + " years")