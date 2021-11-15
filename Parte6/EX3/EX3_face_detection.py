#!/usr/bin/python3
import copy

import cv2


def main():

    window_name = 'Face detection display window'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('/home/goncalo/Desktop/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

    # To capture video from webcam.
    cap = cv2.VideoCapture(0)
    # To use a video file as input
    # cap = cv2.VideoCapture('filename.mp4')

    while True:
        # Read the frame
        _, img = cap.read()  # _ is a variable thas shows if the detection succeeded, we don't need it

        image_gui = copy.deepcopy(img)
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # 1.1 é fator de escala | 4 é o número de neighbours a detetar
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(image_gui, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display
        cv2.imshow(window_name, image_gui)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==113:
            break
    # Release the VideoCapture object
    cap.release()


if __name__ == '__main__':
    main()