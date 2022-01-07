#!/usr/bin/env python3
import rospy
import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv

# useful: http://wiki.ros.org/tf2/Tutorials/Writing%20a%20tf2%20listener%20%28Python%29

def main():
    rospy.init_node('mercury_to_moon')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    rate = rospy.Rate(1.0)

    # tries listening to transform
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('mercury', 'moon', rospy.Time())
            x, y = trans.transform.translation.x, trans.transform.translation.y
            distance = math.sqrt(x**2 + y**2)
            rospy.loginfo('Distance between mercury and moon is ' + str(distance))
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rospy.logwarn('Could not find transform from mercury to moon.')
            rate.sleep()
            continue

        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass