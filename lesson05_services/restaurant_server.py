#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from restaurant_interfaces.srv import TakeOrder

MENU = ('burger', 'salad')

class RestaurantServer(Node):
    def __init__(self):
        super().__init__('restaurant_server')
        self.declare_parameter('max_quantity', 5)
        self.pub = self.create_publisher(String, 'orders', 10)
        self.srv = self.create_service(TakeOrder, 'take_order', self.handle_order)

    def handle_order(self, request, response):
        item = request.item_name.strip().lower()
        limit = self.get_parameter('max_quantity').value
        response.accepted = item in MENU and 0 < request.quantity <= limit
        if response.accepted:
            order = f'{request.quantity} x {item}'
            self.pub.publish(String(data=order))
            response.message = f'{order} coming up'
        elif item not in MENU:
            response.message = f'Sorry, we do not serve {item}'
        else:
            response.message = f'Quantity must be between 1 and {limit}'
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = RestaurantServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
