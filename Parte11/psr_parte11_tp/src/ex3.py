#!/usr/bin/env python3
import math

import rospy

# Because of transformations
import tf_conversions
import tf2_ros
import geometry_msgs.msg
import turtlesim.msg


def broadcast_orbit(broadcaster, transformation, parent, child, distance, alpha):
    # Define transformation
    transformation.header.stamp = rospy.Time.now()
    transformation.header.frame_id = parent
    transformation.child_frame_id = child
    transformation.transform.translation.x = distance * math.cos(alpha)
    transformation.transform.translation.y = distance * math.sin(alpha)
    transformation.transform.translation.z = 0.0
    transformation.transform.rotation.w = 1  # for normalized quaternion

    broadcaster.sendTransform(transformation)  # publish transformation

def main():
    rospy.init_node('circular_frame')

    br = tf2_ros.TransformBroadcaster()  # create broadcaster

    rate = rospy.Rate(100)  # 100Hz
    alpha = 0
    period = rospy.get_param('~period')

    t = geometry_msgs.msg.TransformStamped()  # create transformation

    while not rospy.is_shutdown():

        # changing angle for velocity
        alpha += (1/period)/1000
        if alpha > 2 * math.pi:
            alpha = 0

        broadcast_orbit(br, t, rospy.remap_name('parent'), rospy.remap_name('child'), rospy.get_param('~distance_to_parent'), alpha)

        rate.sleep()

    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass