import math

tourists = 38
van_capacity = 15
van_cost_per_day = 250.00

vans_needed = math.ceil(tourists / van_capacity)   # round UP — can't have partial vans
total_cost = vans_needed * van_cost_per_day
cost_per_person = total_cost / tourists

print(f"Number of tourists: {tourists}")
print(f"Vans needed: {vans_needed}")
print(f"Total van cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

# Checking the math with 38 tourists:
# a) Cost per person: $19.74 (rounded from 19.736842...)
# b) If you collect $19.74 from each of 38 people: 38 * 19.74 = $750.12
# c) The vans cost: 3 vans * $250 = $750.00
# d) You have $0.12 left over because cost_per_person was a repeating decimal.
#    Dividing $750 evenly among 38 people doesn't come out to a clean cent amount,
#    so when each person pays the rounded-up amount, you collect slightly more than needed.