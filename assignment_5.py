
import re

try:
    # Ask the user to enter the ticket information
    text = input("Enter your order: ")

    # Extract all numbers from the text
    numbers = re.findall(r"\d+(?:\.\d+)?", text)

    # Check if exactly two numbers were found
    if len(numbers) != 2:
        raise ValueError("The order must contain exactly two numbers!")

    # Convert the extracted numbers to numeric values
    ticket_quantity = int(numbers[0])
    ticket_price = float(numbers[1])

    # Calculate the total price
    total_price = ticket_quantity * ticket_price

    # Check if the quantity is greater than zero
    if ticket_quantity <= 0:
        raise ValueError("Ticket quantity must be greater than zero!")

    # Check if the ticket price is greater than zero
    if ticket_price <= 0:
        raise ValueError("Ticket price must be greater than zero!")

except (ValueError, IndexError) as e:
    print(f"Error: {e}")

else:
    # Display the successful result
    print(f"Ticket quantity: {ticket_quantity}")
    print(f"Price per ticket: {ticket_price:.2f} GEL")
    print(f"Total price: {total_price:.2f} GEL")

finally:
    # This message is displayed regardless of success or failure
    print("[System]: Order processing finished.")
