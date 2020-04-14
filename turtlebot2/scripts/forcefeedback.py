#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def callback(msg):
        move = Twist()

	#print min(msg.ranges)
	if min(msg.ranges)>0.1 and min(msg.ranges)<0.2:
	   print min(msg.ranges)
	   move.linear.x=0.2
	   
	pub.publish(move)


rospy.init_node('force_feedback')
sub=rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/robot2/cmd_vel_mux/input/safety', Twist, queue_size=10)

rospy.spin()
