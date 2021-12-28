#!/usr/bin/env python3

import math
import rospy
import random
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Point
from visualization_msgs.msg import MarkerArray, Marker

publisher = rospy.Publisher('/markers', MarkerArray, queue_size=1)


def create_marker(group_id):

    # create marker
    marker = Marker()
    marker.header.frame_id = "left_laser"
    marker.header.stamp = rospy.Time.now()
    marker.ns = "my_namespace"
    marker.id = group_id
    marker.type = Marker.SPHERE_LIST
    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0  # otherwise quaternion is not normalized
    marker.scale.x = 0.1
    marker.scale.y = 0.1
    marker.scale.z = 0.1
    marker.color.a = 0.5  # Don't forget to set the alpha!
    # create new randomized color for every new marker
    marker.color.r = random.random()
    marker.color.g = random.random()
    marker.color.b = random.random()

    return marker


def callback(msg):
    rospy.loginfo("LaserScan received...")

    x_prev, y_prev = 1000, 1000
    dist_threshold = 0.3

    marker_array = MarkerArray()

    # Transformar pontos em coord polares em pontos em coord cartesianas
    z = 0

    for idx, range in enumerate(msg.ranges):
        theta = msg.angle_min + msg.angle_increment * idx
        x = range * math.cos(theta)
        y = range * math.sin(theta)

        #should I create a new cluster?

        dist = math.sqrt((x_prev - x)**2 + (y_prev-y)**2)
        if dist > dist_threshold:  # new cluster
            idx_group = len(marker_array.markers)
            marker = create_marker(idx_group)  # new marker for new cluster
            marker.points = []

            marker_array.markers.append(marker)  # add marker to marker array

        last_marker = marker_array.markers[-1]  # saves the most recently created marker to a variable
        last_marker.points.append(Point(x=x, y=y, z=z))  # add point to the most recent marker

        x_prev = x
        y_prev = y

    publisher.publish(marker_array)
    rospy.loginfo("Marker Array published...")


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('lidar_subscriber', anonymous=True)

    rospy.Subscriber("/left_laser/laserscan", LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()