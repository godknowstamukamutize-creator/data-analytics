import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
             'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# a) Product of the Day - randomly select one item
product_of_day = random.choice(products)
print(f"Product of the Day: {product_of_day}")

# b) Usability survey - select 3 items without replacement
survey_picks = random.sample(products, 3)
print(f"Usability Survey Products: {survey_picks}")

# c) Shuffle all products for presentation (modifies list in place)
random.shuffle(products)
print(f"Randomized Product List: {products}")

# d) Simulated daily transaction count between 50 and 300
transaction_count = random.randint(50, 300)
print(f"Daily Transaction Count: {transaction_count}")