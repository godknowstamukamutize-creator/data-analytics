import math

x1, y1 = 1, 2
x2, y2 = 7, 10

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distance between ({x1},{y1}) and ({x2},{y2}) is {distance:.2f}")