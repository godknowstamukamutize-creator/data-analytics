# min_max.py
# Finds and displays the smallest and largest of three numbers

a = 42
b = 17
c = 85

# Find minimum
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Find maximum
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The three numbers are: {a}, {b}, {c}")
print(f"Smallest: {smallest}")
print(f"Largest:  {largest}")