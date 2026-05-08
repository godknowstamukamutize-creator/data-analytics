# Loops through sales records, prints summaries, flags top performers,
# and totals all sales (BONUS)
 
sales_data = [
    ('Marcus Webb',    'East',  4250.00),
    ('Priya Sharma',   'West',  5875.50),
    ('DeShawn Carter', 'East',  3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen',     'West',  4980.25),
]
 
total_sales = 0.00  # BONUS: track overall total
 
for name, region, sales in sales_data:
    print(f"{name} ({region}): ${sales:,.2f}")
    if sales > 5000:
        print(" ^ Top performer!")
    total_sales += sales
 
# BONUS: print the grand total after the loop
print(f"\nTotal sales across all employees: ${total_sales:,.2f}")
 
