# Description: This script tests various numeric 
#              conversion techniques
# Author: Sam Q. Newprogrammer
 
# --- Define variables ---
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# VARIABLE a: " 101.1 "
# a) Cast as integer using int()
# int(a) # ValueError: invalid literal for int() with base 10: ' 101.1 '

# b) Cast as float using float()
a_float = float(a)  # Works! Python strips whitespace automatically for float()

# c) Cast as float then integer
a_float_then_int = int(float(a))  # Works! Result: 101 (truncates decimal)

# d) Use slicing to extract just the numeric portion, then cast
a_stripped = a.strip()          # Remove leading/trailing spaces -> "101.1"
a_sliced = float(a_stripped)    # Cast to float since it has a decimal -> 101.1

# e) Use .strip() to remove leading/trailing spaces
print(".strip() on a:", a.strip())

print(a, type(a))
print(a_float, type(a_float))
print(a_float_then_int, type(a_float_then_int))
print(a_sliced, type(a_sliced))

# VARIABLE B: '55'
# a) Cast as integer using int()
b_int = int(b)      # Works! Result: 55
 
# b) Cast as float using float()
b_float = float(b)  # Works! Result: 55.0
 
# c) int(float()) -- only required for a, skipping here
 
# d) Use slicing to extract numeric portion (entire string is numeric)
b_sliced = int(b[0:2])  # Slices full string "55", casts to int -> 55
 
# e) .strip() -- b has no whitespace, but it works without error
print(".strip() on b:", b.strip())
 
print(b, type(b))
print(b_int, type(b_int))
print(b_float, type(b_float))
print(b_sliced, type(b_sliced))

# VARIABLE C: "402 Stevens"
# a) Cast as integer using int()
# int(c)  # ValueError: invalid literal for int() with base 10: '402 Stevens'
 
# b) Cast as float using float()
# float(c)  # ValueError: could not convert string to float: '402 Stevens'
 
# c) int(float()) -- only required for a, skipping here
 
# d) Use slicing to extract just the numeric portion "402" (indices 0-2)
c_sliced = int(c[0:3])  # Slices "402" from "402 Stevens", casts to int -> 402
 
# e) .strip() -- c has no leading/trailing whitespace, but works without error
print(".strip() on c:", c.strip())
 
print(c, type(c))
print(c_sliced, type(c_sliced))

# VARIABLE D: 'Number 5 '

# a) Cast as integer using int()
# int(d)  # ValueError: invalid literal for int() with base 10: 'Number 5 '
 
# b) Cast as float using float()
# float(d)  # ValueError: could not convert string to float: 'Number 5 '
 
# c) int(float()) -- only required for a, skipping here
 
# d) Use slicing to extract just the numeric portion "5" (index 7)
d_sliced = int(d[7])  # Slices "5" from "Number 5 ", casts to int -> 5
 
# e) Use .strip() to remove trailing space
print(".strip() on d:", d.strip())
 
print(d, type(d))
print(d_sliced, type(d_sliced))
