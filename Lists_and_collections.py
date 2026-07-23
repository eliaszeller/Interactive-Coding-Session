# Talk about collections, collections are object that are designed to hold other objects in them
# They are like bags of different kinds

# Lists

# A list s a ordered collection of items
# It is creat by using square brackets 

my_empty_list = [] # This is a list that does not contain anything
type(my_empty_list)# This is a list
# What do lists do - they contain other objects
my_favorite_numbers = [1,2,3,4,5]
print(my_favorite_numbers)

# Lists can contain other elements
my_favorite_colors = ["Red", "Blue", "Green"]
print(my_favorite_colors)
my_favorite_decimals = [3.14, 2.234, 4.34]
my_favorite_bool = [False, True, False]

# Lists can contain different elements of different kinds
my_favorite_thins = ["red", 3.14, False]

# You can put anything into a list, even other lists
my_mix_list = [False, ["blue", 19], ["red", False], 3.14]
print(my_mix_list)
# Do not be suprised: Lists are very flexible. You can just put a lot of things in them

# Lists are objects meaning...
#  They contain properties and methods

# Lets see some methods of lists
my_favorite_colors.append("Yellow") # This did not print anything
print(my_favorite_colors) # It contains yellow! A new item ws added to it

# THis is different that other metheds that we have covered 
# It changes the object where the other methods dont

my_string = "Elias" # I run this, it prints a string in upper case
my_string.upper   # The original string is still in lowcase '
# The methode COPIES the original object, change it, and returns the copy. The original is NEVER changed

# This is because strings are "immutable", once create they will not change


my_favorite_colors
a = my_favorite_colors.append("Pink")
print(my_favorite_colors)
# The method mutated the original list. The content was CHANGED directly by the method
# But then what is inside 'a'? What did the method return?
print(a) # When you are working with a metod that mutates the original
# It will typically not return the original. It will simply do something on the original and return "None"

my_favorite_colors.copy() # Creates a new copy of a given list


# Other methods with lists
print(my_favorite_colors) # ['Red', 'Blue', 'Green', 'yellow', 'Yellow', 'Pink']
# What if you want to remove an element of the list
# You can use a methode called 'pop'. Pop will remove the last element of a list
# and returns it to you
removed_color = my_favorite_colors.pop()
print(my_favorite_colors)
print(removed_color)
# If you run the same comand multiple times the behavior will change
# The list is being mutated so you will not get the same results 

# What happends if you do not assign the popped color
my_favorite_colors.pop() # List now contains Red, Blue, Green, Yellow

# If a function or method returns something and we do not "catch" it into a variable, it "falls" into the variable

# Lists are orded, meaning you can reach into them at a specific position and grab the contents

my_favorite_names = ["Elias", "Sam", "Joe"]
# Lets say I want to read what is at the begining of that list
# You can use an operation called INDEXING
# You put square brackets after the list, and use the INDEX of the element that you want to grab
print(my_favorite_names[0]) # Elias
print(my_favorite_names[1]) # Sam
print(my_favorite_names[2]) # Joe

# What happens if you index [3]
print(my_favorite_names[3]) # Returns and Index Error


# Continued discussion of INDEXING
# INDEXING: we can use NEGATIVE indices
print(my_favorite_names[-1]) # -1 Reades the last value Joe
print(my_favorite_names[-2]) # -2 Reades the second to last value Sam

# We can also do something called SLICING to grab multiple values froma list
my_favorite_numbers = [1,2,3,4,5,6,7,8,9,10]
#Indexing first
my_favorite_numbers [2]
# Slicing now
my_favorite_numbers[0:3:1] # This means the values between the first and the fourth (excluded) and all of them
# More Exmaples
my_favorite_numbers[1:6:1] # All values between the second and the sevent (excluded) all of them
my_favorite_numbers[3:8:1] # All values between the fourth and eight (or ninth excluded)
my_favorite_numbers[0:6:2]

# When you are slicing you can omit some arguments
my_favorite_numbers[0:3] # By default, the step is one (if omitted)
# this is equivalent to [0:3;1]
my_favorite_numbers[1:] # All of them starting from one
# Both end is omitted (so it defaults to until the end) and step is ommited (so it defaults to 1)
my_favorite_numbers[:4] # Stat is omitted (so it defaults to 0, beginning)
# Stops is 4 (meaning until 4th element, excluded), step is omitted so 1
my_favorite_numbers[::2] # Start is omitted (so 0) stop is omitted (so until) 
# the end, and step is 2: Every other value in the entire list

# Practice slicing
my_favorite_numbers[::-1]

# Something Cool
my_name = "Elias Zeller"
my_name_but_mirrored = my_name[::-1]
my_name_but_mirrored
# A string is an orded collection of characters so you can sice it like a list
my_name[0:4] # You can slice srtings too

# So far were have learned
# Lists are MUTIBLE: We can Modify
# Lists are ITERABLE: We can select a subset

# Lets put these things together 
my_favorite_names # ['Elias', 'Sam', 'Joe']
# I want to replce Elias with Adam: How do we do it?
my_favorite_names[0] = "Adam" # We are indexing the first e;ement of the list and assigning the word "Adam" at the position
my_favorite_names # We have mutated the list

# We can do the same thing with slices
my_favorite_names[1:] # This is slicing ['Sam, 'Joe]
my_favorite_names[1:] = ['Eve', 'Joshua']
my_favorite_names # We can use slicing and indexing to read or update the contents of a list

#Can we use indexing or slicing to upate the content of a sttring
my_name = [0] = "Z" # Strings are not mutable # This does not work
# If you want a new string you need to create a new string

# A few list methods
my_favorite_names.pop()
my_favorite_names.append('Joshue')
# Pop and append can take an additional argument: The position!
my_favorite_names.pop(0) # This will pop the first element
my_favorite_names.insert(0, 'Adam')
my_favorite_names
# all these methods are odifying the original list. Not returning a copy of the list
# One more
my_favorite_names.reverse() # This will return nothing # It returns nothing it is change=ing the order of the original list
my_favorite_names


# Lists are collections of ordered items
# Dictionaries are collections of key:value pairs

# Example
my_friends_age  = {"Nick": 40, "Sam": 35, "Juan": 37}
# Not the syntax
#Dictionaries can have diferent kinds of values
my_information = {"name": "Elias" , "age": 24, "Hobbies": ["Fishing", "snowboarding", "Hiking"]}
# Here we have the key "name" that contians an string vlaue
# Key "age" that contians an int vlaue
# Key "Hobbies" contains a list value

# Keys have to be unique and they have to be Immutable 

# How do we use dictionaries ]# We can reach into them to see the values
# THis is called Indexing. For a list, it is ordered, so we can index with numbers>
# What do we index with when you have a dictionary

my_friends_age["Nick"] # How do we get Knicks age
# I use square brackets to index, and give the key from which  want to see the value

my_information["Hobbies"] # 

# Dictionaries like like lists, are mutable. we can update them
# Lets say my friends Nick just celibrated is birthday
# How do I update his age, You reach into the dict at the desired key and you assigne a new value to it
my_friends_age["Nick"] = 41
my_friends_age

#Can we change my name to Elias to "Elias Zeller"
my_information["name"] = "Elias Zeller"
my_information
my_information.pop("Name") # Removed the "Name" key
my_information['Job Title'] = "Unemployed"
my_information
# We can use indexing to
# 1) Read the values of an existing key
# 2) Update the value of an existing key
# 3) Create a key with a given value

# Since dictionaries are OBJECTS... they have METHODS
# First useful method: get()
my_information['address']
# If you accidentally check for a value that does not exist, you will get a KeyError
# Errors aren't great when writing code , becuase they will stop the code
# A better way is to check if a key exists is to use th emethod get()
my_information.get("address")
Elias_adress = my_information.get("address") 
print(Elias_adress) # This will print "None". get.() returns none when the key is not found

# Three other useful methods, rather than blindly checking
my_information.keys() # Check all the Keys
my_information.values() # Check all the Values 
# you know all the values and keys but don not know haw they correspond
my_information.items()

# Two more things about Dictionaries
# 1) The Keys of a dit must be int or str
# The Values can be anything. so far we've see
# str values
# int Values
# List Values

# What is very common
my_friends_info = {
    'Nick': {
        'age': 41,
        'city': 'Boulder',
        'hobbies': ['skiing', 'cooking']
    },
    'Sam': {
        'age': 37,
        'city': 'Denver',
        'hobbies': ['coffee', 'cooking'],
        'job': 'professor'
    }
}

my_friends_info["Nick"]
my_friends_info["Nick"]["age"]
my_friends_info["Nick"]['hobbies']
my_friends_info["Nick"]['hobbies'].append('Birdwatching')
my_friends_info.items()




