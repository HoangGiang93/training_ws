import rospy
import math
from giskardpy.python_interface import GiskardWrapper
from geometry_msgs.msg import PoseStamped, Point, Quaternion
 
# init ros node
rospy.init_node('test')
giskard_wrapper = GiskardWrapper()

r_goal = PoseStamped()
r_goal.header.frame_id = 'gripper_tool_frame'
r_goal.header.stamp = rospy.get_rostime()
r_goal.pose.position = Point(0.0, -0.06, 0.1)
r_goal.pose.orientation = Quaternion(-0.5, -0.5, -0.5, 0.5)
giskard_wrapper.set_cart_goal('odom', 'gripper_tool_frame', r_goal)
 
giskard_wrapper.plan_and_execute()

r_goal = PoseStamped()
r_goal.header.frame_id = 'gripper_tool_frame'
r_goal.header.stamp = rospy.get_rostime()
r_goal.pose.position = Point(-0.6, 0.0, 0.0)
r_goal.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)
giskard_wrapper.set_cart_goal('odom', 'gripper_tool_frame', r_goal)
 
giskard_wrapper.plan_and_execute()

r_goal = PoseStamped()
r_goal.header.frame_id = 'gripper_tool_frame'
r_goal.header.stamp = rospy.get_rostime()
r_goal.pose.position = Point(0.0, 0.35, 0.0)
r_goal.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)
giskard_wrapper.set_cart_goal('odom', 'gripper_tool_frame', r_goal)
 
giskard_wrapper.plan_and_execute()

r_goal = PoseStamped()
r_goal.header.frame_id = 'gripper_tool_frame'
r_goal.header.stamp = rospy.get_rostime()
r_goal.pose.position = Point(0.6, 0.0, 0.0)
r_goal.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)
giskard_wrapper.set_cart_goal('odom', 'gripper_tool_frame', r_goal)
 
giskard_wrapper.plan_and_execute()

r_goal = PoseStamped()
r_goal.header.frame_id = 'gripper_tool_frame'
r_goal.header.stamp = rospy.get_rostime()
r_goal.pose.position = Point(0.0, 0.35, 0.0)
r_goal.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)
giskard_wrapper.set_cart_goal('odom', 'gripper_tool_frame', r_goal)
 
giskard_wrapper.plan_and_execute()

r_goal = PoseStamped()
r_goal.header.frame_id = 'gripper_tool_frame'
r_goal.header.stamp = rospy.get_rostime()
r_goal.pose.position = Point(-0.6, 0.0, 0.0)
r_goal.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)
giskard_wrapper.set_cart_goal('odom', 'gripper_tool_frame', r_goal)
 
giskard_wrapper.plan_and_execute()