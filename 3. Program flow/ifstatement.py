name = input("Please Enter your Name: ")
age = int (input("How old are you, {0}? ".format(name))) #We have to convert the input into integer type from string type
print(age)

if age >= 18 and age < 99:     #In python there's no need of paranthesis for condition statement
    print("You are old enough to vote.")
elif age >= 100:
    print("I think the your time has come.")

else: print("Please come back in {0} years".format(18-age))
