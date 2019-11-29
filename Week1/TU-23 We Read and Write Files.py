# Creating, Reading and Writing to files

fw = open('myBiography.txt', 'w') #opens file
fw.write("Assalamu alaikum wa rahmatullah\n  My name is Muhammad Maihaja.\n   I am a Muslim\n") #writes to the file
fw.write("    I am a student at ABU, Zaria.\n     I Hope to go to Hajj this year insha'a Allah.\nMassalaama")
fw.close() #close file

fr = open('myBiography.txt', 'r')
MuhammadsBio = fr.read() #reads file and save in LH variable
fr.close()

print(MuhammadsBio)