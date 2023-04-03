#Program ask for package quantity purchased
#Prints price after discount

price = 99
quantity = int(input("How many packages have you purchased: "))

if quantity >= 10 and quantity <= 19:
    price = (price * quantity) * 0.2
    print(price)
elif quantity >= 20 and quantity <= 49:
    price = (price * quantity) * 0.3
    print(price)
elif quantity >= 50 and quantity <= 99:
    price = (price * quantity) * 0.4
    print(price)
elif quantity >= 100:
    price = (price * quantity) * 0.5
    print(price)
else:
    print("No discount")
    price = quantity * price
    print(price)
