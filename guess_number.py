import random
##computer is generating the number and you are guessing it, so yeah done
def guess_number(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {x} : '))
        if guess < random_number:
            print("Sorry try again ! too low ")
        elif guess > random_number :
            print('sorry try again!too high')
    
    print(f"Yay !you guessed the right answer {random_number}")
x = int(input("Enter the maximum value for which you want to play the game : "))
guess_number(x)





        
                      
