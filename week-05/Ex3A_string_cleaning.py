name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# lower()
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# -----------------------------
# title()
# -----------------------------
print(name_1.title())
print(name_2.title())
print(name_3.title())

# -----------------------------
# replace()
# -----------------------------

salary1_clean = salary_1.replace("$", "")
salary2_clean = salary_2.replace("$", "")

print(salary1_clean)
print(salary2_clean)

print(type(salary1_clean))
print(type(salary2_clean))

# They are still strings.
# We must remove commas and cast to int
# before performing math.

# -----------------------------
# replace() + int()
# -----------------------------

salary1_int = int(salary_1.replace("$", "").replace(",", ""))

print(salary1_int)
print(type(salary1_int))