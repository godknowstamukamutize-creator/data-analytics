# Global list to hold all customers — created once outside the class
cust_list = []

class RewardsProgram:
    '''Represents a restaurant rewards program customer.
    Stores contact info and provides profile, thank-you, and list methods.'''

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f"Name:  {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        # Appends this customer as a tuple to the global list
        cust_list.append((self.cust_name, self.phone, self.email))


# Three customer instances
cust1 = RewardsProgram('Alice Johnson', '555-1234', 'alice@email.com')
cust2 = RewardsProgram('Brian Lee',    '555-5678', 'brian@email.com')
cust3 = RewardsProgram('Carmen Diaz',  '555-9012', 'carmen@email.com')

for cust in [cust1, cust2, cust3]:
    cust.profile()
    cust.thank_you()
    cust.add_to_cust_list()
    print()

# Confirm all customers added
print("Customer List:")
for c in cust_list:
    print(c)