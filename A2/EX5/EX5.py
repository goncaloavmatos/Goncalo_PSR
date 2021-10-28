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

    #Ask for all the entries and put them in a list
    pressed_keys= [] #empty list to start

    count_pressed_numbers=0
    count_pressed_others = 0

    while True:
        print('Type something (X to stop)')
        pressed_key=readchar.readkey()


        if pressed_key == stop_key:
            print('You typed ' + Fore.RED + Style.BRIGHT + pressed_key + Style.RESET_ALL + ' terminating.')
            break
        else:
            print('Thanks for typing ' + Fore.BLUE + Style.BRIGHT + pressed_key + Style.RESET_ALL)
            pressed_keys.append(pressed_key)  #add element to list

    print('The keys you pressed are: ' + str(pressed_keys))

    #Analyse list and count
    count_pressed_numbers = 0
    count_pressed_other = 0
    pressed_numbers = []
    pressed_others = []

    for PressedKey in pressed_keys:  #este PressedKey é outro novo
        if str.isnumeric(PressedKey):
            count_pressed_numbers += 1
            pressed_numbers.append(PressedKey)
        else:
            count_pressed_other += 1
            pressed_others.append(PressedKey)

    print('You entered ' + str(count_pressed_numbers) + ' numbers:' + str(pressed_numbers))
    print('You entered ' + str(count_pressed_other) + ' others:' + str(pressed_others))

def main():
    #EX 4a
    #print('give me the stop char')
    #pressed_char = readchar.readchar()

    #PrintAllCharsUpTo(pressed_char)

    #EX 4b
    readAllUpTo('X')





if __name__ == "__main__":
    main()