#!/usr/bin/env python
import tf
import rospy

if __name__ == '__main__':

  rospy.init_node('amr_tf_br')

  bflaser_blink = tf.TransformBroadcaster()
  brlaser_blink = tf.TransformBroadcaster()
  blink_bfprint = tf.TransformBroadcaster()
  bfcamera_blink = tf.TransformBroadcaster()
  brcamera_blink = tf.TransformBroadcaster()

  bcasterfr_blink = tf.TransformBroadcaster()
  bcasterfl_blink = tf.TransformBroadcaster()
  bcasterrr_blink = tf.TransformBroadcaster()
  bcasterrl_blink = tf.TransformBroadcaster()

  bwcasterfr_blink = tf.TransformBroadcaster()
  bwcasterfl_blink = tf.TransformBroadcaster()
  bwcasterrr_blink = tf.TransformBroadcaster()
  bwcasterrl_blink = tf.TransformBroadcaster()

  rate = rospy.Rate(50)

  while not rospy.is_shutdown():

    blink_bfprint.sendTransform((0.00, 0.00, 0.16),
        tf.transformations.quaternion_from_euler(0, 0, 0),
        rospy.Time.now(),"base_link","base_footprint")

    bflaser_blink.sendTransform((0.25, 0.20, 0.00),
        tf.transformations.quaternion_from_euler(0, 0, 0),
        rospy.Time.now(),"front_laserscanner_link","base_link")

    brlaser_blink.sendTransform((-0.25, -0.20, 0.00),
        tf.transformations.quaternion_from_euler(0, 0, 3.1416),
        rospy.Time.now(),"rear_laserscanner_link","base_link")

    bfcamera_blink.sendTransform((0.25, 0.00, 0.00),
        tf.transformations.quaternion_from_euler(0, 0, 0),
        rospy.Time.now(),"front_dcamera_link","base_link")

    brcamera_blink.sendTransform((-0.25, 0.00, 0.00),
        tf.transformations.quaternion_from_euler(0, 0, 3.1416),
        rospy.Time.now(),"rear_dcamera_link","base_link")

    bcasterfr_blink.sendTransform((0.25, -0.20, -0.05),
        tf.transformations.quaternion_from_euler(0, 0, 3.1416),
        rospy.Time.now(),"caster_wheel_M2_link","base_link")

    bcasterfl_blink.sendTransform((0.25, 0.20, -0.05),
        tf.transformations.quaternion_from_euler(0, 0, 3.1416),
        rospy.Time.now(),"caster_wheel_M1_link","base_link")

    bcasterrl_blink.sendTransform((-0.25, -0.20, -0.05),
        tf.transformations.quaternion_from_euler(0, 0, 3.1416),
        rospy.Time.now(),"caster_wheel_M4_link","base_link")

    bcasterrl_blink.sendTransform((-0.25, 0.20, -0.05),
        tf.transformations.quaternion_from_euler(0, 0, 3.1416),
        rospy.Time.now(),"caster_wheel_M3_link","base_link")

    bwcasterfr_blink.sendTransform((0.047, 0.0, -0.04875),
        tf.transformations.quaternion_from_euler(1.570796, 0, 0),
        rospy.Time.now(),"wheel_M2_link","caster_wheel_M2_link")

    bwcasterfl_blink.sendTransform((0.047, 0.0, -0.04875),
        tf.transformations.quaternion_from_euler(1.570796, 0, 0),
        rospy.Time.now(),"wheel_M1_link","caster_wheel_M1_link")

    bwcasterrl_blink.sendTransform((0.047, 0.0, -0.04875),
        tf.transformations.quaternion_from_euler(1.570796, 0, 0),
        rospy.Time.now(),"wheel_M4_link","caster_wheel_M4_link")

    bwcasterrl_blink.sendTransform((0.047, 0.0, -0.04875),
        tf.transformations.quaternion_from_euler(1.570796, 0, 0),
        rospy.Time.now(),"wheel_M3_link","caster_wheel_M3_link")

    rate.sleep()
