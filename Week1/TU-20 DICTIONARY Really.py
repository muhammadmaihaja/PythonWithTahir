# Dictionary in python is a holder for key and values.

infiniIdeas_staff_tasks = {'Manager' : 'Oversees general affairs of company', 'COO' : 'Makes sure organizational affairs move smoothly', 'CFO' : 'Sources money and attract investors', 'Marketing manager' : ' Handles all aspects related to promoting and selling the product' }

print(infiniIdeas_staff_tasks)
print(infiniIdeas_staff_tasks['COO'])


for k,v in infiniIdeas_staff_tasks.items(): # Iterates through the dictionary and prints the keywords with respective values.
    print("The " + k + " does the following task: " + v + ".")