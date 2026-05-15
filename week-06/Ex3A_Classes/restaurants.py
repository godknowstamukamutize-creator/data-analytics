class Restaurant:
    '''Represents a restaurant with a name and food type.
    Provides methods to describe the restaurant and indicate it is open.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


# Three instances
rest1 = Restaurant('Olive Garden', 'Italian food')
rest2 = Restaurant('Nobu', 'Japanese food')
rest3 = Restaurant('In-N-Out', 'American burgers')

# Call methods for each
rest1.describe_rest()
rest1.rest_open()

rest2.describe_rest()
rest2.rest_open()

rest3.describe_rest()
rest3.rest_open()