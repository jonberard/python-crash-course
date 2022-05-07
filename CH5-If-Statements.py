# IF STATEMENTS
# simple example
cars = ['bmw', 'mercedes', 'chevorlet', 'ford', 'honda']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# conditional tests
car = 'bmw' # assigns value to variable
car == 'bmw'# comparison returns True
car == 'audi' # comparison returns False

# Ignorig case when checking for equality
# Testing for equality is case sensitive in Python
# if case matters convert the variable to lower before comparing
car = 'Audi'
car.lower() == 'audi' # Comparison returns True and doesn't affect variable assignment

#Checking for INEQUALITY !=
requested_toppings = 'anchovies'
if requested_toppings != 'mushrooms':
    print('Hold the mushrooms!')

#Numerical Comparisons
age = 18
age == 18 # returns TRUE

if age < 18:
    print('You\'re not old enought to vote!')
else:
    print('The voting booth is ahead and to your left.')

#Checking multiple conditions using and
wants_to_vote = True
if age >= 18 and wants_to_vote == True:
    print('Every vote counts! Proceed to the booth.')
else:
    print('Come back when you 18 and want to vote!')

# Checking multiple conditions using 'or'
age_0 = 18
age_1 = 21
if age_0 >= 21 or age_1 >= 21:
    print('Have fun!')
else:
    print('come on back in a few years!')

# Checking whether a Value is or isn't in a List
'bmw' in cars # returns True

users = ['Jacob', 'Susan', 'Dan', 'Brooke']
user = 'Billy'
if user not in users:
    print(f'{user}, you are banned from this forum!')
else:
    print("Welcome back!")

# CHALLENGE 1
# 5-1 Conditional Tests
car = 'bmw'
print('Is car == bmw? I predict True.')
print(car == 'bmw')

print('\nIs car == \'bmx\'? I predict False')
print(car == 'bmx')

if car.lower() == 'bmw':
    print(f'I want to buy a new {car.upper()}.')
else:
    print('Enjoy your new ride!')

lucky_number = 7
if lucky_number == 7:
    print('We have the same lucky number!')
elif lucky_number < 7:
    print('You\'re lucky number ius lower than mine.')
else:
    print('You have a higher lucky number.')

'ford' in cars #returns True
'Volkswagen' in cars # returns False

if 'ford' and 'chevorlet' in cars:
    print('You\'ve narrowd it down to two great American cars')

# if elif else statements only need one test to pass before it stops.
# if you need more than one to pass use simple if statement
print('\n')
if 'ford' in cars:
    print("You're buying a Ford.")
if 'chevorlet' in cars:
    print("You're buying a Chevorlet.")
if 'bmw' in cars:
    print("You're buying a BMW!")

# CHALLENGE 2
# 5-3 Alien Colors 1
alien_color = 'red'
if 'green' in alien_color:
    print('You just earned 5 points!')
alien_color = 'green'
if 'green' in alien_color:
    print('You just earned 5 points!')

# 5-4 Alien Colors 2
print('\n')
alien_color = 'yellow'
if alien_color is 'green':
    print("You just earned 5 points")
else:
    print("You just earned 10 points!")

# 5-5 Alien Colors 3
print('\n')
alien_color = 'red'
if alien_color is 'green':
    print("You've earned 5 points.")
elif alien_color is "yellow":
    print("You've earned 10 points!")
elif alien_color is 'red':
    print("You've earned 15 points!")

# 5-6 Stages of Life
print('\n')
age = 76
if age < 2:
    print("You're just a baby!")
elif age >= 2 and age < 4:
    print("You're a little toddler.")
elif age >= 4 and age < 13:
    print("You're just a kid.")
elif age >= 13 and age < 20:
    print("You're a troubled teenager!")
elif age >= 20 and age < 65:
    print("You're am adult.")
else:
    print("You're a senior! Enjoy life!")

# 5-7 Favorite Fruits
print('\n')
favorite_fruits = ['pineapple', 'apple', 'strawberry', 'watermelon']
if 'pineapple' in favorite_fruits:
    print("You really like pineapples!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'strawberry' in favorite_fruits:
    print('You really like strawberries!')

#Using if statements with lists
print('\n')
requested_toppings = ['anchovies', 'black olives', 'green peppers', 'mushrooms']
# using a for loop to handle an out of stock topping
for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print("I'm sorry! We are currently out of mushrooms.")
    else:
        print(f"Adding {requested_topping}")


# checking that a list is not empty
print('\n')
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"adding {requested_topping}!")
    print("Finished making your pizza")
else:
    print('Are you sure you want a plain pizza?')

# Using multiple lists
print('\n')
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'pepperoni']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"We don't have {requested_topping}.")
print("\nYou're pizza is finished!")

# Challenge 3
# Hello Admin
print('\n')
usernames = ['admin Jon', 'admin Brooke', 'admin Bodhi', 'admin Bash', 'Fred']
for username in usernames:
    if 'admin' in username:
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f'Hello {username}, thank you for loggin in again.')

# 5-9 No Users
print('\n')
usernames = []
for username in usernames:
    print(f"Hello {username}!")
else:
    print('We need to find some damn users!')

# 5-10 Checking Usernames
current_users = ['junebug', 'torch_boy', 'glitter_girl', 'BJB3124', 'DanandDave']
new_users = ['jonton', 'dork', 'junebug', 'bjb3124', 'DonkyKong']
current_users_lower = [user.lower() for user in current_users] # List comprehension FTW

# current_users_lower = current_users[:].lower()
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is already taken. You'll need a different username.")
    else:
        print(f"{new_user} is availble. Register now!")

# 5-11 Ordinal Numbers
print("\n")
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
for number in ordinal_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

# SELF CHALLENGE - Check to see if flight is avaible.
print('\n')
available_flights = ['UAL2123', "AAL234", "SWA345", "AAY1235"]
user_flights = ['ual2123', "SWA235", 'AAY1235', 'JBU1078']
available_flights_lower = [flight.lower() for flight in available_flights]
for user_flight in user_flights:
    if user_flight.lower() in available_flights_lower:
        print(f"{user_flight.upper()} is available to book!") #converts back to upper
    else:
        print(f"{user_flight} is sold out. Try searching again to a different destination.")
