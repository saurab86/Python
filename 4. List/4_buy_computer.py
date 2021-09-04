available_parts=["computer","monitor","keyboard","mouse","mouse pad","hdmi cable" ]
current_choice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("mouse pad")
        elif current_choice == '6':
            computer_parts.append("hdmi cable")
    else:
        print("Please add options from the list below:")
        for number, part in enumerate (available_parts):    # ENUMERATE IN PYTHON RETURNS PAIRS OF VALUES. THE FIRST VALUE IS THE INDEXED POSITION AND SECOND VALUE IS ITEM   
            print("{0}: {1}".format(number + 1, part))
              
              #OR
        # for part in available_parts:
        #     print("{0}: {1}".format(available_parts.index(part)+1, part))

    current_choice = input()

print(computer_parts)
