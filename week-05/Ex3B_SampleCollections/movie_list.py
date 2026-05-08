movies = ["Inception", "The Matrix", "Arrival", "Spirited Away"]

# Length of list
print(f"The list movies includes my top {len(movies)} favorite movies")

# Print full list
print(movies)

# sorted()
print(sorted(movies))
print(movies)

# sorted() creates a temporary sorted copy
# The original list does not change

# -----------------------------
# .sort()
# -----------------------------

movies.sort()
print(movies)

# .sort() permanently changes the list

# -----------------------------
# append()
# -----------------------------

movies.append("The Dark Knight")

print(f"The updated movies list includes {len(movies)} movies")

print(movies)

