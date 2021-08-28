name=input("Enter your name: ")
age= int(input("enter your age: "))

if  18<=age<31:
    print("Welcome {} for your holiday trip.".format(name))

elif age<18:
    print("Sorry, your are underage.")
else:
    print("Sorry,your age is over aged.")