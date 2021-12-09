#!/usr/bin/env python3
import cv2

def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    print('You are being recorded')

    while True:

        _, image = capture.read()  # get an image from the camera

        cv2.imshow(window_name, image)
        cv2.waitKey(1)



if __name__ == '__main__':
    main()