numbers = [1,45,31,162,60]
for number in numbers:
    if numbers % 8 ==0:
        print("The numbers are unacceptable")   
        break
else :
    print("All those numbers are acceptable")