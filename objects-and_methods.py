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