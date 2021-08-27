day=input("Please enter the day: ")
temperature=int(input("Enter the temperature: "))
raining= True
if (day == "Saturday" or "saturday" and temperature>27) or not raining:  # 'and' has higher precedence than 'or' in python
    print("Go to swimming.")
else:
    print("Learn Python.")
print()

print("*"*80)
print()
print("For boolean expression.")

if 0:           #Python expects a boolean expression after if, which is why it tries to evaluate 0 as boolean values
    print("True")
else:
    print("False")

#Similarly

name = input("Please enter your name: ")
if name:
    #OR
    # if name !="" : We can also code in this form.
    print("Welcome {}.".format(name))
else:
    print("Are yout the man with no name")