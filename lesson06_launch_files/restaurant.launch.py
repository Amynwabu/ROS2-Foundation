from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='test2_py_pkg', executable='chef', name='chef_node', output='screen'),
        Node(package='test2_py_pkg', executable='restaurant_server',
             name='restaurant_server', output='screen',
             parameters=[{'max_quantity': 10}]),
    ])
