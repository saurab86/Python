print("Please choose your option from the list below: ")
print('1:\tLearn Python')
print("2:\tLearn Java")
print("3:\tGo Swimming")
print("4:\tHave Dinner")
print("5:\tGot to bed") 
print("0:\texit")

while True:
    choice = input()

    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}.".format(choice))
    else:
        print("Please olny choose your option available from the list below: ")
        print('1:\tLearn Python')
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tHave Dinner")
        print("5:\tGot to bed") 
        print("0:\texit")


  #*** GIVES THE SAME OUTPUT AS ABOVE.
# choice = "-"
# while choice != "0":
#     if choice in "12345":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your option from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tGo swimming")
#         print("4:\tHave dinner")
#         print("5:\tGo to bed")
#         print("0:\tExit")

#     choice = input()
