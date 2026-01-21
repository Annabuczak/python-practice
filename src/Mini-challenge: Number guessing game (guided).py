# Ask user to guess the number
secret = 7
guess = int(input("Guess the number: "))

# Give feedback
print("You guessed:", guess)

if guess > 10:
    print("You are too high")
elif guess < 2:
    print("You are too low")
elif guess < secret:
    print("You are too low")
elif guess == secret:
    print("Good guess, you got it right!")
else:
    print("You win")