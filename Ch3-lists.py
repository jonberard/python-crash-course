#LISTS 
# lists allow you to store sets of information in one place no matter the quantity
music_formats = ['record', '8-track', 'cd', 'digital']
print(music_formats)   

# accessing the elements in a list
# lists are ordered, zero-indexed which means the first element is 0 
print(f'Cruising in my caddy listening to the BeeGees on my {music_formats[1]} player!')

# can also use string methods on lists
print(music_formats[2].title())

# can always access the last element in a list with -1
print(music_formats[-1])
print(music_formats[-2])

#Use individual values from list
print(f'Cruising in my caddy listening to the BeeGees on my {music_formats[1].upper()} player!')

# Changing, Adding, Removing Elements
car_companies = ['Ford', 'Chevorlet', 'Honda', 'Kia']
print(car_companies)
print(car_companies[0])

car_companies[0] = 'Hyundai'
print(car_companies[0])
print(car_companies)

# add element to the list
car_companies.append('Ford') # Will add Ford to the end of the list.
print(car_companies)

# insert element into list - requires position and element
car_companies.insert(0, 'Ferarri')
print(car_companies)

# removing an element from list
# if you know the position to delete use del
del car_companies[0]
print(car_companies)

# you can remove an elemnt to work with by using pop()
popped_car_company = car_companies.pop()
print(car_companies)
print(popped_car_company)

#you can pop any element in list by adding position in parentheses
first_car = car_companies.pop(1)
print(f'My first car was a {first_car.title()}.')

# if you do NOT know the position of the element to remove but you do know the value, use the remove method.
# it is similar to delete except you remove by value and not position. 
print(car_companies)
car_companies.remove('Honda')
print(car_companies)

car_companies = ['Hyundai', 'Ford', 'Chevorlet', 'Chrysler', 'Dodge', 'Subaru', 'Ferarri']
too_expensive_car = 'Ferarri'
car_companies.remove(too_expensive_car)
print(car_companies)

# Challenge Section 1
# 3-4
print('\n')
jam_list = ['David Gilmour', 'Roger Waters', 'Jimmy Page', 'Jimmy Hendrix', 'Mark Knopfler', 'Jeff Beck']
print(f'I\'d love to jam with {jam_list[0].title()} one day.')
print(f'I\'d love to jam with {jam_list[1].title()} one day.')
print(f'I\'d love to jam with {jam_list[2].title()} one day.')
print(f'I\'d love to jam with {jam_list[3].title()} one day.')
print(f'I\'d love to jam with {jam_list[4].title()} one day.')
print(f'I\'d love to jam with {jam_list[5].title()} one day.')

# 3-5 - remove and replace guest
print(f'It turns out {jam_list[3]} can\'t make it tonight after all.')
dead_guitarist = jam_list.pop(3)
jam_list.append('The Edge')
print(f'Since {dead_guitarist.title()} can\'t make it, I took it upon myself to invite {jam_list[-1].title()} instead! Cheers!')

# 3-6 More Guests!
print('Holy shit we found a bigger stage! Let\'s invite more people.')
jam_list.insert(0, 'Andy Timmons')
jam_list.insert(4, 'John Mayer')
jam_list.append('Kieth Richards')
print(f'I\'d love to jam with {jam_list[0].title()} one day.')
print(f'I\'d love to jam with {jam_list[1].title()} one day.')
print(f'I\'d love to jam with {jam_list[2].title()} one day.')
print(f'I\'d love to jam with {jam_list[3].title()} one day.')
print(f'I\'d love to jam with {jam_list[4].title()} one day.')
print(f'I\'d love to jam with {jam_list[5].title()} one day.')
print(f'I\'d love to jam with {jam_list[6].title()} one day.')
print(f'I\'d love to jam with {jam_list[7].title()} one day.')
print(f'I\'d love to jam with {jam_list[8].title()} one day.')

# 3-7 Shrinking List
print('Well, the excitement has died off. We got kicked to the community center. Only room for 3!')
print(f'I\'m sorry, {jam_list.pop(6)}. I gotta let ya go. It\'s just not gonna happen tonight.')
print(f'I\'m sorry, {jam_list.pop(0)}. I gotta let ya go. It\'s just not gonna happen tonight.')
print(f'I\'m sorry, {jam_list.pop(1)}. I gotta let ya go. {jam_list[0]} is the better guitarist anyways.')
print(f'I\'m sorry, {jam_list.pop(3)}. I gotta let ya go. It\'s just not gonna happen tonight.')
print(f'I\'m sorry, {jam_list.pop(1)}. I gotta let ya go. It\'s just not gonna happen tonight.')
print(f'I\'m sorry, {jam_list.pop(3)}. I gotta let ya go. It\'s just not gonna happen tonight.')
print('\n')
print(f'Hey, {jam_list[0]}, {jam_list[1]}, {jam_list[2]}, great news! You guys are still invited.')

# empty jam
del jam_list[-1]
del jam_list[-1]
del jam_list[-1]
print(jam_list)

# Organizing a List
car_companies.sort() # permanently alphabetizes the list
print(car_companies)

car_companies.sort(reverse=True) # this alphabetically reverses the list permantly by passing this argument.
print(car_companies)

# temporarily sorting a list using sorted()
motorcycle_brands = ['ducati', 'yamaha', 'honda']
print(motorcycle_brands)
print(sorted(motorcycle_brands)) # temporarily sorts the list but then reverts back to roiginal on next call
print(motorcycle_brands)

# reversing the order of a list
car_companies.sort()
print(car_companies)

car_companies.reverse() # reverses the list permanently
print(car_companies)

#Finding the LENGTH of a list with len()
print(len(car_companies))

#LIST CHALLENGE 2
# 3-8
places_to_vist = ['Maldives', 'Minorca', 'Pacific Islands', 'Australia', 'New Zealand']
print(places_to_vist)
print(sorted(places_to_vist))
print(places_to_vist)
print(sorted(places_to_vist, reverse=True)) # This reverse the order and is NOT permanent
print(places_to_vist)

print('\n')
places_to_vist.reverse()
print(places_to_vist)

print('\n')
places_to_vist.reverse()
print(places_to_vist)

print('\n')
places_to_vist.sort()
print(places_to_vist)

print('\n')
places_to_vist.sort(reverse=True)
print(places_to_vist)

# 3-9 Guitar Guests
print('\n')
print(f"I am inviting {len(jam_list)} guitar players to play onstage with me tonight.")

# 3-10 Every Funciton
print('\n')
instruments = ['Drums', 'Guitar', 'Bass', 'Piano', 'Vocals']
print(instruments)
instruments.append('Whistle')
print(instruments)
not_an_instrument = instruments.pop()
print(f'C\'mon, everyone knows the {not_an_instrument} is not an instrument!')
instruments.insert(1, 'Percussion')
print(instruments)
instruments.remove('Percussion')
print(instruments)
print(sorted(instruments))
print(sorted(instruments, reverse=True))
print(instruments)
instruments.sort()
print(instruments)
instruments.sort(reverse=True)
print(instruments)

