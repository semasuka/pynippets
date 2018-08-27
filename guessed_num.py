"""
small program to guess a number between 1-1000 using the keyboard input, limited to only to 10 guesses

"""

from random import randint
#set the max
highest = 1000
#generating the max
random_num = randint(1,highest)
print(random_num)

guessed_num = 0
guesses = 1
original_guesses = 10
while guessed_num != random_num and guesses <= 10:
    if guessed_num == 0:
        #instruction
        guessed_num = int(input("Game instruction:\n-Please a number between 1 and 1000\n-You only have 10 guesses\n-Enter 0 to quit the game\n\nEnter the number:\n"))
    else:
        #decreasing depending on the number of number of input
        original_guesses -=1
        print("you are left with {} guess(es)".format(original_guesses))
        guessed_num = int(input("Try again:\n"))


    if guessed_num == 0:
        print("quiting the game...")
        break

    if guessed_num < random_num:
        guesses += 1
        print("Please guess higher\n")

    elif guessed_num > random_num:
        guesses += 1
        print("Please guess lower\n")

if guessed_num != 0 and guesses < 10:
    print("Congratulation guessed it after {} guess(es)! the number was {}".format(guesses,random_num))

elif original_guesses == 1:
    print("Sorry but you have exhausted all your guesses")
