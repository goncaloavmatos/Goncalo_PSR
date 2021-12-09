#!/usr/bin/env python3
import math

import rospy
import std_msgs.msg
from sensor_msgs.msg import LaserScan, PointField, PointCloud2
from sensor_msgs import point_cloud2

publisher = rospy.Publisher('/left_laser/point_cloud', PointCloud2, queue_size=1)


def callback(msg):
    rospy.loginfo("LaserScan received...")

    header = std_msgs.msg.Header(seq=msg.header.seq, stamp=msg.header.stamp, frame_id=msg.header.frame_id)
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
              PointField('y', 4, PointField.FLOAT32, 1),
              PointField('z', 8, PointField.FLOAT32, 1)]

    points = []

    #Transformar pontos em coord polares em pontos em coord cartesianas
    z = 0
    for idx, range in enumerate(msg.ranges):
        theta = msg.angle_min + msg.angle_increment * idx
        x = range * math.cos(theta)
        y = range * math.sin(theta)
        points.append([x, y, z])  # add poin to the pointcloud

    pc2 = point_cloud2.create_cloud(header, fields, points)
    publisher.publish(pc2)
    rospy.loginfo("PointCloud published...")


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