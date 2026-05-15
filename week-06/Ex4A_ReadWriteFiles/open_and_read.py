# Open the file in read mode
f = open('about_me.txt', 'r')

# --- SECTION 1: .read() ---
# Reads the entire file at once
print(f.read())

# .read(50) reads 50 characters; the second call continues from where it left off
# print(f.read(50))
# print(f.read(50))

f.close()

f = open('about_me.txt', 'r')

# --- SECTION 2: .readline() ---
# Reads first 10 characters of line 1
print(f.readline(10))

# Reads the rest of line 1 (no argument = reads to end of current line)
print(f.readline())

# Loop reads the next 4 lines one at a time
for i in range(1, 5):
    print(f.readline())

f.close()

f = open('about_me.txt', 'r')

# --- SECTION 3: .readlines() ---
# .readlines(1)  → returns first line as a list
print(f.readlines(1))

# Second .readlines(1) → continues from where it left off
print(f.readlines(1))

# .readlines(10) → reads enough lines to cover ~10 bytes, rounded up to full lines
print(f.readlines(10))

# .readlines(100) → same idea but larger hint
print(f.readlines(100))

# .readlines(-1) → reads all remaining lines (same as no argument)
print(f.readlines(-1))

f.close()

f = open('about_me.txt', 'r')

# Variable 1: first 50 characters using .read()
var1 = f.read(50)

# Variable 2: next 4 lines using .readline() in a loop, stored as a list
var2 = []
for i in range(4):
    var2.append(f.readline())

# Variable 3: next chunk as a list of complete lines using .readlines()
var3 = f.readlines(100)

f.close()

# Print combined output
print(f"First 50 characters: {var1}")
print(f"Next four lines, as list by line: {var2}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {var3}")