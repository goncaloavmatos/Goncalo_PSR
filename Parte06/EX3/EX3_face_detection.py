#!/usr/bin/python3
import copy

import cv2
import numpy as np


def main():

    window_name = 'Face detection display window'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
   #cv2.namedWindow('mask_face', cv2.WINDOW_AUTOSIZE)

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('/home/goncalo/Desktop/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

    # To capture video from webcam.
    cap = cv2.VideoCapture(0)
    # To use a video file as input
    # cap = cv2.VideoCapture('filename.mp4')

    while True:
        # Read the frame
        _, img = cap.read()  # _ is a variable thas shows if the detection succeeded, we don't need it

        height, width, _ = img.shape

        # Create mask of the rectangle that is placed on the detected face
        mask_face = np.ndarray((height, width), dtype=np.uint8)
        mask_face.fill(0)

        image_gui = copy.deepcopy(img)
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # 1.1 é fator de escala | 4 é o número de neighbours a detetar
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(image_gui, (x, y), (x+w, y+h), (255, 0, 0), 2)

            #Create mask of the rectangle that is placed on the detected face
            mask_face = cv2.rectangle(mask_face, (x, y), (x + w, y + h), 255, -1)

            # adicionar 50 no canal verde dos pixels da mascara e retirar 10 ao azul e vermelho
            cv2.add(image_gui, (-10, 50, -10, 0), dst=image_gui, mask=mask_face)

        # .......... Display .................
        cv2.imshow(window_name, image_gui)
        #cv2.imshow('mask_face', mask_face)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==113:
            break
    # Release the VideoCapture object
    cap.release()


if __name__ == '__main__':
    main()