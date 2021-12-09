#!/usr/bin/env python3
# license removed for brevity

import rospy
from std_msgs.msg import String
from psr_aula8_ex4.msg import Dog

import argparse

def talker():

    # .............................................................
    # Initialization
    # .............................................................

    parser = argparse.ArgumentParser(description='Part8 example')
    parser.add_argument('--rate', type=float, default='1 ', help='message rate')
    parser.add_argument('--topic', type=str, default='chatter ', help='topic to listen')
    parser.add_argument('--message', type=str, default='Do not know what to say ', help='message to print')

    args = vars(parser.parse_args())

    pub = rospy.Publisher(args['topic'], Dog, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(args['rate'])  # 10hz

    # .............................................................
    # Execution
    # .............................................................

    while not rospy.is_shutdown():
        dog = Dog()
        dog.name = 'Lubi'
        dog.age = 6
        dog.color = 'brown'
        dog.brothers.append('ragnar')

        rospy.loginfo('Sending dog...')
        pub.publish(dog)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass