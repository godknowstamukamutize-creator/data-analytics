# Candy tuple
candies = ("Gummy Bears", "Lollipops", "Jelly Beans")

# Flavor tuple
flavors = ("Mango", "Strawberry", "Blue Raspberry")

# Set of candy combinations
candy_options = {
    candies[0] + " - " + flavors[0],
    candies[1] + " - " + flavors[1],
    candies[2] + " - " + flavors[2]
}
# Output
print("Today's candy options include:")
print(candy_options)
# Notice: The ORDER of items may differ each time you run the script!
# Sets are UNORDERED -- Python does not guarantee any particular order.
# This is a key difference from lists and tuples.
