#!/usr/bin/env python

import rospy
import cv2
import image_converter

# def callback(data):
#     rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def img_subscriber():

    rospy.init_node('img_subscriber', anonymous=True)
    image_converter.ImageConverter(nodeType='sub')
    rospy.spin()

if __name__ == '__main__':
    img_subscriber()