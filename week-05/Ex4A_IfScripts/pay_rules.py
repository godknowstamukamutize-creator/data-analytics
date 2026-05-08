# pay_rules.py

# Starting variables
pay_rate = 17.30
hours_worked = 45

# Calculate gross pay
if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = pay_rate * hours_worked

# Display results
print("Pay Rate: $", pay_rate)
print("Hours Worked:", hours_worked)
print("Gross Pay: $", round(gross_pay, 2))

# bonus_gregorian_calendar.py

year = 2000

if year % 400 == 0:
    print(year, "is a leap year")
elif year % 100 == 0:
    print(year, "is NOT a leap year")
elif year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is NOT a leap year")