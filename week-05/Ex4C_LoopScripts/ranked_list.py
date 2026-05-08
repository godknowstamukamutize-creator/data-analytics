# Displays a numbered ranked list using enumerate(), with a top pick label
# BONUS: also prints the list in reverse order
 
favorites = ["tacos", "ramen", "jerk chicken", "injera", "pierogi", "dumplings"]
 
print("My Favorite Foods (in order):")
for index, item in enumerate(favorites, start=1):
    if index == 1:
        print(f"{index}. {item} <- top pick!")
    else:
        print(f"{index}. {item}")
 
print()
 
# BONUS: reverse order, still numbered 1 through len(favorites)
print("My Favorite Foods (reversed, re-numbered):")
for index, item in enumerate(reversed(favorites), start=1):
    if index == 1:
        print(f"{index}. {item} <- top pick!")
    else:
        print(f"{index}. {item}")
