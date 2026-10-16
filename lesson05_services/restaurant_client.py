#!/usr/bin/env python3
import argparse
import sys
import rclpy
from rclpy.node import Node
from rclpy.utilities import remove_ros_args
from restaurant_interfaces.srv import TakeOrder

class OrderClient(Node):
    def __init__(self):
        super().__init__('order_client')
        self.cli = self.create_client(TakeOrder, 'take_order')

    def send_order(self, item, quantity):
        request = TakeOrder.Request()
        request.item_name = item
        request.quantity = quantity
        return self.cli.call_async(request)

def main(args=None):
    argv = sys.argv if args is None else ['order_client'] + list(args)
    parser = argparse.ArgumentParser(description='Submit a restaurant order')
    parser.add_argument('item')
    parser.add_argument('quantity', type=int)
    options = parser.parse_args(remove_ros_args(args=argv)[1:])
    if options.quantity <= 0:
        parser.error('quantity must be positive')
    rclpy.init(args=args)
    node = OrderClient()
    try:
        while rclpy.ok() and not node.cli.wait_for_service(timeout_sec=1.0):
            node.get_logger().info('Waiting for the restaurant...')
        if not rclpy.ok():
            return
        future = node.send_order(options.item, options.quantity)
        rclpy.spin_until_future_complete(node, future)
        response = future.result()
        if response is not None:
            node.get_logger().info(f'{response.accepted}: {response.message}')
        else:
            node.get_logger().error('No service response received')
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
