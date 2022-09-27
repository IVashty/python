# A List is a collection which is ordered and changeable.
# Allows duplicate members
# Python program to demonstrate
# Creation of List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Creating a List with
# the use of a String
List = ["GeeksForGeeks"]
print("\nList with the use of String: ")
print(List)

# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [["Geeks", "For"], ["Geeks"]]
print("\nMulti-Dimensional List: ")
print(List)

"""""
List Methods:

Here are some other common list methods.
    list.append(elem) -- adds a single element to the end of the list. Common
                error: does not return the new list, just modifies the original
    list.insert(index, elem) -- inserts the element at the given index,
        shifting elements to the right.
    list.extend(list2) adds the elements in list2 to the end of the list.
    Using + or += on a list is similar to using extend().
    list.index(elem) -- searches for the given element from the start of the
                list and returns its index. Throws a ValueError if the element
                does not appear (use "in" to check without a ValueError).
    list.remove(elem) -- searches for the first instance of the given element
        and removes it (throws ValueError if not present)
    list.sort() -- sorts the list in place (does not return it). (The sorted()
                function shown later is preferred.)
    list.reverse() -- reverses the list in place (does not return it)
    list.pop(index) -- removes and returns the element at the given index.
    Returns the rightmost element if index is omitted :
        (roughly the opposite of append()).
"""

# Examples of methods put tot practice

list = ["larry", "curly", "moe"]
print(list)
list.append("shemp") ## append elem at end
print(list )
list.insert(0, "xxx")  ## insert elem at index 
print(list)
list.extend(["yyy", "zzz"])  ## add list of elems at end
print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index("curly"))  ## 2

list.remove("curly")  ## search and remove that element
list.pop(1)  ## removes and returns 'larry'
print(list)  # ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
list = [1, 2, 3]
print(list.append(4))  ## NO, does not work, append() returns None
# Correct pattern:
list.append(4)
print(list)  ## [1, 2, 3, 4]
list = []  ## Start as the empty list
list.append("a")  ## Use append() to add elements
list.append("b")
