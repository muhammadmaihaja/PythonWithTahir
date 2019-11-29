# In this, multiple values are initialized with arguments

def basicInfo(name = "Muhammad", age = 22, sex = "Male"):
    print(name, age, sex)

basicInfo() # This prints the default values
basicInfo("Umar", 7, "Male") #New values entered
basicInfo(sex="Female", name="Halima",) # Some values entered, but age maintains default value