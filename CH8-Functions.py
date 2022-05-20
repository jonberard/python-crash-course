# FUNCTIONS
# - blocks of code designed to do one specific job.
# - you call a function

# Defining a function
def greet_user():
    """ Display a simple greeting.""" # DOCSTRING - python looks for this when it generates documentation for the functions
    print("Hello!")

greet_user() # this is "calling" the function

# Passing information to a function
print("\n")
def greet_user(username): # username is a parameter - piece of info func needs to do job
    """Take name argument and display text"""
    print(f"Hello, {username.title()}!")

greet_user('Jon') # 'Jon' is the argument passed to func during call

# CHALLENGE 1
# 8-1 message
print("\n")
def display_message():
    """Display simple message"""
    print("I am learning about functions!")

display_message()

# 8-2 Favorite Book
def favorite_book(title):
    """Display message with favorite book"""
    print(f"My favorite books is {title.title()}!")

favorite_book('catcher in the rye')

# POSITIONAL arguments - python matches arguments with the order arguments provided
def describe_pet(animal_type, pet_name):
    """Display inf about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'pink') # order matters when passing arguments in positional argument. See below
describe_pet('pink', 'hamster') #argument in wrong order and makes no sesne

# KEYWORD Arguments - name/value pair that you pass to func
def describe_pet(animal_type, pet_name):
    """Display inf about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='pink')
describe_pet(pet_name='pink', animal_type='hamster') # these two calls are indeifferent because keywords

# DEFAULT Values - python uses defauly arg value if one is provided
def describe_pet(pet_name, animal_type='dog'): # 'dog' is defautl value passed
    """Display inf about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
# When using default values, any parameter with a default value
# needs ti be listed AFTER all the parameters that don't have
# default values. This allows Python to continue interpreting 
# position arguments correctly.

# Equivalent function calls
# a dog named 'willie
describe_pet('willie')
describe_pet(pet_name='willie')

# a hamster named harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# CHALLENGE 2
# 8-3 T-shirt
def make_shirt(size, printed_text):
    """displays shirt info"""
    print(f"\nYou ordered a size {size.capitalize()} shirt that says, '{printed_text}'.")

make_shirt('m','better late than never')

make_shirt(size='s', printed_text='Suck it, Trebek!')

# 8-4 Large Shirts
def make_shirt(size, printed_text='Ilove Python!'):
    """displays shirt info"""
    print(f"\nYou ordered a size {size.capitalize()} shirt that says, '{printed_text}'.")

make_shirt('m')

make_shirt(size='s', printed_text='Suck it, Trebek!')

# 8-5 Cities
def describe_city(city_name, country_name='the United States'):
    """Displays message"""
    print(f"\n{city_name.title()} is in {country_name.title()}.")

describe_city('Dallas')
describe_city(city_name='Austin')
describe_city(city_name='paris', country_name='france')
