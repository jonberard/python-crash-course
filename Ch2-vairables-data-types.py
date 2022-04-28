# Variables and Data Types

message = "Hello World!"
print(message)

# You can change the value of the variable anytime and python will keep track
message = "Hello Python Crash Course!"
print(message)
print("\n")

# Variables are basically labels you assign to values

#STRINGS
# Strings are a series of characters inside quotes(single or double)
# Each data type has built in methods 
name = "dirk diggler"
print(name.title())
print(name.upper())
print(name.lower())
print("\n")

#Using variables in Strings
first_name = "chest"
last_name = "rockwell"

# f-strings allow you to replace the name of vairable inside the braces with the value
full_name = f"{first_name} {last_name}"
print(full_name)
print(full_name.title())
print(f"Hello, {full_name.title()}!")

# Can also use f strings in variable assignments 
message = f"Hello, {full_name.title()}!"
print(message)
print("\n")

# Adding Whitespace to Strings with Tabs or Newlines using escapes
print("Python")
print("\tPython")
print("languages: \nPython\nJavascript\nRust")
print("\n")

# Stripping whitespace from Strings
favorite_language = ' python '
# have to assign it to new variable if you want changes permanently
right_stripped_favorite = favorite_language.rstrip()
print(right_stripped_favorite)
left_stripped_favorite = favorite_language.lstrip()
print(left_stripped_favorite)
stripped_favorite = favorite_language.strip()
print(stripped_favorite)

#String Challenges
print("\n")
person = "David Gilmour"
print(f"{person} is the guitar player for Pink Floyd!")

print("\n")
#Name Cases
print(person.title())
print(person.lower())
print(person.upper())

print("\n")
#Famous Quote
print("Robert Frost once said: \nThe woods are lovely, dark and deep,\nBut I have promises to keep,\nAnd miles to go before I sleep,\nAnd miles to go before I sleep.")
print("\n")
famous_poet = "Robert frost"
print(f"{famous_poet} once said: \nThe woods are lovely, dark and deep,\nBut I have promises to keep,\nAnd miles to go before I sleep,\nAnd miles to go before I sleep.")
