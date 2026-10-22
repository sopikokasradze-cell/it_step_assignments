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