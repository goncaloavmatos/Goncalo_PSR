#!/usr/bin/python3

import argparse
import numpy as np

import cv2

# Global variables
window_name = 'window - Ex3a'
image_gray = None


def onTrackbarMin(minimum):
    # Add code here to threshold image_gray and show image in window

    global image_gray
    Mask = cv2.inRange(image_gray, 0, minimum)
    Mask=~Mask
    cv2.imshow(window_name, Mask)

    #image_gray[Mask]=0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    cv2.createTrackbar('Red', window_name, 0, 255, onTrackbarMin)

    # add code to create the trackbar ...
    cv2.waitKey(0)

if __name__ == '__main__':
    main()