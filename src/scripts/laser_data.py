#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def laserdata_callback(msg):

        for i in [60,120]:
            print (msg.ranges[i])

rospy.init_node('laser_data')
sub = rospy.Subscriber('/robot2/scan', LaserScan, laserdata_callback)


rospy.spin()
