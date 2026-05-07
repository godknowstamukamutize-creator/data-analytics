import math

length = 12  # feet
width = 10   # feet
tiles_per_box = 12

area = length * width
tiles_needed = area * 1.10          # add 10% buffer
boxes_needed = math.ceil(tiles_needed / tiles_per_box)  # round UP — can't buy partial boxes

print(f"Room area: {area} sq ft")
print(f"Tiles needed (with 10% buffer): {math.ceil(tiles_needed)}")
print(f"Boxes to buy: {boxes_needed}")