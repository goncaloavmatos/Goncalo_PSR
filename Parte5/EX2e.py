#!/usr/bin/python3

import cv2
import numpy as np


def mouse_callback(event, x, y, flags, param):
    global image_original

    pix=image_original[y,x]
    H = pix[0]
    S = pix[1]
    V = pix[2]

    print('R = ' + str(R) + ';  G = ' + str(G) + ';  B = ' + str(B))

def main():
    global image_original
    #Load image
    image_filename = '/home/goncalo/Desktop/Goncalo_PSR/Parte5/images/atlas2000_e_atlasmv.png'
    image_original = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image_hsv = cv2.cvtColor(image_original, cv2.COLOR_BGR2HSV)  # Load an image

    image_h, image_s, image_v = cv2.split(image_hsv)

    ranges = {'h': {'min':40, 'max':180},
              's': {'min':180, 'max':256},
              'v': {'min':60, 'max':180}}

    #Process image
    mins = np.array([ranges['h']['min'], ranges['s']['min'] , ranges['v']['min'] ])
    maxs =  np.array([ranges['h']['max'], ranges['s']['max'] , ranges['v']['max'] ])
    Mask = cv2.inRange(image_hsv, mins, maxs)


    #Visualization
    cv2.namedWindow('original',cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("original", mouse_callback)

    cv2.imshow('original', image_original)  # Display the image
    cv2.imshow('processed', Mask)  # Display the image

    cv2.waitKey(0)

if __name__ == '__main__':
    main()