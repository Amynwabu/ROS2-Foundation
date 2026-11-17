#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyFirstNode(Node):
    """
    A simple ROS2 node that demonstrates basic node creation.
    This is your first step into ROS2 programming!
    """
    
    def __init__(self):
        # Initialize the node with name 'my_first_node'
        super().__init__('my_first_node')
        
        # Log a message when the node starts
        self.get_logger().info('Hello from My First Node!')
        
        # Create a timer that calls timer_callback every 1 second
        self.create_timer(1.0, self.timer_callback)
        
        # Initialize a counter
        self.counter = 0
    
    def timer_callback(self):
        """
        This function is called every second by the timer.
        """
        self.counter += 1
        self.get_logger().info(f'Counter: {self.counter}')

def main(args=None):
    # Initialize the ROS2 Python client library
    rclpy.init(args=args)
    
    # Create an instance of our node
    node = MyFirstNode()
    
    try:
        # Keep the node running and processing callbacks
        rclpy.spin(node)
    except KeyboardInterrupt:
        # Ctrl+C: shut down quietly
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
