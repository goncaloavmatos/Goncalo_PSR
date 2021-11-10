#!/usr/bin/python3

import cv2
import numpy as np


def mouse_callback(event, x, y, flags, param):
    global image_original

    pix=image_original[y,x]
    B = pix[0]
    G = pix[1]
    R = pix[2]

    print('R = ' + str(R) + ';  G = ' + str(G) + ';  B = ' + str(B))

def main():
    global image_original
    #Load image
    image_filename = '/home/goncalo/Desktop/Goncalo_PSR/Parte5/images/atlas2000_e_atlasmv.png'
    image_original = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    image_b, image_g, image_r = cv2.split(image_original)

    ranges = {'b': {'min':0, 'max':50},
              'g': {'min':80, 'max':256},
              'r': {'min':0, 'max':50}}

    #Process image
    mins = np.array([ranges['b']['min'], ranges['g']['min'] , ranges['r']['min'] ])
    maxs =  np.array([ranges['b']['max'], ranges['g']['max'] , ranges['r']['max'] ])
    Mask = cv2.inRange(image_original, mins, maxs)
    Mask= Mask.astype(np.bool)

    image_original[Mask]=[0,0,255]

    #Visualization
    cv2.namedWindow('original',cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("original", mouse_callback)

    cv2.imshow('original', image_original)  # Display the image
    #cv2.imshow('processed', Mask)  # Display the image

    cv2.waitKey(0)

if __name__ == '__main__':
    main()