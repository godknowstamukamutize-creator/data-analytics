import math

cust_list = []

class RewardsProgram:
    '''Enhanced rewards program that tracks restaurants visited
    and rewards points earned per visit.'''

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []   # default empty list
        self.rewards_points = 0         # default 0

    def profile(self):
        print(f"Name:  {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))

    def calculate_rewards(self, bill):
        # $1 = 1 point, rounded down
        return math.floor(bill)

    def visit_rest(self):
        rest_name = input("Name of restaurant: ")
        if rest_name not in self.restaurants_visited:
            self.restaurants_visited.append(rest_name)

        bill = float(input("What was the total food bill for this visit? $"))
        points_earned = self.calculate_rewards(bill)
        self.rewards_points += points_earned

        print(f"Points for this visit:        {points_earned}")
        print(f"Total rewards points earned:  {self.rewards_points}")
        print(f"Thank you for visiting {rest_name}!")


# Test
cust1 = RewardsProgram('Alice Johnson', '555-1234', 'alice@email.com')
cust1.profile()
cust1.visit_rest()
cust1.visit_rest()