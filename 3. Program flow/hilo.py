low = 1
high = 1000

print("Think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while True:
    guess = low + (high-low)//2
    high_low = input("My guess is {} Enter h if your guessig value is higher,"
    " l if your guess value is lower,"
   " or c if my guess was correct: "
    .format(guess)).casefold()

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1

    elif high_low == "c":
        print("I got in {} guss!".format(guesses))
        break
    else:
        print("Please enter h, l or c only")
    guesses+=1
