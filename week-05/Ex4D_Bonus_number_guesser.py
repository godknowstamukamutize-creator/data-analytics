# A number guessing game that generates a random number WITHOUT using the random module.
# Instead, it builds a list of numbers, shuffles using a dict + sorted trick, then picks one.
 
import time
 
# --- Generate a "random" number without the random module ---
# Build a pool of numbers (1–100)
number_pool = list(range(1, 101))
 
# Shuffle by pairing each number with a pseudo-random key derived from the current time,
# then sort by those keys. This uses two collection types: a list and a dict.
seed = int(time.time() * 1000000)  # microsecond timestamp as our seed
shuffle_keys = {}
for num in number_pool:
    seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF  # linear congruential generator
    shuffle_keys[num] = seed
 
shuffled_pool = sorted(number_pool, key=lambda n: shuffle_keys[n])
secret_number = shuffled_pool[0]  # pick the first number from the shuffled list
 
# --- Game setup ---
low  = 1
high = 100
guess_count  = 0
guessed_nums = []
 
print("=" * 40)
print("      🎯 NUMBER GUESSER GAME 🎯")
print("=" * 40)
print(f"I'm thinking of a number between {low} and {high}.")
print("Can you guess it? Let's find out!\n")
 
# --- Main game loop ---
while True:
    raw = input("Your guess: ").strip()
 
    # Bonus (d): safe handling for non-numeric input
    if not raw.isdigit() and not (raw.startswith('-') and raw[1:].isdigit()):
        print("  ⚠️  That doesn't look like a number. Try again!\n")
        continue
 
    guess = int(raw)
 
    # Check if guess is in range
    if guess < low or guess > high:
        print(f"  ⚠️  Please guess a number between {low} and {high}.\n")
        continue
 
    guess_count  += 1
    guessed_nums.append(guess)
 
    if guess < secret_number:
        print("  📈 Higher!\n")
    elif guess > secret_number:
        print("  📉 Lower!\n")
    else:
        print(f"\n🎉 Correct! The number was {secret_number}!")
        print(f"   You got it in {guess_count} guess{'es' if guess_count != 1 else ''}.")
        break
 
# --- Bonus summary ---
# (b) Print all guessed numbers
print(f"\n📋 Your guesses: {guessed_nums}")
 
# (c) Fewer than 5 guesses = awesome
if guess_count < 5:
    print("⭐ You're awesome — under 5 guesses!")
else:
    print("Good game! Keep practicing. 💪")
 
print("=" * 40)
 
