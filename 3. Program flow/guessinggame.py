answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher.")
    else:   # guess must be greater than answer
        print("Please guess lower.")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it.")
    else:
        print("Sorry, you have not guessed correctly.")
else:
    print("You got it first time.")

# if guess < answer:
#     print("Please guess higher")
#     guess=int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("You have not guessed correctly")                       #THIS CODE IS CORRECT BUT LONG CODE

# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you have guessed it")
#     else:
#         print("Sorry you have not guessed it correctly")

# else:
#     print("You got it first time")