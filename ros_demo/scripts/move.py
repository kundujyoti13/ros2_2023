import rclpy
from geometry_msgs.msg import Twist

 

def move_rosbot():
    rclpy.init()

 

    node = rclpy.create_node('rosbot_controller')

 

    cmd_pub = node.create_publisher(Twist, 'cmd_vel', 10)

 

    # Create a Twist message with linear velocity in the x-axis
    twist = Twist()
    twist.linear.x = 0.2  # Adjust the linear velocity as desired

 

    # Publish the Twist message repeatedly to move the ROSbot
    while rclpy.ok():
        cmd_pub.publish(twist)
        node.get_logger().info('Moving ROSbot forward')
        rclpy.spin_once(node)

 

    # Stop the ROSbot when the program is interrupted
    twist.linear.x = 0.0
    cmd_pub.publish(twist)

 

    node.destroy_node()
    rclpy.shutdown()

 

if __name__ == '__main__':
    move_rosbot()