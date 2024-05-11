#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int16
from rospy import set_param

class MobileLegendsClient:

    def __init__(self):
        rospy.init_node('budi01_gaming_client')
        rospy.loginfo('Node budi01_gaming_client started')

        self.sg_data = None
        self.xs_data = None

        rospy.Subscriber('/XS', Int16, callback=self.xs_callback)
        rospy.Subscriber('/SG', String, callback=self.sg_callback)

    def sg_callback(self, msg):
        smartguys_data = msg.data
        rospy.loginfo("Received SG data: %s" % smartguys_data)
        self.sg_data = smartguys_data

    def xs_callback(self, msg):
        xs_data = msg.data
        rospy.loginfo("Received XS data: %s" % xs_data)
        self.xs_data = xs_data
        self.process_data()

    def process_data(self):
        rospy.loginfo("Processing data: %s, %s" % (self.xs_data, self.sg_data))
        if self.sg_data == "HIGH" and self.xs_data > 50:
            rospy.loginfo("Budi says: LANCAR")
        elif self.sg_data == "MEDIUM" and self.xs_data > 50:
            rospy.loginfo("Budi says: PATAH-PATAH")
        elif self.sg_data == "LOW" and self.xs_data > 50:
            rospy.loginfo("Budi says: NGE-LAG")
        else:
            rospy.loginfo("Budi says: MENDING TURU")



if __name__ == '__main__':
    try:
        budi = MobileLegendsClient()
        rospy.spin()
    except rospy.ROSInterruptException:
        pas