age = 22
print("My age is " + str(age))  #My age is 22. str replace int type to string

#Print("My age  is " + age ) will give an error because in python string and integer cannot be concatinated

print("I am {0} years old.".format(age)) #{0} is the replacement feild

print("There are {0} days in {1}, {2}, {3}, {4}"
     .format(31,"Jan","March","Sep", "Oct."))   #{0},{1},{2},{3},{4} are replacement feilds

print("Give me {2} dollar {0} cents {1}".format(50,"okay!",100))  #replacement feilds are indexed sequentially ie. {2} bounds to 100
     #{0} bounds to 50 and {1} bounds to okay
print()
name = "Red"
age = 24 
print(f"Name: {name} and Age: {age}")    #Here we need not use .format string replacement. We only use 'f' before double quotation.
       #And string variable and integer variable needs to place {variable name or operation betn double quotation}