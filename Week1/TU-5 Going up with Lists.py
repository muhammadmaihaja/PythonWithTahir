# Lists in python can be created using square brackets.
# A list in python is synonymous to Arrays in other programming languages.

# Below are the list of scores students obtained in a test

studentScores = [27, 91, 76, 31, 45, 99]

print(studentScores) #print the items in the list studentScores

print(studentScores[2]) #prints item 3 in the list

studentScores[2] = 46 #Substitute item 3 with the new value

studentScores + [11, 2, 84] # Temporary addition of items to a list

studentScores.append(100)# Add an item permanently to the list.

print(studentScores[:4])#display item one to five

studentScores[:4] = [1, 14, 56, 67,23] #substitute items one to five with new list

studentScores[:4] = [] #remove items one to five from the list

studentScores[:] = [] #remove all items from the list