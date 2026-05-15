# ─────────────────────────────────────────
# ValueError
# Raised when a function gets the right type but an inappropriate value
# ─────────────────────────────────────────
try:
    num = int("banana")   # "banana" can't be converted to an integer
except ValueError:
    print("ValueError: Cannot convert that string to an integer.")
else:
    print(f"Conversion successful: {num}")
finally:
    print("Let's try another one...\n")


# Another way to raise ValueError
try:
    num2 = int("")   # empty string also causes ValueError
except ValueError:
    print("ValueError: Cannot convert an empty string to an integer.")
else:
    print(f"Result: {num2}")
finally:
    print("Let's try another one...\n")


# ─────────────────────────────────────────
# NameError
# Raised when a variable is used before being defined
# ─────────────────────────────────────────
try:
    m = banana   # 'banana' hasn't been defined as a variable
except NameError:
    print("NameError: Tried to use a variable that hasn't been defined.")
else:
    print(m)
finally:
    print("Let's try another one...\n")


# ─────────────────────────────────────────
# TypeError
# Raised when an operation is applied to the wrong data type
# ─────────────────────────────────────────
try:
    result = "hello" + 5   # can't add a string and an integer
except TypeError:
    print("TypeError: Cannot add a string and an integer together.")
else:
    print(f"Result: {result}")
finally:
    print("Let's try another one...\n")


# Another way to raise TypeError
try:
    result2 = len(42)   # len() doesn't work on integers
except TypeError:
    print("TypeError: len() doesn't work on an integer.")
else:
    print(f"Result: {result2}")
finally:
    print("Let's try another one...\n")


# ─────────────────────────────────────────
# SyntaxError
# Raised when Python can't parse the code — must be triggered via eval() or exec()
# because a true SyntaxError prevents the file from running at all
# ─────────────────────────────────────────
try:
    eval("def ()")   # invalid syntax inside a string, caught at runtime via eval
except SyntaxError:
    print("SyntaxError: The code string has invalid Python syntax.")
else:
    print("No syntax error found.")
finally:
    print("Let's try another one...\n")


# ─────────────────────────────────────────
# BONUS examples from w3schools review
# ─────────────────────────────────────────

# ZeroDivisionError
try:
    x = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")
finally:
    print("Let's try another one...\n")

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[10])   # index 10 doesn't exist
except IndexError:
    print("IndexError: List index is out of range.")
finally:
    print("Let's try another one...\n")

# KeyError
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])   # key "age" doesn't exist
except KeyError:
    print("KeyError: That key does not exist in the dictionary.")
finally:
    print("Let's try another one...\n")

# FileNotFoundError
try:
    f = open("nonexistent_file.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError: The file could not be found.")
finally:
    print("Let's try another one...\n")