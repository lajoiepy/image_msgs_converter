cmake_minimum_required(VERSION 2.8.3)
project(image_msgs_converter)

find_package(catkin REQUIRED
sensor_msgs
cv_bridge
rospy
std_msgs
)

find_package(OpenCV 2 REQUIRED)
