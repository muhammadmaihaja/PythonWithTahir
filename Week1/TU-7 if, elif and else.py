# The if statement executes once if the condition evaluates to true

# A program that knows the range which a value exists

number = 3

if number <= 500:
    print("Number is from 0 to 500")# prints this if the above condition is satisfied
elif number <= 1000:
    print("Number is from 501 and above") #evaluates this if the first statement fails
else:
    print("The number is invalid")# This is the final, executes when all conditions don't match

#Program that tells the behaviour of a person based on their names.

name = "mommy"
if name == "Muhammad":
    print("He's a gentle guy")
elif name == "Halima":
    print("She's a stubborn girl")
elif name == "Mommy":
    print("She's unapologetic")
else:
    print("No valid name entered")