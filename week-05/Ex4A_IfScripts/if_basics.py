# if_basics.py
# Exercise 4.A - Lab 1: If Statement Basics
 
x = 100
y = 20
 
# a) If x divided by y is 5
if x / y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("are the variables set up correctly?")
 
# b) If x times y is y
if x * y == y:
    print("now x times y is y")
    x = 10
else:
    print("Whoops, x equals " + str(x))
 
# c) If x is less than y
if x < y:
    print("x is less than y")
    x = x * 2
else:
    print("uh oh, x is not less than y")
 
# d) If x is greater than y
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")
 
# e) Final print statement
print("The final value of x is " + str(x) + " and the final value of y is " + str(y))
