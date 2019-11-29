# Function that can take any amount of arguments

def multiplyNumbers(*args):
    product = 1
    for operand in args:
        product *= operand
    print(product)

multiplyNumbers(2, 2, 2)