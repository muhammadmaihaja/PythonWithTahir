# Break in python stops the execution of the loop and goes to the next line of code if any

# Program to check an unknown number within the range 0 to 99

unknownNumber = 56

for x in range(100):
    if x is unknownNumber:
        print(x, " is the Unknown Number")
        break
    else:
        print(x)

# Continue skips the current iteration

numbersTaken = [2, 5, 11, 18,]

for x in range(20):
    if x in numbersTaken:
        continue
    else:
        print(x)
    