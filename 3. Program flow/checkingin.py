     #'IN'  CONDITION 
parrot =   "Norgewian Blue"
letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("{} is not in {}".format(letter, parrot))

   
    #'NOT' IN CONDITION
activity=input(("What would like to do today? "))

if "cinema" not in activity.casefold():                     #.casefold convert upper case to lower case as well as read other special character
    print("But i want to got to cinema today.".upper())     #.upper() convert lower case to upper case.
else:
    print("Lets's learn python today.")