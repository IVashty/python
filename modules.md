# MODULES:
A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the moduleâ€™s name (as a string) is available as the value of the global variable `__name__`
~for example,

`# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
`
