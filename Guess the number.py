import random
def rando():
    a=random.randint(1,100)
    for i in range(10):
        n=int(input("\nEnter Your Number:"))
        if(n==a):
            print("Congratulations!! Your Guess is CORRECT")
            break
        elif(n>a):
            print("Nah! Try it a little lower\n")
        elif(n<a):
            print("Oops!! Make it a little higher\n")
    else:
        print("You have run out of your guesses.Try Again\n")
        rando()
print("Welcome to the Number Guessing Game\n")
print("You have only 10 chances to guess the number.Enter from 1 to 100\n")
rando()
