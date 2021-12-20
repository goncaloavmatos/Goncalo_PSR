#!/usr/bin/env python3
import math

import rospy
import std_msgs.msg
from sensor_msgs.msg import LaserScan, PointField, PointCloud2, Image
from sensor_msgs import point_cloud2
import cv2
from cv_bridge import CvBridge

# Helpful: http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

def main():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('image_publisher', anonymous=False)

    publisher = rospy.Publisher('~image', Image, queue_size=1)

    # video capture setup
    capture = cv2.VideoCapture(0)
    window_name = 'Opencv window'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    rate = rospy.Rate(15)

    while True:
        _, cv_image = capture.read()

        cv2.imshow(window_name, cv_image)

        bridge = CvBridge()

        image_message = bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
        publisher.publish(image_message)

        if cv2.waitKey(1) == ord('q'):
            break

        rate.sleep()

    capture.release()
    cv2.destroyAllWindows()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()