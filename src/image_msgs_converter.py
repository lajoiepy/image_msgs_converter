#!/usr/bin/env python
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):
    rospy.init_node('image_msgs_converter', anonymous=True)
    output_topic = rospy.get_param("/image_msgs_converter/output_topic")
    input_topic = rospy.get_param("/image_msgs_converter/input_topic")
    self.output_image_type = rospy.get_param("/image_msgs_converter/output_image_type")
    self.image_pub = rospy.Publisher(output_topic, Image)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber(input_topic,Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, self.output_image_type)
    except CvBridgeError as e:
      print(e)
    try:
      converted_msg = self.bridge.cv2_to_imgmsg(cv_image, self.output_image_type)
      converted_msg.header = data.header
      self.image_pub.publish(converted_msg)
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = image_converter()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
