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

# DEFAULT Values - python uses default arg value if one is provided
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

# RETURN VALUES
# funcs don't have to always display output directly. 
# they can process data and then return set of values back to whatever called func 
# print("\n")
# def get_formatted_name(first_name, last_name):
#     """Return full name formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('david', 'gilmour')
# print(musician)

# middle name default - may not always have middle name
print('\n')
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return full name formatted"""
    if middle_name: # python interprets non-empty strings as True.
        # so middle_name evaluates to True is a middle name argument is in the function call
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()

musician = get_formatted_name('John', 'hooker', 'lee')
print(musician)
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
    
# Returning a Dictionary
# funcs can return any kind of data value you need
# def build_person(first_name, last_name):
#     """Return a dictionary of information about person"""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('David', 'Gilmour')
# print(musician)

# extend func to add age
print('\n')
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about person"""
    person = {'first': first_name, 'last': last_name}
    if age: # runs if age is True (or has a number in it). None evaluates to False (left empty)
        person['age'] = age
    return person

musician = build_person('Jimi', 'Hendrix', age=27)
print(musician)

# using a func with while loop
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' to quit at any time)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# CHALLENGE 3
# 8-6 City Names
print('\n')
def city_country(city, country):
    answer = f"{city}, {country}"
    print(answer.title())

city_country('austin', 'united states')

# 8-7 Album
print('\n')
def make_album(artist, title, song_number=None):
    """Returns a dictionary with info"""
    albums = {
        'artist': artist.title(), 
        'album_title': title.title(),
        'number_of_songs': song_number
        }
    return albums

pink_floyd = make_album('Pink Floyd', 'Meddle', song_number=5)
print(pink_floyd)

def_leopard = make_album('Def Leopard', 'hysteria')
print(def_leopard)

# 8-8 User Albums
def make_album(artist, title):
    """Returns a dictionary with info"""
    albums = {
        'artist': artist.title(), 
        'album_title': title.title(),
        }
    return albums

while True:
    print("\nEnter artist and album name.")
    print("(Enter 'q' to quit at anytime.")

    artist = input("What is the artist name: ")
    if artist== 'q':
        break

    album = input("What is the album name: ")
    if album == 'q':
        break

    music_dict = make_album(artist, album)
    print(music_dict)

# passing a LIST to a func
def greet_users(names):
    """Print simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['jon', 'brooke', 'bash']
greet_users(usernames)

# modifying a LIST in a FUNC
# start with some designs that need to be printed.
print("\n")
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# simulate printing each design until none are left

while unprinted_designs:
    completed = unprinted_designs.pop()
    print(f"Printing {completed}.")
    completed_models.append(completed)

# Display all completed models
print("\nThe following models have been completed:")
for model in completed_models:
    print(model)

# reorganizing the above with 2 functions
print("\n")
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to compoleted models after printing."""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot armor', 'battle bot']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List
# you can send a copy of a list to a func like:
# function_name(list_name[:])

# slice notation makes a copy of the list to send tothe function.

#CHALLENGE 4
# 8-9 Messages
print("\n")
short_texts = ['brb', 'lol', 'wtf', 'cya']

def show_messages(messages):
    for message in messages:
        print(f"{message}")

show_messages(short_texts)

# 8-10 Sending Messages
print("\n")
short_texts = ['brb', 'lol', 'wtf', 'cya']
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(f"{message}")

def send_messages(messages, new_list):
    while messages:
        for message in messages:
            moved_message = messages.pop()
            print(f"....moving {moved_message}...")

            new_list.append(moved_message)


# send_messages(short_texts, sent_messages)
# print(sent_messages)
# print(short_texts)

# 8-11 Archived Messages
print("\n")
send_messages(short_texts[:], sent_messages) # sending a copy doesn't affect the original list. See print
print(short_texts)
print(sent_messages)

# Passing an arbitrary Number of Arguments
# The * in parameter name tells Python to make an empty tuple called toppings.
# the arbitrary argument must come last if passing different kinds
print("\n")
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""
    print(f"\nMaking a {size.capitalize()} pizza with the following toppings:")

    for topping in toppings:
        print(f" - {topping}")

make_pizza('m', 'pepperoni')
make_pizza('l', 'cheese', 'pineapple', 'ham')

# Using arbitrary keyword Arguments
print("\n")

def build_profile(first, last, **user_info): # the ** cases Python to create an empty dictionary
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('jon', 'breen', location='Austin', job='aviation')
print(user_profile)

# Challenge
print("\n")

# 8-12 Sandwiches
def make_sandwich(*toppings):
    print('You ordered a sandiwch with:')
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('ham', 'cheese', 'mustard')

# 8-13 User Profile
print("\n")

the_midnight = build_profile('The', 'Midnight', genre='Synthwave', type='group', vocals=True)
print(the_midnight)

# 8-14 Cars
print("\n")

def build_car(manufacturer, model, **build_info):
    build_info['manufacturer'] = manufacturer
    build_info['model'] = model
    return build_info

car = build_car('ford', 'bronco', doors=2, engine=2.3, color='green')

print(car)

# Storing your functions in modules
# stores functions in separate files and allows you to 
# hide the program's code and focus on higher level logic
# just have to 'import' the file and then call function. 

# EX: import pizza - pizza is the name of the pizza.py file that houses the build_pizza func

# Can also import sepcific functions
# EX: 'from module_name import function_name

# Using 'as' to Give a Function an Alias
# EX: 'from pizza import make pizza as mp
# then you just call func by alias - EX: mp('pepperoni', 'cheese', 'sauce) 