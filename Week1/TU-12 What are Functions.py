# Functions are used to break a program into manageable blocks

# A small program to show how functions are called
def whoareyou(name): #This function requires the user to input his name for identification
    print("Welcome ", name)
    print("Your I.D NO. is 84145837")

whoareyou("Muhammad Maihaja")

# Riyal to Naira currency converter

def riyalToNaira(riyalValue):
    Naira = riyalValue * 99.5
    print(riyalValue, " Riyal is equivalent to ", Naira ,"Naira")

riyalToNaira(500)