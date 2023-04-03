import random

#randomNum generator game

def main():
#asks user if they'd like to play game
#if yes, receives user input and matches it against randomly generated number
play = int(input("Play again? (1 for yes, 2 for no): ")
           if play == 1:
    
                numbers = random.randint(1, 100)
                choice = int(input("Guess the number: "))

                right_or_wrong(numbers, choice)
           else:
               break
#right_or_wrong checks user input against generated num
def right_or_wrong(num, choi):

    if num == choi:
        print("correct")
    else:
           while num != choi
               choi = int(input("Wrong, try again: "))
               if choi > num:
                   choice = int(input("Too high, try again:"))
               elif choi < num:
                   choi = int(input("Too low, try again:"))
               else:
                   print("Correct!")

    
