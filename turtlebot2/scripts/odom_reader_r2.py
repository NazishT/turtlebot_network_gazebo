#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
v_x = 0
w = 0

def odom_callback(msg):

 
    vel_msg = Twist()

    global v_x, w

    v_x=msg.linear.x
    w = msg.angular.z

    vel_msg.linear.x = v_x
    vel_msg.angular.z = w
    pub.publish(vel_msg)

    print "------------------------------------------------"
    print "velocity linear x = " + str(v_x)
    print "velocity angular z = " + str (w)
 

if __name__=='__main__':
     rospy.init_node('odom_reader_r2', anonymous=True)     
     sub = rospy.Subscriber('robot1/mobile_base/commands/velocity', Twist, odom_callback) 
     pub = rospy.Publisher('robot2/mobile_base/commands/velocity', Twist, queue_size=100)
     #pub = rospy.Publisher('robot2/cmd_vel/input/switch', Twist, queue_size=5)
     while not rospy.is_shutdown():
     	rospy.spin()
