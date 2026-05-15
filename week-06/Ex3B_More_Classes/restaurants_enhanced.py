class Restaurant:
    '''Represents a restaurant with a name, food type, customers served,
    and customer ratings. Includes methods to update and display this info.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0        # default
        self.customer_ratings = []    # default empty list

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        served_today = int(input("How many customers served today? "))
        self.number_served += served_today

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            raw = input("Rate your experience 1-5 (5 = excellent): ")
            # Validate: must be a whole number integer between 1 and 5
            if raw.isdigit() and 1 <= int(raw) <= 5:
                rating = int(raw)
                self.customer_ratings.append(rating)
                avg = sum(self.customer_ratings) / len(self.customer_ratings)
                print(f"Your rating was {rating}. "
                      f"The average rating for {self.rest_name} is {avg:.1f}.")
                break
            else:
                print("Invalid input. Please enter a whole number between 1 and 5.")


# Three instances
rest1 = Restaurant('Olive Garden', 'Italian food')
rest2 = Restaurant('Nobu', 'Japanese food')
rest3 = Restaurant('In-N-Out', 'American burgers')

# Test print_num_served → add → print again
for rest in [rest1, rest2, rest3]:
    print()
    rest.print_num_served()       # initial value (0)
    rest.add_num_served()
    rest.add_num_served()
    rest.print_num_served()       # updated total

# Test customer_rating several times per restaurant
for rest in [rest1, rest2, rest3]:
    print()
    rest.customer_rating()
    rest.customer_rating()
    rest.customer_rating()