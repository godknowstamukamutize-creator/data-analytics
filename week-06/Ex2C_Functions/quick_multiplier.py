# Step 2: Doubler lambda
doubler = lambda n: n * 2

# Step 3: Test doubler
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# Step 4: Tripler lambda
tripler = lambda n: n * 3

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

# Step 5: multiplier() function that returns a lambda
def multiplier(x):
    return lambda n: n * x

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler  = multiplier(6)
septupler  = multiplier(7)
octupler   = multiplier(8)
nonupler   = multiplier(9)
decupler   = multiplier(10)

# Step 6: Test each one
print(quadrupler(5))
print(quintupler(5))
print(sextupler(5))
print(septupler(5))
print(octupler(5))
print(nonupler(5))
print(decupler(5))

# Get name from user
name = input("Enter a name: ")

# Function to truncate the name for the song
def trunc_name(name):
    name = name.lower()
    vowels = 'aeiou'
    if name[0] in vowels:
        return name          # Ann → ann
    elif name[1] in vowels:
        return name[1:]      # Dan → an
    else:
        return name[2:]      # Stan → an

# Test trunc_name
# print(trunc_name(name))

# Generator function for the name game
def name_game(name):
    n = name.capitalize()
    t = trunc_name(name)
    yield f"{n}, {n}, bo-b{t}"
    yield f"banana fana fo-f{t}"
    yield f"me my mo-m{t}"
    yield f"{n}!"

# Test with multiple names
test_names = [name, 'carly', 'CHARLIE', 'Aidan', 'Billy']

for test in test_names:
    print()
    for line in name_game(test):
        print(line)