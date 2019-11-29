'''
The FOR loop iterate through a huge list, do some task at a time without having to write the code over.
It is useful when you want to perform a specific task to multiple items. Thereby, saving writing multiple lines of codes.
'''

# Lets say we want to print some list of verbs in a list and the lenght of it's characters.

verbs = ["Read", "Walk", "Sleep", "Code", "Eat", "Restart",]

for ver in verbs:
    print(ver)
    print("The lenght of ", ver, "is:")
    print(len(ver))

# Selected items could also be printed
for ver in verbs[1:3]: #note that first number is inclusive while last exclusive.
    print(ver)