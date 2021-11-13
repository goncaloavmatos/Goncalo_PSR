#!/usr/bin/python3

import argparse
import cv2
import numpy as np
from pprint import pprint
import json

# ............... Global Variables ................................

minBH = 0
maxBH = 0
minGS = 0
maxGS = 0
minRV = 0
maxRV = 0


# .................. Trackbar callback functions ....................
# These functions change each limit according to changes in their respective trackbars

def onTrackbarMinBH(val):
    global minBH
    minBH = val

def onTrackbarMaxBH(val):
    global maxBH
    maxBH = val

def onTrackbarMinGS(val):
    global minGS
    minGS = val

def onTrackbarMaxGS(val):
    global maxGS
    maxGS = val

def onTrackbarMinRV(val):
    global minRV
    minRV = val

def onTrackbarMaxRV(val):
    global maxRV
    maxRV = val



def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left click on: x = ' + str(x) + ', y = ' + str(y))





def main():
    window_name = 'window - Ex3d'

    # ............... Input arguments .........................

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    parser.add_argument('-hsv', action='store_true', help='To use HSV image. Default is RGB.')
    args = vars(parser.parse_args())

    # .............. Processing input image .....................

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    cv2.imshow('original',image)
    cv2.namedWindow(window_name)

    if args['hsv']:  # To change from BGR to HSV, if requested
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # ................Create Trackbars...............................................

    cv2.createTrackbar('Min BH', window_name, 0, 255, onTrackbarMinBH)
    cv2.createTrackbar('Max BH', window_name, 255, 255, onTrackbarMaxBH)
    cv2.createTrackbar('Min GS', window_name, 0, 255, onTrackbarMinGS)
    cv2.createTrackbar('Max GS', window_name, 255, 255, onTrackbarMaxGS)
    cv2.createTrackbar('Min RV', window_name, 0, 255, onTrackbarMinRV)
    cv2.createTrackbar('Max RV', window_name, 255, 255, onTrackbarMaxRV)

    previous_ranges = {}

    # .............Assigning limits selected with the trackbars.......................

    while True:

        if not args['hsv']:
            ranges = {'b': {'min': minBH, 'max': maxBH},
                      'g': {'min': minGS, 'max': maxGS},
                      'r': {'min': minRV, 'max': maxRV}}

            # Process image
            mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
            maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
            Mask = cv2.inRange(image, mins, maxs)
            cv2.imshow(window_name, Mask)

        else:
            ranges = {'h': {'min': minBH, 'max': maxBH},
                      's': {'min': minGS, 'max': maxGS},
                      'v': {'min': minRV, 'max': maxRV}}

            # Process image
            mins = np.array([ranges['h']['min'], ranges['s']['min'], ranges['v']['min']])
            maxs = np.array([ranges['h']['max'], ranges['s']['max'], ranges['v']['max']])
            Mask = cv2.inRange(image, mins, maxs)
            cv2.imshow(window_name, Mask)

        # ............. printing limits ...............

        if previous_ranges != ranges:
            pprint(ranges)
            previous_ranges = ranges

        cv2.setMouseCallback(window_name, onMouse)

        pressed_key = cv2.waitKey(1)

        # ............... termination routine ..............

        if pressed_key == ord('t'):
            print('Pressed t to terminate.')

            file_name = 'limits.json'
            with open(file_name, 'w') as file_handle:
                print('Saving dictionary with the current limits...')
                json.dump(ranges, file_handle)
                print('Limits saved.')
            break

if __name__ == '__main__':
    main()