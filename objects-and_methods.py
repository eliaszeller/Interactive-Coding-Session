this_is_an_integer = 10
this_is_a_string = "Elias"
type(this_is_an_integer)
type(this_is_a_string)

#after creating a variable in python you can check all the things that are contained in the variable using the .dot
# in the vscode. after you press the dot it will reveal a list of thing contained in that object
print(this_is_an_integer.numerator)
print(this_is_an_integer.denominator) # 1
this_is_an_integer.real
# Properties are describing the state of the object we created 
another_integer = 5
print(another_integer.numerator)
print(this_is_a_string.__class__) # no useful methods
# Methods allow us todo stuff with objects we created
#They are like a function, in that they can do things
#but they are specifically attached (bond) to that object

#Some Methods of this is a string
this_is_a_string.upper() # A method requires parenthesis
this_is_a_string.lower() 
print(this_is_a_string) 
this_is_a_string.endswith('!')
this_is_a_string.endswith('as')
this_is_an_integer.real

# A few more methods for strings
# Strings contain alot of methods because there are a lot of things we can do with them
# We've see upper (), lower(), title() capitalizes the first letter of each word
my_sentence = "hello my name is elias"
my_sentence.title()

# We've seen 'endswith ()'
this_is_a_string.endswith('!')
this_is_a_string.endswith('as')

lots_of_space = "                elias.zeller@colorado.edu    "  # Entry in a dataset

cleaned_email = lots_of_space.strip()
is_it_edu = cleaned_email.endswith(".edu")

print(cleaned_email)  # elias.zeller@colorado.edu
print(is_it_edu)      # True

# We can write the same operation more concisely without creating
# a separate variable for the cleaned email.
is_it_edu = lots_of_space.strip().endswith(".edu")
is_it_edu
# Calling multiple methods in one expression is called method chaining.

# Common errors with methods and properties
entry.shout() # AttributesError: n attribute shout()
# You trry to call a method that doesn't not exist on the bject
price = 12 
price.numerator() # TypeError: int object is not callable 
type(price.numerator) # Numerator is a property of the integer 12, storedinto price
# it contains an integer, which is 12
# But an integer does not do anything. It is not a function or a method
# You cannot call it. That's what the "not callable" is stating

# Some more exploration
price.is_integer # This is a method: purple box, and it is an action we are doing
# What will happen if I run this Line?
# We need the parenthesis to call the mothod! otherwise it is not doing anything.
price.is_integer()

# So far we've seen four typesof objects: str, float, int, bool
# In pythn we are going to create other objects
# One object that will solve a problem we had before

from decimal import Decimal # not seen yet
# What is Decimal? It is a factory for manufacting a new kind of object: Decimal object
# To create a float or int, you just needed to type a float or inr
# to create a boolean, you just need to type true or flase, or logical expression

# To create a Decimal object, we are going to use the Decimal thingie we just imported
a = Decimal(".1")
# We have create a new decimal object, with the calue .1
type(a)
b = Decimal(".2")
type(b)
print(.1 + .2) # Floating point error
# This is because, by default, python represents floats with a limited number of zeros
print(a + b) # If you print the sum of two Decimals objects, you get an exact representation

# That is thte problem the decimal is solving
a.  # If you reach into a Decimal object with the dot, you are going to see a lot of new methods and properties


