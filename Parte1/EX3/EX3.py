#!/usr/bin/python3
from colorama import Fore, Back, Style
import argparse


def isPrime(value):
    #print('Checking if ' +str(value)+' is prime:')

    for i in range (2,value):
        remainder = value % i  # % = resto da divisão inteira
       # print('Division by ' + str(i) + ' is ' +str(remainder))

        if remainder ==0:
            #print('Number ' + str(value) + 'is not prime because division by ' +str(i) + ' has 0 remainder')
            return False
    return True

def main():


    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--maximum_number',  type=int, help='an integer for the accumulator')

    args = vars(parser.parse_args())

    print("Starting to compute prime numbers up to " + str(args['maximum_number']))

    count = 0;
    for i in range(1, args['maximum_number']+1):
        if isPrime(i):
            print(Back.GREEN + 'Number ' +Back.BLUE+ str(i) + Back.GREEN +' is prime.' + Style.RESET_ALL)
            count+=1  #igual a count=count+1
        else:
            print(Back.RED + Style.BRIGHT + 'Number ' + str(i) + ' is not prime.' + Style.RESET_ALL)
            pass

    print(Fore.BLUE + Back.YELLOW +'Between 1 and ' + str(args['maximum_number']) + ' there are ' + str(count)+ ' prime numbers'+ Style.RESET_ALL)
if __name__ == "__main__":
    main()