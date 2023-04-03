#Asks user for height, print triangle

height = int(input("Height of your triangle: "))

for r in range(height+1):
    for m in range(r-1):
        for c in range(1, height - r+2):
            print('', end='*')
        print()

