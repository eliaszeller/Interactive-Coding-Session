print("Hello World")
print(2+2)
# Here, nonthing gets exicued when I press enter
# How can I run this code
# Two ways
# 1. Put the carret on the line and press shift + eneter (Send the line tp the REPL and run it)
# 2. Run the File (Send the entire content of the file to Python , all the lines will be executed in sequence) Press the play button (after writing script)

# Reminder 1: We can create variables in python 
my_name = "Elais Zeller"
print(my_name) # This is printing the contents of the variable

# Running the code all at once will open a new terminal to start from scratch with out any other previous inputs

# Four big types of data in Python 
this_is_an_integer = 10
this_is_a_float = 3.14
this_is_a_string = "Hello World"
this_is_a_boolean = True

# Print using the Pring function
print(this_is_an_integer)
print(this_is_a_float)
print(this_is_a_string)
print(this_is_a_boolean)

# Print () is something called a function (taked between 0 and many arguments and that has a specific behavior, It is an action)

print(this_is_a_boolean, this_is_a_float)

# This is a value
print(3.14)
print("Hello World")
# This is a variable
print(my_name)
# An expression
print(2+2)

print(this_is_an_integer)
print(this_is_an_integer + 5)
# 1. Read the value contained inside the variable "this is an Integer"
# 2. Do the operation, here, a sum,  between
# 3. Print the result of that operation

#How do you figure out the type ofvariable
what_is_this = type(this_is_an_integer)
print(what_is_this)
what_is_that = type(3.12)
print(what_is_that)

# Calculations !
print(2+3)
print(2+3*5)
print((2+3)*5) #PEMDAS
 
print(2+3)
print((1+2) ==3) #"==" is equal
# logical comparisons always return Boolean: True or False

print(0.1+0.2)
print((.01+0.2) ==0.3) # Floats may not always be exact 

# can you do
my_rounded_addition = round((0.1+0.2), 1)
print(my_rounded_addition)
round(3.14)

# Logical expressions
print(3 == 5)
print(3 != 5)
print(3 > 5)
print(3 < 5)
print(3 <= 5)
print(3 >= 5)

#Using and Or
condition_1 =True
condition_2 =True
condition_3 =False
condition_1 =True

print(condition_1)
print(condition_1 and condition_2) # AND only returns true when all conditions are True
print(condition_1 or condition_2) # OR returns True when one condition is true

print(True + True)
print(True + False)
print(True == 1)
print(False == 0)
print(True * 5)

# String manipulation  Calculations pluss strings
Greeting = "Hello " + "World"
print(Greeting)

laugh = "ha" *3
print(laugh)

weird_laugh = "ha" * 3.12 # Doesn't work
print(weird_laugh) 


number = 42
is_this_a_number = "42"
print(number +10)
print(this_is_a_number + 10) #Doesn't work
#create a ne vairable
now_this_is_a_number = int(is_this_a_number)
print(now_this_is_a_number)
int("15")
int("fifteen") # Doesn't work


# One more example
my_age = 24
print(my_age)
my_into = "Hello, my name Elias and I am" + my_age
print(my_into)
