#! /usr/bin/env python

import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import control_msgs.msg
import trajectory_msgs.msg

rospy.init_node('test_odom')

# Creates the SimpleActionClient, passing the type of the action
# (FibonacciAction) to the constructor.
client = actionlib.SimpleActionClient('/iai_donbot/whole_body_controller/base/follow_joint_trajectory', control_msgs.msg.FollowJointTrajectoryAction)

# Waits until the action server has started up and started
# listening for goals.
client.wait_for_server()

# Creates a goal to send to the action server.
goal = control_msgs.msg.FollowJointTrajectoryActionGoal()
goal.goal.trajectory.joint_names = ['odom_x_joint', 'odom_y_joint', 'odom_z_joint']
point = trajectory_msgs.msg.JointTrajectoryPoint()
point.positions = [1, 1, 1]
point.velocities = [0, 0, 0]
point.effort = []
point.time_from_start.nsecs = 1
goal.goal.trajectory.points.append(point)

# Sends the goal to the action server.
client.send_goal(goal.goal)

# Waits for the server to finish performing the action.
client.wait_for_result()

# Prints out the result of executing the action
client.get_result()  
