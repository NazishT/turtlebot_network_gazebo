#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def callback(msg):
        move = Twist()


	for i in [60,120]:
      	    
            if min(msg.ranges)> 0.05 and min(msg.ranges)<1.0:
               print min(msg.ranges)
               move.linear.x=0.0
               move.angular.z=2
               pub1.publish(move)
               #pub2.publish(move)


rospy.init_node('force_feedback')
sub=rospy.Subscriber('/robot2/scan', LaserScan, callback)
pub1= rospy.Publisher('/robot2/cmd_vel_mux/input/safety_controller',Twist, queue_size=10)
#pub2= rospy.Publisher('/cmd_vel_mux/input/safety',Twist, queue_size=10)

rospy.spin()
