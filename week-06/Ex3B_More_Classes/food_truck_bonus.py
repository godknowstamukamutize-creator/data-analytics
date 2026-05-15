class Restaurant:
    '''Represents a restaurant with a name and food type.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


# Child class inherits from Restaurant
class FoodTruck(Restaurant):
    '''A mobile food truck that inherits from Restaurant.
    Adds booking availability and location tracking.'''

    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)
        self.private_bookings = 'N'
        self.truck_location = ''
        # Challenge: list to track location history (no duplicates — 
        # unique locations are more useful for route/area analysis)
        self.location_history = []

    def accepts_private_bookings(self):
        answer = input("Does this food truck accept private bookings? Y/N: ").strip().upper()
        self.private_bookings = answer
        if answer == 'Y':
            print(f"This food truck currently accepts private bookings.")
        else:
            print(f"This food truck currently does not accept private bookings.")

    def relocate_truck(self):
        location = input("Enter current location (street address and city): ")
        self.truck_location = location
        # Only add to history if not already there
        if location not in self.location_history:
            self.location_history.append(location)
        print(f"Truck is currently located at {location}.")

    def print_location_history(self):
        print("Location history:")
        for loc in self.location_history:
            print(f"  - {loc}")


# Test
truck1 = FoodTruck("Rolling Tacos", "Mexican street food")
truck1.describe_rest()
truck1.rest_open()
truck1.accepts_private_bookings()
truck1.relocate_truck()
truck1.relocate_truck()
truck1.relocate_truck()
truck1.print_location_history()