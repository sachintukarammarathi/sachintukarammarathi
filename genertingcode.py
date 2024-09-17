import random
import string

# Get the desired password length from the user
try:
    length = int(input("Enter the desired password length: "))
    if length < 1:
        print("Please enter a positive integer for the length.")
    else:
        # Define character sets for the password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate the password using random choice
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the generated password
        print(f"Generated Password: {password}")

except ValueError:
    print("Please enter a valid number.")