import rospy
import math
from giskardpy.python_interface import GiskardWrapper
from geometry_msgs.msg import PoseStamped, Point, Quaternion
 
# init ros node
rospy.init_node('test')
giskard_wrapper = GiskardWrapper()

r_goal = PoseStamped()
r_goal.header.frame_id = 'base_footprint'
r_goal.header.stamp = rospy.get_rostime()
r_goal.pose.position = Point(1.5, -2.0, 0.0)
r_goal.pose.orientation = Quaternion(0.0, 0.0, -math.sqrt(2)/2, math.sqrt(2)/2)
giskard_wrapper.set_cart_goal('odom', 'base_footprint', r_goal)
 
giskard_wrapper.plan_and_execute()

r_goal = PoseStamped()
r_goal.header.frame_id = 'gripper_tool_frame'
r_goal.header.stamp = rospy.get_rostime()
r_goal.pose.position = Point(0.41, -0.535, 0.0)
r_goal.pose.orientation = Quaternion(0.0, 0.0, -math.sqrt(2)/2, math.sqrt(2)/2)
giskard_wrapper.set_cart_goal('base_footprint', 'gripper_tool_frame', r_goal)
 
giskard_wrapper.plan_and_execute()

r_goal = PoseStamped()
r_goal.header.frame_id = 'gripper_tool_frame'
r_goal.header.stamp = rospy.get_rostime()
r_goal.pose.position = Point(0.0, 0.0, 0.35)
r_goal.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)
giskard_wrapper.set_cart_goal('base_footprint', 'gripper_tool_frame', r_goal)
 
giskard_wrapper.plan_and_execute()

r_goal = PoseStamped()
r_goal.header.frame_id = 'gripper_tool_frame'
r_goal.header.stamp = rospy.get_rostime()
r_goal.pose.position = Point(0.0, 0.0, -0.35)
r_goal.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)
giskard_wrapper.set_cart_goal('base_footprint', 'gripper_tool_frame', r_goal)
 
giskard_wrapper.plan_and_execute()

r_goal = PoseStamped()
r_goal.header.frame_id = 'base_footprint'
r_goal.header.stamp = rospy.get_rostime()
r_goal.pose.position = Point(-2.0, -1.5, 0.0)
r_goal.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)
giskard_wrapper.set_cart_goal('odom', 'base_footprint', r_goal)
 
giskard_wrapper.plan_and_execute()


