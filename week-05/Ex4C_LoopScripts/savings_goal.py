# Uses a while loop to simulate saving toward a goal, with milestone messages
 
balance = 500.00       # starting bank balance
goal = 3000.00         # savings goal
weekly_savings = 200.00  # amount saved each week
 
treat_cost = 25.00     # cost of a little treat (used when balance >= 75% of goal)
 
while balance < goal:
    balance += weekly_savings
 
    halfway = goal * 0.50
    almost = goal * 0.75
 
    if balance >= almost:
        balance -= treat_cost
        print(f"So close! After treating myself, my balance is up to ${balance:,.2f}")
    elif balance >= halfway:
        print(f"Almost there! This week my balance is up to ${balance:,.2f}")
    else:
        print(f"This week my balance increased to ${balance:,.2f}")
 
print(f"Goal met! My current balance is ${balance:,.2f}")
 
