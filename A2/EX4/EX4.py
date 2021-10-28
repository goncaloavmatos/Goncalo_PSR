#!/usr/bin/python3

from colorama import Fore, Back, Style
import argparse
import readchar

def PrintAllCharsUpTo(stop_char):
    print('I dont know how to do this' )
    print('Printing all values up to stop_char ->' + str(stop_char))

    # desde o nr decimal correspondente ao espaço até ao numero correspondente ao caracter que introduzir
    for i in range(ord(' '), ord(stop_char)+1):
        print(chr(i)); #imprime o caracter correpondente a cada numero do ciclo

def readAllUpTo(stop_key):

    count_pressed_numbers = 0
    count_pressed_other = 0

    while True:
        print('Type something (X to stop)')
        pressed_key=readchar.readkey()

        if str.isnumeric (pressed_key):  #se é numero, conta um numero
            count_pressed_numbers +=1    #se não é numero, conta outros
        else:
            count_pressed_other +=1

        if pressed_key == stop_key:
            print('You typed ' + Fore.RED + Style.BRIGHT + pressed_key + Style.RESET_ALL + ' terminating.')
            break
        else:
            print('Thanks for typing ' + Fore.BLUE + Style.BRIGHT + pressed_key + Style.RESET_ALL)

    print('You entered ' + str(count_pressed_numbers) + ' numbers.')
    print('You entered ' + str(count_pressed_other) + ' others.')

def main():
    #EX 4a
    #print('give me the stop char')
    #pressed_char = readchar.readchar()

    #PrintAllCharsUpTo(pressed_char)

    #EX 4b
    readAllUpTo('X')





if __name__ == "__main__":
    main()