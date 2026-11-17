#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NewsPublisher(Node):
    """
    A ROS2 Publisher node that publishes news messages to /news_channel topic.
    This demonstrates basic topic publishing in ROS2.
    """
    
    def __init__(self):
        # Initialize the node
        super().__init__('news_publisher')
        
        # Create a publisher on the '/news_channel' topic
        # Queue size of 10 means it can hold 10 messages before dropping old ones
        self.publisher_ = self.create_publisher(String, '/news_channel', 10)
        
        # Create a timer that publishes every 2 seconds
        self.timer = self.create_timer(2.0, self.publish_news)
        
        # Counter for message numbering
        self.counter = 0
        
        self.get_logger().info('News Publisher started! Publishing to /news_channel')
    
    def publish_news(self):
        """
        Callback function that publishes news messages.
        """
        msg = String()
        self.counter += 1
        msg.data = f'Breaking News #{self.counter}: ROS2 is awesome!'
        
        # Publish the message
        self.publisher_.publish(msg)
        
        # Log what was published
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    # Initialize ROS2
    rclpy.init(args=args)
    
    # Create the node
    node = NewsPublisher()
    
    try:
        # Keep the node running
        rclpy.spin(node)
    except KeyboardInterrupt:
        # Ctrl+C: shut down quietly
        pass
    finally:
        # Cleanup (rclpy may already be shut down by the Ctrl+C handler)
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
