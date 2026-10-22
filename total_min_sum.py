
total = 0
count = 0
numbers = []

while True:
    user_input = input("Enter a number or 'stop': ")

    if user_input.lower() == "stop":
        break

    try:
        number = float(user_input)

        total += number
        count += 1
        numbers.append(number)

    except ValueError:
        print("Invalid input! Please enter a number or 'stop'.")

print("Sum:", total)
print("Count:", count)

if count > 0:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
    print("No numbers were entered.")

while True:
    try:
        height = int(input("Enter pyramid height (1-8): "))

        if 1 <= height <= 8:
            break
        else:
            print("Height must be between 1 and 8.")

    except ValueError:
        print("Invalid input! Please enter a whole number.")

for row in range(1, height + 1):
    for space in range(height - row):
        print(" ", end="")

    for symbol in range(row):
        print("#", end="")

    print()