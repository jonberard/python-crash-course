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

# insert element into list
car_companies.insert(0, 'Ferarri')
print(car_companies)