# Variables declared in functions are function specific

varA = "global variable"

def func1():
    varB = "function specific"
    print(varA)
    print(varB)

def func2():
    print(varA)
    print(varB) # This doesn't prints because the variable is not accessible by the function.

func1()

func2()