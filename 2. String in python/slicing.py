#Slicing of Strings
variable = "Game of Thrones"

print(variable[0:3])  #Print the 'Gam'. including string from index 0 and don't include the index 3.4
print()
print(variable[5:7])  #Print only 'of'.
print(variable[:5])   #Print 'Game'
print(variable[8:])   #Prints 'Thrones 

#Negative slicing
print(variable[-7:-2])  #O/P 'Thron'