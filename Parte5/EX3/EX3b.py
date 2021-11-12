#!/usr/bin/python3

import argparse
from functools import partial
import cv2

def onTrackbarMin(minimum, image_gray, window_name):
    # Add code here to threshold image_gray and show image in window

    Mask = cv2.inRange(image_gray, 0, minimum)
    Mask=~Mask
    cv2.imshow(window_name, Mask)

    #image_gray[Mask]=0

def main():
    window_name = 'window - Ex3b'

    # Argumentos entrada
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)

    onTrackbarPartial = partial(onTrackbarMin, image_gray=image_gray, window_name=window_name)

    cv2.namedWindow(window_name)
    cv2.createTrackbar('Threshold', window_name, 0, 255, onTrackbarPartial)

    # add code to create the trackbar ...
    cv2.waitKey(0)

if __name__ == '__main__':
    main()