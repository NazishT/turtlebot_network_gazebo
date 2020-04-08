#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def callback(msg):
        move = Twist()

	print msg.ranges[360]
	if msg.ranges[360]<1:
	   move.linear.x=-1
	   move.angular.z=-1
	pub.publish(move)


rospy.init_node('force_feedback')
sub=rospy.Subscriber('/scan', LaserScan, callback)
pub= rospy.Publisher('/robot1/mobile_base/commands/velocity',Twist, queue_size=5)

rospy.spin()
