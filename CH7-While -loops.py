# WHILE loops
# while loops run as long as, or while, certain conditions are true
print('\n')
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#Letting the user choose when to quit
# print("\n")
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# message = ""

# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit': # this if statement does not print quit.
#         print(message)

# Using a FLAG
# flag - variable that acts as a signal to the program
print("\n")
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True # this is flag variable
while active:
    message = input(prompt)

    if message == 'quit':
        active = False # changes the FLAG variable enabling program to quit
    else:
        print(message)

# Using BREAK to exit a looop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: # a loop that starts with 'while True' will run until it reaches break statement
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"\nI'd love to go to {city.title()}! ")

# using CONTINUE in a loop
print("\n")

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Avoiding infinite loops
# press CTRL + C to break an infiite loop

# Challenge 2
print("\n")

# 7-4 pizza toppings
prompt = "\nWhat toppings would you like on your pizza? "
prompt += "\nEnter 'quit' to exit when done. "
toppings = []

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
        toppings.append(topping)
    else:
        print("\nYour order is complete. You ordered a pizza with:")
        for top in toppings:
            print(f"{top}")
        print("\nIt will be out shortly. Enjoy!")
        break
            
# Movie tickets
prompt = "\nWelcome to AMC theaters. Enter your age for ticket pricing. "

while True:
    age = input(prompt)
    age = int(age)

    if age > 0 and age < 3:
        print("Your ticket is free. Enjoy!")
        break
    elif age >= 3 and age <= 12:
        print("That'll be $10.")
        break
    elif age > 12:
        print("Damn, you're old. That'll be $15!")
        break
    else:
        print("Please enter a valid age.")
        break

# Using a While Loop with Lists and Dictionaires
# moving Items from one List tddubplate1

#start with users that need to be verified
# and an empty list to hold confirmed users
print('\n')
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users
# move each verified user into the list of confirmed users
while unconfirmed_users: # loops as long as list is not empty
    current_user = unconfirmed_users.pop() # removes index starting with last

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user) # adds the "popped" user to the confirmed user list

 # Display all confirmed users
print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title()) # loops through confirmed user and prints

# REMOVING All Instances of Specific Values froma List
# for more than one instance of repeated value, use a while loop to remove
print('\n')
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# FIlling a DICTIONARY with User Input
print('\n')

responses = {}

# set flag to indicate that  polling is active
polling_active = True

while polling_active:
    #Prompt the person's name and response.
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll. 
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False
    
print(responses)

# Polling is complete. Show the results. 
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


# End of Chapter Challenges
# 7-8 Deli
sandwich_orders = ['pastrami', 'italian', 'pastrami', 'ham and cheese', 'turkey bacon', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I have made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"How was your {sandwich} sandwich?")
print(finished_sandwiches)
print(sandwich_orders)

# 7-9 No Pastrami
print("\n")
sandwich_orders = ['pastrami', 'italian', 'pastrami', 'ham and cheese', 'turkey bacon', 'pastrami']
finished_sandwiches = []

#remove pastrami from sandwich orders
print("Sorry! The deli has run out of pastramai")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I have made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"How was your {sandwich} sandwich?")
print(finished_sandwiches)
print(sandwich_orders)

# 7-10 Dream Vacation
print("\n")

responses = {} # creates dicitonary to store username and response
active_polling = True # use as flag to continue/stop

while active_polling:
    name = input("\nWhat's your name? ")
    response = input("\nWhere would you go on your dream vacation? ")

    #store the response in dictionary
    responses[name] = response

    #find out if anyone else will take it
    repeat = input("Will anyone else be answering? (yes / no) ")

    if repeat == 'no':
        active_polling = False

# loop trhough dictionary and print responses
print("\n")
for name, response in responses.items():
    print(f"{name.title()}'s dream vacation is to go to {response.title()}. ")
