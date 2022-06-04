# CLASSES
# when creating a class you 'instantiate' the class

# Dog Class
class Dog: #capitazlied name refers to class
    """A simple attempt to model a dog"""

    def __init__(self, name, age): # method that python runs automatically whenever we create a new isntance of Dog
        """initialize name and attributes"""
        self.name = name # defines the attributes and sets it to variable name
        self.age = age

    
    def sit(self):
        """simulate a dog sitting in response to commmand"""
        print(f"{self.name} is now sitting.")

    def roll(self):
        """simulate rolling over in response to command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Pearl', 8)
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")


# Accessing attributes
# use dot notation to access attributes
print("\n")

my_dog.sit()
my_dog.roll()

# you can create as many instances of a class as you'd like
your_dog = Dog('Lucy', 4)
print(f"Your dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")


# CHALLENGE 
# 9-1 Restaurant
print("\n")
class Restaurant:

    def __init__(self, name, cuisine, number_served=0):
        self.name = name.title()
        self.cuisine = cuisine
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}.")
        print(f"They serve {self.cuisine} of food.")

    def open_restaurant(self):
        print(f"{self.name} is now OPEN!")

    def increment_number_served(self, number):
        self.number_served += number


# 9-2 Three Restaurants
olive_garden = Restaurant('olive garden', 'italian')
olive_garden.describe_restaurant()
olive_garden.open_restaurant()

chilis = Restaurant('chilis', 'american')
chilis.describe_restaurant()

applebees = Restaurant('applebees', 'american')
applebees.describe_restaurant()

# 9-3 Users
print("\n")

class User:
    """stores a user's profile"""

    def __init__(self, f_name, l_name, login_attempts=0):
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"The user's name is {self.f_name} {self.l_name}.")
    
    def greet_user(self):
        print(f"Hey, {self.f_name}! Welcome to our forum.")

    def increment_login_attempts(self, attempt=1):
        self.login_attempts += attempt

    def reset_login_attempts(self):
        self.login_attempts = 0



bob = User('bob', 'ross')
bob.greet_user()

dave = User('dave', 'thomas')
dave.describe_user()


# Working with Classes and Instances
print("\n")
class Car:
    """Simiple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #sets a default value without passing into parameters

    def get_descriptive_name(self):
        """Return a neatly descriptive formatted name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def update_odometer(self, mileage):
        """Set odometer reading to the given value"""

        # Reject odometer reading if rolling back
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rollback the odometer!")

    def read_odometer(self):
        """Print statement that give odometer reading"""
        print(f"This car has {my_new_car.odometer_reading} miles on it.")

    def increment_odometer(self, miles):
        """add the given amount to the odometer reading"""
        """reject negative number so you can't rollback"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't rollback your mileage!")


    
my_new_car = Car('Ford', 'Bronco', 2022)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# modifying attribute values
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an attribute thorugh a method
# added this method to the class above

    # def update_odometer(self, mileage):
    #     """Set odometer reading to the given value"""
    #     self.odometer_reading = mileage

my_new_car.update_odometer(56)
my_new_car.read_odometer()

my_used_car = Car('Subaru', 'Forester', '2015')

print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_000)
print(my_used_car.odometer_reading)
my_used_car.increment_odometer(200)
print(my_used_car.odometer_reading)
my_used_car.increment_odometer(-200)
print(my_used_car.odometer_reading)

# CHallenge 9-4
print("\n")
restaurant = Restaurant("Chevy's", 'Mexican', 25)
print(restaurant.number_served)
restaurant.increment_number_served(20)
print(restaurant.number_served)

# Challenge 9-5 Login Attempts
user_2 = User('Jon', 'Ber', 1)
print(user_2.login_attempts)
user_2.increment_login_attempts()
print(user_2.login_attempts)
user_2.reset_login_attempts()
print(user_2.login_attempts)

# Overriding Methods from the Parent Class
# define a method in the child class with the same name as the Parent class
# you want to override. Python will disregard the parent class method
# and only pay attention to the method you define in the child class.

# Instances as Attributes
# If your growing list of attributes and methods are becoming lengthy,
# you can write separate classes and uses smaller classes that work together

class Battery:
    """A simple attemtp to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """initialize battery's attributes"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print Statement describing the battery size"""
        print(f"This car has a {self.battery_size}--kwh battery.")  

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range == 315

        print(f"This car can go about {range} miles on a full charge.")    

    def upgrade_battery(self):
        """check battery size and default to 100"""

        if self.battery_size == 75:
            self.battery_size = 100
            print("...Upgrading battery...")
        else:
            print("Your battery is maxed out already.")


#Inheritance
# when one class inherits from another, it takes on the attributes and
# methods of the first class. 
# The original class is called the PARENT CLASS, and the new class
# is called the CHILD class. 

# the __init__() Method for a Child Class
# model an electric car based on car class
print("\n")
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery() # This tells python to create a new instance of Battery

    # Defining Attributes and Methods for Child Class
    # def describe_battery(self):
    #     """Print Statement describing the battery size"""
    #     print(f"This car has a {self.battery_size}--kwh battery.")

my_tesla = ElectricCar('tesla', 'model 3', 2021)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() 
my_tesla.battery.get_range()

# Challenges
# 9-6 Ice Cream Stand
print("\n")
class IceCreamStand(Restaurant):
    """Simiple model of Ice Cream Stand"""

    def __init__(self, name, cuisine='ice cream'):
        """initialize an ice cream stand"""
        super().__init__(name, cuisine)
        self.flavors = []

    def add_flavors(self):
        print("We have the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
            
baskins = IceCreamStand('Baskins')
baskins.flavors = ['chocolate', 'strawberry', 'neopolitan']
baskins.describe_restaurant()
baskins.add_flavors()

# 9-7 Admin
print("\n")
class Admin(User):
    """Admin class with privilege"""

    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        
        self.privileges = Privileges()

# 9-8 Privileges
class Privileges:
    """describe privilieges for admin"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(f"following privileges granted:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no priviliges")


admin_1 = Admin('frank', 'trombone')
admin_1.describe_user()
admin_1.privileges.show_privileges()

print("\nAdding Privileges...")
admin_1.privileges.privileges = [
    'can add post', 
    'can delete post', 
    'can ban user'
    ]

admin_1.privileges.show_privileges()


# 9-9 Battery Upgrade
print("\n")
leaf = ElectricCar('Nissan', 'Leaf', 2015)
leaf.battery.get_range()
leaf.battery.upgrade_battery()
leaf.battery.get_range()




