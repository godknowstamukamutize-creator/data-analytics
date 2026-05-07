salary = 4500.00
tax_rate = 0.23
taxes_withheld = salary * tax_rate
take_home = salary - taxes_withheld

print(f"Your monthly salary is ${salary:.2f}")
print(f"Federal taxes withheld (23%): ${taxes_withheld:.2f}")
print(f"Take-home pay: ${take_home:.2f}")