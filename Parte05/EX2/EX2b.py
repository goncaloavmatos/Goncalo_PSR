#!/usr/bin/python3

import cv2

def main():

    #Load image
    image_filename = '/home/goncalo/Desktop/Goncalo_PSR/Parte05/images/atlascar2.png'
    image_original = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image_gray=cv2.cvtColor(image_original,cv2.COLOR_BGR2GRAY)

    #Process image
    retval, image_thresholded = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)

    #numpy data
    print(type(image_original))

    print(image_original.shape)

    print(image_original.dtype)


    #Visualization
    #cv2.imshow('original', image_original)  # Display the image
    #cv2.imshow('gray', image_gray)  # Display the image
    #cv2.imshow('processed', image_thresholded) # Display the image

    #cv2.waitKey(0)


if __name__ == '__main__':
    main()