#coin counting game
#decides if coins entered is =, < or > a dollar

penny = int(input("Number of pennies: "))
dime = int(input("Number of dimes: "))
nickel = int(input("Number of nickels: "))
quarter = int(input("Number of quarters: "))

nop = penny * 0.01
nod = dime * 0.10
non = nickel * 0.05
noq = quarter * 0.25

total = nop + nod + non + noq

if total == 1.00:
    print("You've made a dollar!")
elif total <= 0.99:
    print("That's less than a dollar")
else:
    print("That's more than a dollar")
