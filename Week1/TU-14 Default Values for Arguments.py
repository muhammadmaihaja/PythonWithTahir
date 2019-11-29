# Functions can have preset values. That is they can have some initialized values

def get_gender(sex = 'Unknown gender'):
    if sex == "m":
        sex = "Male"
    elif sex == "f":
        sex = "Female"
    print(sex)
get_gender("m")
get_gender('f')
get_gender()