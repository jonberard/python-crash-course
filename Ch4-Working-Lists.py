# Introducing the For Loop
Drummers = ['Neil Peart', 'John Bonham', 'Nick Mason']
for drummer in Drummers:
    print(drummer)
# Simply read, the codeis running: For every drummer in the list of Drummers
# print the drummer's name until there are no more names to print

print('\n')
for drummer in Drummers:
    print(f'Congrats, {drummer.title()}, you\'re in the list of \'Top Drummers of all time\'!')
    print(f'{drummer.title()}, I am looking forward to your next record!\n')

print('Thanks for being the best drummers in the world. You guys are great!') # This is outside the loop and gets executed once

# CHALLENGE 1
# 4-1 PIZZAS
print('\n')
pizzas = ['Pepperoni', 'cheese', 'supreme']
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f'I love {pizza} pizza!')
print('I really love pizza!')
print('\n')

# 4-2 Animals
animals = ['dog', 'cat', 'hamster', 'guinea pig']
for animal in animals:
    print(f'A {animal} would make a great pet!')
print('Save a life and adopt one of these animals!')
print('\n')

# Making Numerical Lists
for value in range(1, 5): # range() does NOT include the defined last input. Prints 1-4
    print(value)

print('\n')
for value in range(6): # can also pass single value and it will print up to the value
    print(value)

# using range to make a LIST of numbers
print('\n')
numbers = list(range(6))
print(numbers)

# using range() to skip numbers by using a 3rd input
numbers = list(range(1, 10, 2))
print(numbers) # will print ODD numbers to list since it starts at one and goes by 2s

print('\n')
numbers = list(range(0, 10, 2)) # will print even numbers into a list
print(numbers)

# using range to put the first 10 square numbers into a list
squares = [] # empy list defined so we can append it
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# more precise sqaure for loop
square = []
for value in range(1, 11):
    square.append(value**2)

print(square)
print('\n')

# simple statistics with list
digits = list(range(0,11))
print(digits)

minimum = min(digits)  # finds minimum number in list
print(minimum)

max(digits) # finds maximum number in list

sum(digits)  #finds the sum of all numbers in list

# LIST COMPREHENSIONS - combines for loop and creation of elemnents in one line of code
squares = [value**2 for value in range(1, 11)]
print(squares)
print('\n')

# CHALLENGE 2
# 4-3 Counting to 20
for value in range(1, 21):
    print(value)
print('\n')

4
# 4-4 One Million
million_numbers = list(range(1, 1_000_001))
# print(million_numbers)

# 4-5 Summing a million
print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))
print('\n')

# 4-6 Odd Numbers
odd_nums = list(range(1, 20, 2))
print(odd_nums)
print('\n')

# 4-7 Threes
threes = [values*3 for values in range(3, 31)]
print(threes)

# 4-8 Cubes
cubes = [values**3 for values in range(1, 11)]
print(cubes)
print('\n')

#SLICING a list
quarterbacks = ['Joe Montana', 'John Elway', 'Jim Kelly']
print(quarterbacks[0:2]) # doesn't print the value of 2. Stops one short.and

quarterbacks.append('Dan Marino')
print(quarterbacks[:]) # omiitting the indexes prints entire list. You can omit either or both. 
print(quarterbacks[:4])
print(quarterbacks[-2:]) # can use negative index to recall from end of list
print(quarterbacks[0:3:2]) # 3rd value tells slice how many values to skip
print('\n')

# LOOPING THROUGH SLICE
print('Here are the best NFL quarterbacks of all the 80s/90s:')
for quarterback in quarterbacks[:]:
    print(f'\t{quarterback.title()}')
print('\n')

print('Here are my top 2 quarterbacks of all time:')
for quarterback in quarterbacks[:2]:
    print(f'\t{quarterback.title()}')

# Copying a list
my_favorite_fish = ['Halibut', 'Snook', 'Trout', 'Salmon']
healthy_fish = my_favorite_fish[:]
print(my_favorite_fish)
print(healthy_fish)

# copying a list into new list creates two separate lists to be modified
my_favorite_fish.append('Hogfish')
healthy_fish.append('Talapia')
print(my_favorite_fish)
print(healthy_fish)

# if you don't copy using the slice, it will NOT create two separate list
not_farmed_fish = my_favorite_fish
my_favorite_fish.append('Cobia') # Will add this to both lists since one points to the other
not_farmed_fish.append('Redfish')
print(my_favorite_fish)
print(not_farmed_fish)
print('\n')

# Challenge 3
# 4-10
print('The first 3 quarterbacks in the list are:')
for player in quarterbacks[:3]:
    print(f'\t{player}')

print('The qaurterbacks from the middle of the list are:')
for player in quarterbacks[1:4]:
    print(f'\t{player}')

print('The last 3 quarterbacks in the list are:')
for player in quarterbacks[-1:-4]:
    print(f'\t{player}')
print(quarterbacks)