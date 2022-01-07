#!/usr/bin/env python3
import math

import rospy

# Because of transformations
import tf_conversions
import tf2_ros
import geometry_msgs.msg
import turtlesim.msg


def main():
    rospy.init_node('circular_frame')

    br = tf2_ros.TransformBroadcaster()  # create broadcaster

    rate = rospy.Rate(10)  # 10Hz
    alpha = 0

    while not rospy.is_shutdown():
        t = geometry_msgs.msg.TransformStamped()  # create transformation

        # changing angle for velocity
        alpha += 0.01
        if alpha >2 * math.pi:
            alpha = 0

        rho = 3

        # Define transformation
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = 'parent'
        t.child_frame_id = 'child'
        t.transform.translation.x = rho * math.cos(alpha)
        t.transform.translation.y = rho * math.sin(alpha)
        t.transform.translation.z = 0.0
        q = tf_conversions.transformations.quaternion_from_euler(0, 0, 10 * alpha)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        br.sendTransform(t)  # publish transformation

        rate.sleep()

    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass