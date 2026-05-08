# greeting.py

hour = 23

if hour >= 23 or hour < 4:
    print("What are you doing up so late??")
elif hour < 10:
    print("Good morning!")
elif hour < 17:
    print("Good day!")
else:
    print("Good evening!")