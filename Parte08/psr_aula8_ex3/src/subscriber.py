#!/usr/bin/env python3
import rospy
import argparse
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard: %s ", data.data)


def main():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can

    # .............................................................
    # Initialization
    # .............................................................

    parser = argparse.ArgumentParser(description='Part8 example')
    parser.add_argument('--topic', type=str, default='chatter ', help='topic to listen')

    args = vars(parser.parse_args())

    # .............................................................
    # Execution
    # .............................................................
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber(args['topic'], String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()