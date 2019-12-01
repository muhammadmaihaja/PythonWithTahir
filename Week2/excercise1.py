# To check a variable type in python
# E.g Let's say you have a variable age

age = 22
print(type(age)) # This prints type int, inferring that 22 is an integer

 # Entering the help() function in python with a value in the bracket invokes the list of things you could do with that.

 # In this script, we'll use 25 different methods of type string

my_name = "maihaja" # We could use the capitalize method to change into a proper way to write a noun.
print("The proper way to write " + my_name + " is " + my_name.capitalize() + ".") # my_name capitalized where necessary

repetitive_text = "Muhammad is name. Also Muhammad is an embodiment of good characters. Same Muhammad is the most used name. Muhammad Everywhere. Muhammad up. Muhammad down. Muhammad right. Muhammad left"
print("Muhammad is mentioned " + str(repetitive_text.count("Muhammad")) + " times in repetitive_text.") #Returns the number Muhammad appears in repititive_text in integer type.

csv_file = "book1.csv"
print("Is book1 a .csv file?\n" + "Answer: " + str(csv_file.endswith(".csv"))) #Returns true if csv_file ends with .csv extension.

alpha_string = " A string is alphabetic if all characters in the string are alphabetic"
print(alpha_string.isalpha()) # This string is not alpha because it contains space characters

alphaNum_string = "iakhjfaius9384717"
print(alphaNum_string.isalnum()) # The characters in alphaNum are Alpha-numeric

decimal_string = "0.2"
print(decimal_string.isdecimal()) #returns true if decimal

digit_string = "789"
print(digit_string.isdigit()) #Evaluates to true

python_identifiers = "AtoZ_aTOz_0to9_and_underscore"
print("python_identifiers are all valid identifiers: " + str(python_identifiers.isidentifier())) #evaluates to true for all

numeric_string = "0123456789"
print("Is a numeric string: " + str(numeric_string.isnumeric())) #all characters are numbers

space_string = " "
print("Is a space string: " + str(space_string.isspace())) # A space character is included

lowercase_string = "ejnamhaiwjefhaiujk"
uppercase_string = lowercase_string.upper() #converts lower case to upper.
print(uppercase_string)

uppercase_string.lower()# Converts upper to lower
print(lowercase_string) #Although lowercase_string is defined is still stands. Thesame output nonetheless

print(repetitive_text.replace("Muhammad", "Umar")) #repititive text is defined above

test_partiton = "manlike.Muhammad "
print(test_partiton.partition(".")) #partitions

print(test_partiton.rfind("like"))

print('A1B2'.zfill(8)) # Adds zeros at the biginning of a string. Coolway to convert to decimal

sentence = "design and implementation of an automatic room controlled water heater."
print(sentence.title()) # All first letters in words are capitalized

subjects = "Mathematics, English, Physics, Biology, Arabic"
print(subjects.split()) # convert comma separated string to list format

vulgar_statement = "Damn you bitch"
print(vulgar_statement.startswith("Damn")) #returns true if it starts with the word "Damn'

print(repetitive_text.swapcase()) # Changes upper to lower case and lower to uppercase in the string

print(sentence.find('automatic', 31, 44)) #finds the word automatic within the indices 31 and 44 and returns it index

car_name = "BUICK"
print(car_name.center(20,"$")) # Positions "BUICK" between 7 and 8 dollar signs

print(lowercase_string.islower()) # Evaluates to true because lowercase_string is in lower case

print(lowercase_string.isupper()) #evaluates to false because lowercase_string is in lowercase

slines = " Muhammad Everywhere.\n Muhammad up.\n Muhammad down. Muhammad right.\n Muhammad left"
print(repetitive_text.splitlines()) # Return a list of the lines in the string, breaking at line boundaries.