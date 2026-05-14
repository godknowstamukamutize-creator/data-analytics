import random
import math
import statistics

# Starting variables
vals_1_100 = range(1, 100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)
radius = random.randint(3, 10)
pi = math.pi

# --- Calculations for subset (75 samples) ---
sample_sum = sum(vals_sample)
sample_avg = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

# --- Calculations for superset (200 values) ---
choices_avg = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_stdev = statistics.stdev(vals_choices)
choices_variance = statistics.variance(vals_choices)

# --- Circle calculations ---
area = pi * (radius ** 2)
area_ceil = math.ceil(area)   # rounded up
area_floor = math.floor(area) # rounded down

# --- Output ---
print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_avg}")
print(f"Median of 75 sample values: {sample_median}")

print('\n')

print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {choices_avg}")
print(f"Median of 200 values: {choices_median}")
print(f"Mode of 200 values: {choices_mode}")
print(f"Standard deviation of 200 values: {choices_stdev}")
print(f"Variance of 200 values: {choices_variance}")

print('\n')

print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_ceil} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_floor} (rounded down to the nearest integer)")