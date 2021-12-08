#!/usr/bin/env python3
import rospy
import argparse
from psr_parte9_ex_tp.msg import Dog
from std_msgs.msg import String


def callback(msg):
    rospy.loginfo(" I heard: %s ", msg.brothers)


def main():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can


    # .............................................................
    # Execution
    # .............................................................
    # run simultaneously.
    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber('chatter', Dog, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()