# Lesson 07: Smart Restaurant System — assignment, slide 37

Build a fresh system using the lecture patterns, not an independent periodic publisher alongside a disconnected service.

## Required architecture

```text
waiter (service client) -- /take_order --> manager (service server)
                                              |
                                       accepted orders
                                              |
                                           /orders
                                              |
                                       chef (subscriber)
```

## Packages

Reuse restaurant_interfaces (ament_cmake) from lesson05, containing srv/TakeOrder.srv:

```text
string item_name
int32 quantity
---
bool accepted
string message
```

Create restaurant_system as an ament_python package:

```bash
source /opt/ros/humble/setup.bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python restaurant_system --dependencies rclpy std_msgs restaurant_interfaces
```

Required structure:

```text
restaurant_system/
  package.xml
  setup.py
  setup.cfg
  resource/restaurant_system
  restaurant_system/
    __init__.py
    waiter.py
    manager.py
    chef.py
  launch/restaurant.launch.py
```

## Tasks

1. Implement waiter.py as a one-shot service client accepting item and quantity from the command line. Adapt lesson05 restaurant_client.py; import TakeOrder from restaurant_interfaces.srv and call /take_order. Wait for the service and log the response. Do not create a periodic order publisher here.
2. Implement manager.py as the service server AND publisher. Adapt lesson05 restaurant_server.py, change its node name to manager, accept burger/salad with a valid quantity, reject unknown items, and publish each accepted order once on /orders. Rejected orders must not be published.
3. Implement chef.py as a std_msgs/String subscriber to /orders, logging each order. Adapt the lesson04 subscriber.
4. Register the three executables in setup.py:

```python
entry_points={'console_scripts': [
    'waiter = restaurant_system.waiter:main',
    'manager = restaurant_system.manager:main',
    'chef = restaurant_system.chef:main',
]},
```

5. Create launch/restaurant.launch.py:

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='restaurant_system', executable='manager', output='screen'),
        Node(package='restaurant_system', executable='chef', output='screen'),
    ])
```

6. Install the launch file using setup.py data_files as in lesson06. Add launch and launch_ros as exec_depend entries in restaurant_system/package.xml. Keep rclpy, std_msgs and restaurant_interfaces dependencies. The launch starts the two persistent nodes only; run the waiter separately with arguments.

## Build and success test

Stop the lecture restaurant_server and periodic waiter first so they cannot interfere with the assignment graph.

```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install --packages-up-to restaurant_system
source install/setup.bash
ros2 launch restaurant_system restaurant.launch.py
```

In separately sourced terminals, start observations before submitting orders:

```bash
ros2 node list
ros2 topic echo /orders
rqt_graph
```

Then run the slide's success test:

```bash
ros2 run restaurant_system waiter burger 2
```

Expected: accepted service response, one /orders message and a chef log for 2 x burger. Submit an unknown item; expect rejection and no corresponding chef order. Inspect the service separately with:

```bash
ros2 service call /take_order restaurant_interfaces/srv/TakeOrder "{item_name: burger, quantity: 2}"
```

## Stretch goals

Add a menu parameter and explain the QoS choices, or implement CookOrder as an action with progress feedback and cancellation. Use max_quantity from the lecture example to demonstrate runtime configuration if desired.

Submit source packages, evidence of the running graph and accepted/rejected cases, and a short justification of topic versus service versus action. This is an assignment brief, not a supplied completed assessment solution.
