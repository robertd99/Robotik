#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from beginner_tutorials.msg import Num
img_list = []
def callback(data):
   rospy.loginfo('image to controller published')
   img_list.append(data)
   rospy.loginfo(len(img_list))
def controller():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('controller', anonymous=True)

    rospy.Subscriber('imageController', Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    controller()




