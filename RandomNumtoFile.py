#program writes random numbers to file
#user specifies how many numbers will be written
import random


def main():
    filename = ''
    noR = 0
    randNum = 0
    counter = 0

    #user chooses file to be written to
    filein = input('Enter filename for data to be written to: ')

    #user also specifies how many random numbers will be generated
    noR = int(input('Quantity of random numbers ' \
                    'to be written to file: '))

    #open file specified by user
    outFile = open(filein, 'w')

    #for loop to generate random integers and write them to
    #user defined file
    for counter in range(noR):
        randNum = random.randint(1, 500)
        outFile.write(str(randNum) + '\n')

    #closes outFile
    outFile.close()

    print('Writing data to file completed')

main()




