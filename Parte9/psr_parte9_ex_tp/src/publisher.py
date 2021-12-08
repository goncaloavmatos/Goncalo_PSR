#!/usr/bin/env python3
# license removed for brevity

import rospy
from std_msgs.msg import String
from psr_parte9_ex_tp.msg import Dog
import colorama

def talker():

    # .............................................................
    # Initialization
    # .............................................................

    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('chatter', Dog, queue_size=10)

    # read a private parameter
    frequency = rospy.get_param("~frequency", default=1)  # til torna parametro privado

    rate = rospy.Rate(frequency)  # hz

    # .............................................................
    # Execution
    # .............................................................

    while not rospy.is_shutdown():
        #read global parameter
        highlight_text_color = rospy.get_param("/highlight_text_color")

        dog = Dog()
        dog.name = 'Lubi'
        dog.age = 6
        dog.color = 'brown'
        dog.brothers.append('ragnar')
        dog.brothers.append('Lau')

        rospy.loginfo('Sending dog... Name: ' + getattr(colorama.Fore, highlight_text_color) + str(dog.name) + colorama.Style.RESET_ALL)  # mesmo que um print em ROS
        pub.publish(dog)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass