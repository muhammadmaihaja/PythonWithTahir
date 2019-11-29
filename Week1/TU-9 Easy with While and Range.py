# A loop can be initiated with range without a list.

# Print number 0 to 99 using range
# Range can be used to loop without a pre-defined list.

for number in range(100): # This can be used to do a task a specified number of times
    print(number)
for number in range(0, 1000, 50):
    print(number)

# While loops iterate as long as a condition is true


word = 0
while word < 5: # This iterates five times incrementing value of word every single time.
    if word == 0:
        print("MY ")
    elif word == 1:
        print("NAME ")
    elif word == 2:
        print("IS")
    elif word == 3:
        print("MUHAMMAD ")
    elif word == 4:
        print("MAIHAJA.")
    word += 1