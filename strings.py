# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
from unicodedata import name

name='Vashti'
age=24

#concatenate
print('hello my name is '+ name +' and I am '+ str(age))

# String Formatting
   #position argument
print('My name is {name} and I am {age} '.format(name=name , age=age))
   #F-Strings
print(f'Hello, my name is {name} and I am {age}.')


# String Methods
   #capitalise
s='hello python'
print(s.capitalize())
   #
