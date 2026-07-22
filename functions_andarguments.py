functions_andarguments.py
# We've been using functions from Day 1 (or almost)
# print(), type()
len("Elias") # number of elements in a string


# Print () <- What does it take?
# Any expression that we want to print
# What does it do? It prints stuff to the user.

# str() <- what does it take
# it takes any expression 
# What does it do? It turns it into a string adn returns it to a user>

# What does it mean to return something
# Lets take print() as an example
print("1234") # It will print "1234" into the terminal 
my_content = print("1234")
my_content # My content is empty. print("1234") did not store anything in it.

# Some functions (most) return something. Think of them as a conveyor belt
# They are going to taake an object on one side, do things to it, and then RETURN
# the result of what it did on the other side of the machine
# but they are not going to hand you back anything

# Lets write functions to better understand this distinction
# We are going to write a function that takes a price, a rate, and returns the price updated with the rate

# How do we create a new function? We use the following syntax:

def print_total(price, rate):  # def, function name, parentheses, parameters, and a colon
    # Notice that the code inside the function is indented.
    # This indented section is called the function body.
    # Every line in the function body helps define what the function does.
    total = price * (1 + rate)
    print(total)


# We've created our function. Let's test-drive it!
print_total(10, .1)  # Let's run the function.

# Let's say we want to store the result.
my_total = print_total(10, .1)
my_total  # Nothing useful is stored because print_total() only prints the total.
          # It does not return the total, so my_total contains None.


def calculate_total(price, rate):  # Same structure as before
    total = price * (1 + rate)
    return total  # Sends the calculated total back to where the function was called.


my_total = calculate_total(10, .1)
print(my_total) # Success: this function calaculated something
# RETURNED it back to me,  and now I can store it into a variable 
# What happens if you don't store it
calculate_total(10, .1)


# More vocabulary: The imputs of  function ae called arguments
# They come into two flavors
# 1. 'Positional arguments', defned by the order in which you enter them
round(3.14,1) # Rounds the first number to the number of digits in the secont number
round(1,2.14) # Does not work

calculate_total(10, .1)
calculate_total(.1, 10) # POSITIONAL ARGUMENTS ARE EXPECTED ina specific order and given into a certain order

# Some functions take a variable number of arguments
round(3.14) # Here, the second number is not compulsory. It has a default, which is 0
print("ABC", "DEF", "GHI") # Pring "ABC DEF GHI", you can give as many as you want

# Flavor 2# These are arguments that are added by specifying their names
print('A', 'B', 'C', 'D', sep="*")
# Name arguments are not compulorsy, they do not have a default 
print('A', 'B', 'C', 'D', sep="-", end="!")

def add_excitement(text):
    excited_string = text + " !!!!!!!!!!!!"
    return excited_string
    print("The function ran successfully.") # added this after the return
    # anything add after the return will not do anything

python_is_fun = add_excitement("python_is_fun")
python_is_fun

print((19).numerator)
price = 10
print(price.numerator)




