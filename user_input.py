# Name (string)
name = input("What is your name? ")

# Age (integer)
while True:
    age = input("How old are you? ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Please enter a valid age (integer only).")

# Location (string)
location = input("Where do you live? ")

print(f"Hello {name}, you are {age} years old and live in {location}.")
