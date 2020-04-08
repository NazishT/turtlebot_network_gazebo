#!/usr/bin/env python


import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

v_x = 0
w= 0

def odom_callback(msg):
 	
	vel_msg = Twist()
        global v_x, w
       
        v_x=msg.twist.twist.linear.x
        w=msg.twist.twist.angular.z


        vel_msg.linear.x=v_x
        vel_msg.angular.z=w
        pub.publish(vel_msg)

        print "------------------------------------------"
        print "velocity linear x=" +str(v_x)
        print "velocity angular z=" +str(w)


if __name__=='__main__':
        rospy.init_node('odom_reader_r1', anonymous=True)
	sub=rospy.Subscriber('/robot2/odom', Odometry, odom_callback)
        pub=rospy.Publisher('/robot1/cmd_vel_mux/input/navigation', Twist, queue_size=5)
        #pub=rospy.Publisher('robot1/mobile_base/commands/velocity', Twist, queue_size=5)

        while not rospy.is_shutdown():
           rospy.spin()
