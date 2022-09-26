print("Hello World")
print("print('Hello World')")

# STRING MANIPULATION.
# a. string concatenation
print("Hello\n " + "World")
print("Hello " + "World" + "!")

# b.Accessing
word = "Hello World"
letter = word[0]
print(letter)

# c.Length - len()
print(len(word))

# d. Finding - .count()  .find() .index()
print(word.count("l"))
print(word.find("H"))
print(word.index("World"))

# e. Count - .count()
s = "Count, the number of spaces"
print(s.count(" "))

# f.slicing
print(word[0])  # get one char of the word
print(word[0:1])  # get one char of the word (same as above)
print(word[0:3])  # get the first three char
print(word[:3])  # get the first three char
print(word[-3:])  # get the last three char
print(word[3:])  # get all but the three first char
print(word[:-3])  # get all but the three last character
# trial 2
word = "Hello World"
print(word[0:3])  # items start through end-1
print(word[3:])  # items start through the rest of the list
print(word[:-1])  # items from the beginning through end-1
print(word[:])  # a copy of the whole list

# g.Split Strings - .split()
print((word.split(" ")))  # Split on whitespace

# h.Startswith / Endswith - .startswidth() , .endswith()
print(word.startswith("H"))  # shld return a boolean ie True or False
print(word.endswith("w"))  # shld return a boolean ie True or False

# i. Repeats Strings
print(".\n" * 10)  # prints ten dots on their individual lines

# j. Replacing - .replace()
print(word.replace("Hello", "Goodbye"))  # Replaces Hello with Goodbye

# k. Changing Case Strings
string = "Hello World"
print(string.upper())  # HELLO WORLD
print(string.lower())  # hello world
print(string.title())  # Hello World
print(string.capitalize())  # Hello world
print(string.swapcase())  # hELLO wORLD

# l.Reversing  - .reversed()
print(" ".join(reversed(string)))  # d l r o W o l l e H

# m.Strip -  strip(), lstrip(), rstrip()
print(word.strip(""))  # removes from both ends
# print(lstrip()) # removes leading characters (Left-strip)
# print(rstrip()) # removes trailing characters (Right-strip)

# n.Testing - The return type will be in Boolean value (True or False)
print(word.isalnum())  # check if all char are alphanumeric
print(word.isalpha())  # check if all char in the string are alphabetic
print(word.isdigit())  # test if string contains digits
print(word.istitle())  # test if string contains title words
print(word.isupper())  # test if string contains upper case
print(word.islower())  # test if string contains lower case
print(word.isspace())  # test if string contains spaces
print(word.endswith("d"))  # test if string endswith a d
print(word.startswith("H"))  # test if string startswith H
