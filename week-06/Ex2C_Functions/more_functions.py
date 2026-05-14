# Function 1: Display a mailing label
def display_mailing_label(name, address, city, state, zip):
    print(f"{name}")
    print(f"{address}")
    print(f"{city}, {state} {zip}")
    print()

    # Function 2: Add any number of integers
def add_numbers(*args):
    result = sum(args)
    equation = ' + '.join(str(n) for n in args)
    print(f"{equation} = {result}")

    # Function 3: Display a receipt
def display_receipt(total_due, amount_paid):
    print(f"Total Due:    ${total_due:.2f}")
    print(f"Amount Paid:  ${amount_paid:.2f}")
    print()
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due:   ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining balance to be paid: ${balance:.2f}")
    print()  

    # --- Calling display_mailing_label() ---
display_mailing_label('Jane Smith', '123 Main St', 'Dallas', 'TX', '75001')
display_mailing_label('John Doe', '456 Oak Ave', 'Austin', 'TX', '78701')

# --- Calling add_numbers() ---
add_numbers(5)                      
add_numbers(10, 20)               
add_numbers(3, 7, 12, 4, 9)        

# --- Calling display_receipt() ---
display_receipt(50.00, 60.00)   # overpay
display_receipt(50.00, 50.00)   # exact payment
display_receipt(50.00, 30.00)   # underpay

# BONUS a) Mailing label with optional second address line
def display_mailing_label2(name, address1, city, state, zip, address2=None):
    print(f"{name}")
    print(f"{address1}")
    if address2:
        print(f"{address2}")
    print(f"{city}, {state} {zip}")
    print()

    display_mailing_label2('Acme Corp', '789 Business Blvd', 'Houston', 'TX', '77001', 'Suite 400')

# BONUS b) Receipt with multiple balances
def display_receipt2(amount_paid, *totals):
    total_due = sum(totals)
    print(f"Total Due:    ${total_due:.2f}")
    print(f"Amount Paid:  ${amount_paid:.2f}")
    print()
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due:   ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining balance to be paid: ${balance:.2f}")
    print()

display_receipt2(100.00, 40.00, 35.00, 20.00)  # three balances totaling $95