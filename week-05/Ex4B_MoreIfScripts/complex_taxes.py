# complex_taxes.py

hours_worked = 45
pay_rate = 20
filing_status = "single"

# Calculate weekly gross pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

# Annual gross pay
annual_gross = gross_pay * 52

# Determine tax rate
tax_rate = 0

if filing_status == "single":

    if annual_gross < 12000:
        tax_rate = 0.10
    elif annual_gross < 50000:
        tax_rate = 0.20
    else:
        tax_rate = 0.30

elif filing_status == "joint":

    if annual_gross < 24000:
        tax_rate = 0.10
    elif annual_gross < 100000:
        tax_rate = 0.20
    else:
        tax_rate = 0.30

# Weekly tax withholding
tax_withheld = gross_pay * tax_rate

# Net pay
net_pay = gross_pay - tax_withheld

# Output
print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate} per hour, your gross weekly pay is ${gross_pay:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${tax_withheld:.2f}")
print(f"Your net pay is ${net_pay:.2f}")