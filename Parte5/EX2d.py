#!/usr/bin/python3

import cv2
import numpy as np

def main():

    #Load image
    image_filename = '/home/goncalo/Desktop/Goncalo_PSR/Parte5/images/atlas2000_e_atlasmv.png'
    image_original = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    image_b, image_g, image_r = cv2.split(image_original)

    ranges = {'b': {'min':20, 'max':150},
              'g': {'min':20, 'max':150},
              'r': {'min':20, 'max':150}}

    #Process image
    mins = np.array([ranges['b']['min'], ranges['g']['min'] , ranges['r']['min'] ])
    maxs =  np.array([ranges['b']['max'], ranges['g']['max'] , ranges['r']['max'] ])
    image_processed = cv2.inRange(image_original, mins, maxs)

    #Visualization
    cv2.imshow('original', image_original)  # Display the image
    cv2.imshow('processed', image_processed)  # Display the image

    cv2.waitKey(0)

if __name__ == '__main__':
    main()