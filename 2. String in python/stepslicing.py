variable = "Norwegian Blue"

print(variable[0:6:2])  #Prints 'Nre'
print(variable[0:6:3])  #Prints 'Nw'

number="9,223,454,274,554,877,664,"
print(number[1::4])    #Prints all commas..

#Backward step Slicing 
letters ="abcdefghijklmnopqrstuvwxyz"
backwards =  letters[25:0:-1]   #gives backward value from z to b but not a
print(backwards)
print()
print(letters[25::-1])         #gives backwards value from z to a.

print(letters[16:13:-1])      #print 'qpo' from backwords.
print(letters[25:-9:-1])      #prints last eight characters 
 #Or Print(letters[:-9:-1])   is the same operation