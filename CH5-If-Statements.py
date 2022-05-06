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
requested_topping = 'anchovies'
if requested_topping != 'mushrooms':
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
