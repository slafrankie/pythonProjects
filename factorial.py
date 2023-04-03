#Finds factorial of number given by user

factorial = 1

#User enters integer
num = int(input("Enter the number: "))

#If loop validates whether number is whole and positive
if num < 0:
    print("Number must be positive and greater than 0")
else:
    #for loop to perform the factorial operation
    for x in range(1,num + 1):
        factorial = factorial * x

    print('Factorial of ', num)
    print(factorial)
        
