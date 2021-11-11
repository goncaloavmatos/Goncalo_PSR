#!/usr/bin/python3

import cv2


def main():

    image_filename = '/home/goncalo/Desktop/Goncalo_PSR/Parte5/images/atlas2000_e_atlasmv.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)  # Load an image

    height, width, _ = image.shape

    (y, x) = [int(height/2), int(width/2)]

    print((x, y))

    image_processed = image
    image_processed = cv2.circle(image_processed, (x, y), 100, (200, 0, 0), 20)  # Alínea a)

    image_processed = cv2.putText(image_processed, 'PSR', (x-50, y), cv2.FONT_HERSHEY_PLAIN, 4, (200, 0, 0), 10)   # Alínea b)

    cv2.imshow('window', image)  # Display the image
    cv2.imshow('processed', image_processed)  # Display the image
    cv2.waitKey(0)  # wait for a key press before proceeding


if __name__ == '__main__':
    main()