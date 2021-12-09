#!/usr/bin/python3
from colorama import Fore, Back, Style
import time
import math

def main():
    in_seconds = time.time() #The time() function returns the number of seconds passed since epoch. epoch= January 1, 1970, 00:00:00 at UTC
    local_time = time.ctime(in_seconds) #The time.ctime() function takes seconds passed since epoch as an argument and returns a string representing local time.

    print('This is Ex1 and the local time is: ' + Fore.BLUE + Back.YELLOW + Style.BRIGHT + local_time + Style.RESET_ALL)


if __name__ == '__main__':
        main()
