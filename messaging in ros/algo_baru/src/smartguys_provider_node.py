#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import random

if __name__ == '__main__':
    rospy.init_node('smartguys_provider_node')
    rospy.loginfo('Node smartguys_provider started')
    pub = rospy.Publisher('/SG', String, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        data = random.choice(["LOW", "MEDIUM", "HIGH"])
        rospy.loginfo("SG Sending data: %s" % data)
        pub.publish(data)
        rate.sleep()