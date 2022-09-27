# A variable is a container for a value, which can be of various types

"""
This is a
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
"""

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
"""''
Local Variables
Local variables are those which are initialized inside a function and belongs only to that particular function. It cannot be accessed anywhere outside the function. Let’s see how to create a local variable.
"""
# Example: Creating local variables
def f():
    # local variable
    s = "I love Geeksforgeeks"
    print(s)


# Driver code
f()
