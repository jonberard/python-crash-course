# USER INPUT AND WHILE LOOPS
# input() 
message = input("Tell me something and I will repeat it back to you: ")
print(message)

print('\n')

prompt = "If you tell us who you are, we can, personlize the messages to see who you are."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"Hey, {name.title()}! It's great to meet you.")

# Using int() to accept Numerical Input
print("\n")
age = input('How old are you? ')
age = int(age)
print(age) # prints number as string and you can't do numerical comparisons

# age = int(age) # converts string into numerical representation
if age >= 18:
    print("You can vote!") # allows for numerical comparison now.
else:
    print("You're not old enough to vote!")

# The Modulo Operator
# basically returns the remainder 
# even or odd
print("\n")
number = input("Enter a number and I'll tell you if it's even or odd. ")
if int(number) % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd")

# Challenge 1
# 7-1 Rental Car
print('\n')
rental = input("What brand of rental would you like: ")
print(f"Let me see if I have any {rental.title()}s available.")

# 7-2 Restaurant Seating
print('\n')
group = input("How many people are in your group? ")
group = int(group)

if group > 8:
    print("You'll have to wait for your table.")
else:
    print("Your table is ready!")

# 7-3 Multiples of Ten
print('\n')
user_number = input("Give me a number. Any number. ")
user_number = int(user_number)

if user_number % 10 == 0:
    print(f"{user_number} is a multiple of 10!")
else:
    print(f"{user_number} is NOT a multiple of 10.")

