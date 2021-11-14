#!/usr/bin/python3

import cv2
import numpy as np
from colorama import Fore, Style


# Specifying that at the start the user is not painting
painting = False

# .................. On Mouse function ....................


def on_mouse(event, x, y, flags, param):

    global painting

    if event == cv2.EVENT_LBUTTONDOWN:
        painting = True
        whiteboard[y, x] = colour
    elif event == cv2.EVENT_MOUSEMOVE:
        if painting:
            whiteboard[y, x] = colour
    else:
        painting = False

# ................... Main function .......................


colour = (0, 0, 0)  # To start with black by default


def main():

    # ..................... Initialization ........................
    global pressed
    global whiteboard
    global colour

    whiteboard = np.zeros([400, 600, 3], dtype=np.uint8)
    whiteboard.fill(255)  # or img[:] = 255

    cv2.namedWindow('whiteboard', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('whiteboard', on_mouse)

    print('Press r, g or b to paint in red, green or blue respectively.')
    print('\nIf you do not select a colour, you will paint in black by default')
    print('c - Clear the white board\nt - Terminate')

    # ..................... Color selection ..........................

    while True:

        cv2.imshow('whiteboard', whiteboard)  # Display the image

        pressed = cv2.waitKey(1)

        if pressed == ord('r'):
            colour = (0, 0, 255)
            print('Current colour: ' + Fore.RED + 'RED' + Style.RESET_ALL)

        if pressed == ord('g'):
            colour = (0, 255, 0)
            print('Current colour: ' + Fore.GREEN + 'GREEN' + Style.RESET_ALL)

        if pressed == ord('b'):
            colour = (255, 0, 0)
            print('Current colour: ' + Fore.BLUE + 'BLUE' + Style.RESET_ALL)

        if pressed == ord('c'):
            whiteboard = np.zeros([400, 600, 3], dtype=np.uint8)
            whiteboard.fill(255)  # or img[:] = 255
            print('\nCLEARED THE WHITEBOARD')



        # To terminate programme
        if pressed == ord('t'):
            print('Pressed t to terminate.')
            break


if __name__ == '__main__':
    main()