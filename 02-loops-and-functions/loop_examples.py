# Guided training examples: loops and loop control

# range() uses an exclusive stop value.
for i in range(1, 11):
    print(f"{i} * 2 = {i * 2}")

print()

# break exits the loop when the condition is met.
for i in range(1, 11):
    print(i)
    if i == 6:
        print("The loop stops at", i)
        break

print()

# continue skips the rest of the current iteration.
for i in range(1, 11):
    if i == 6:
        continue
    print(i)

print()

# A while loop repeats while its condition remains true.
i = 0
while i < 10:
    print(i)
    i += 1
