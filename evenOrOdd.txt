#Counts total number of odd and even integers
#from 100 random numbers
import random

def main():
    numbers = random.randint(1, 10000)

    generator(numbers)

def generator(num):
    count = 0
    even = 0
    odd = 0
    while count != 100:
        num = num % 2

        if num == 0:
            even = even + 1
        else:
            odd = odd + 1


    print("Odd:", odd)
    print("Even:", even)

main()
        

