#Asks user for the name of a file, displays the first five lines
#or displays all contents if less than 5 lines

def main():
    #variable 'file' used to 
    infile = open('numbers.txt')
    lines = 0
    value = 0
    avg= 0
    

    for line in infile:
        print(line)
        value = float(line) + value
        lines += 1

     
    avg = value / lines
    print(avg)
        

main()
