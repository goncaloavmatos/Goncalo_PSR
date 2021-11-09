#!/usr/bin/python3

import cv2

def main():

    #Load image
    image_filename = '/home/goncalo/Desktop/Goncalo_PSR/Parte5/images/atlascar2.png'
    image_original = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image_rgb = cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB)

    image_r, image_g, image_b = cv2.split(image_rgb)

    #Process image
    retval, image_r_processed = cv2.threshold(image_r, 150, 255, cv2.THRESH_BINARY)
    retval, image_g_processed = cv2.threshold(image_g, 100, 255, cv2.THRESH_BINARY)
    retval, image_b_processed = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)

    print('image_r shape' + str(image_r.shape))
    print('image_rgb shape' + str(image_rgb.shape))

    #Visualization
    cv2.imshow('original', image_original)  # Display the image
    cv2.imshow('processed r', image_r_processed) # Display the image
    cv2.imshow('processed g', image_g_processed)  # Display the image
    cv2.imshow('processed b', image_b_processed)  # Display the image

    cv2.waitKey(0)

if __name__ == '__main__':
    main()