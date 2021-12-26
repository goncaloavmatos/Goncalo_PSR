#!/usr/bin/env python3
# license removed for brevity
import random
import rospy
from std_msgs.msg import String, ColorRGBA, Header
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3


def main():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('markers', Marker, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    # count = 0
    # increment = 0.1

    while not rospy.is_shutdown():
        #count += increment

        # -------------------------------------------------------------------------------------------------------------
        # Create marker - RED OPAQUE CUBE
        # -------------------------------------------------------------------------------------------------------------

        # Create marker
        marker = Marker()  # useful: http://docs.ros.org/en/noetic/api/visualization_msgs/html/msg/Marker.html

        # Marker has a header parameter that needs to be created (File type: std_msgs/Header.msg)
        header = Header(stamp= rospy.Time.now(), frame_id='world')

        # Marker has a Pose parameter that needs to be created (File type: geometry_msgs/Pose.msg)
        # Pose has a Position parameter(Point) and an Orientation parameter(Quaternion)
        point = Point(x=0, y=0, z=0)
        quaternion = Quaternion(x=0, y=0, z=0, w=1)  # W has to be 1 for normalized quaternion
        pose = Pose(position=point, orientation=quaternion)

        # Marker has a scale parameter that needs to be created (File type: geometry_msgs/Vector3.msg)
        scale = Vector3(x=1, y=1, z=1)

        # Marker has a color parameter that needs to be created (File type: std_msgs/ColorRGBA.msg)
        color = ColorRGBA(r=1, g=0, b=0, a=1)  # a is alfa, and represents the transparency. 0=transparent and 1=opaque

        # Marker parameters
        marker.header = header
        marker.type = Marker.CUBE
        marker.pose = pose
        marker.scale = scale
        marker.color = color
        marker.ns = 'marker'
        marker.id = 0

        # -------------------------------------------------------------------------------------------------------------
        # Create another marker
        # -------------------------------------------------------------------------------------------------------------
        # marker2 = Marker()  # useful: http://docs.ros.org/en/noetic/api/visualization_msgs/html/msg/marker.html
        #
        # # marker2 has a header parameter that needs to be created (File type: std_msgs/Header.msg)
        # header = Header(stamp=rospy.Time.now(), frame_id='world')
        #
        # # marker2 has a Pose parameter that needs to be created (File type: geometry_msgs/Pose.msg)
        # # Pose has a Position parameter(Point) and an Orientation parameter(Quaternion)
        # point = Point(x=count, y=0, z=0)
        # quaternion = Quaternion(x=0, y=0, z=0, w=1)  # W has to be 1 for normalized quaternion
        # pose = Pose(position=point, orientation=quaternion)
        #
        # # marker2 has a scale parameter that needs to be created (File type: geometry_msgs/Vector3.msg)
        # scale = Vector3(x=1, y=1, z=1)
        #
        # # marker2 has a color parameter that needs to be created (File type: std_msgs/ColorRGBA.msg)
        # color = ColorRGBA(r=1, g=0, b=0, a=1)  # a is alfa, and represents the transparency. 0=transparent and 1=opaque
        #
        # # marker2 has a points parameter that needs to be created
        # marker2.points = []
        #
        # for i in range(0, 10):
        #     x = random.randint(-3, 3)
        #     y = random.randint(-3, 3)
        #     z = random.randint(-1, 1)
        #     marker2.points.append(Point(x=x, y=y, z=z))
        #
        # # marker2 parameters
        # marker2.header = header
        # marker2.type = Marker.SPHERE_LIST
        # marker2.pose = pose
        # marker2.scale = scale
        # marker2.color = color
        # marker2.ns = 'marker2'
        # marker2.id = 1

        # -------------------------------------------------------------------------------------------------------------
        # Create another marker - GREEN TRANSPARENT SPHERE
        # -------------------------------------------------------------------------------------------------------------

        markersphere = Marker()  # useful: http://docs.ros.org/en/noetic/api/visualization_msgs/html/msg/marker.html

        # markersphere has a scale parameter that needs to be created (File type: geometry_msgs/Vector3.msg)
        scalesphere = Vector3(x=2, y=2, z=2)

        # markersphere has a color parameter that needs to be created (File type: std_msgs/ColorRGBA.msg)
        colorsphere = ColorRGBA(r=0, g=1, b=0, a=0.3)  # a is alfa, and represents the transparency. 0=transparent and 1=opaque

        # markersphere parameters
        markersphere.header = header
        markersphere.type = markersphere.SPHERE
        markersphere.pose = pose
        markersphere.scale = scalesphere
        markersphere.color = colorsphere
        markersphere.ns = 'markersphere'
        markersphere.id = 1

        # -------------------------------------------------------------------------------------------------------------
        # Create another marker - TEXT
        # -------------------------------------------------------------------------------------------------------------

        markertext = Marker()  # useful: http://docs.ros.org/en/noetic/api/visualization_msgs/html/msg/marker.html

        # markertext has a color parameter that needs to be created (File type: std_msgs/ColorRGBA.msg)
        color_t = ColorRGBA(r=1, g=0, b=0,
                                a=1)  # a is alfa, and represents the transparency. 0=transparent and 1=opaque

        # Marker has a Pose parameter that needs to be created (File type: geometry_msgs/Pose.msg)
        # Pose has a Position parameter(Point) and an Orientation parameter(Quaternion)
        point_t = Point(x=2, y=2, z=0)
        quaternion_t = Quaternion(x=0, y=0, z=0, w=1)  # W has to be 1 for normalized quaternion
        pose_t = Pose(position=point_t, orientation=quaternion_t)

        # markertext parameters
        markertext.header = header
        markertext.type = markertext.TEXT_VIEW_FACING
        markertext.text = 'Radius = ' + str(scalesphere.x)
        markertext.pose = pose_t
        markertext.scale = scale
        markertext.color = color_t
        markertext.ns = 'markertext'
        markertext.id = 2

        # Finally, publish created markers
        pub.publish(marker)
        pub.publish(markersphere)
        pub.publish(markertext)
        rospy.loginfo('Publishing Marco')
        rate.sleep()

        # if count > 3 or count < -3:
        #     increment = -increment


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass