# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
# representes by
# def _____():

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
# example 1

string = "GeeksforGeeks"
# lambda returns a function object
print(lambda string: string)

# example 2:
# Python program to demonstrate
# lambda functions
x = "GeeksforGeeks"

# lambda gets pass to print
(lambda x: print(x))(x)
# example 3:
# Python program to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y * y * y


g = lambda x: x * x * x
print(g(7))

print(cube(5))
