# Lesson 05: Services and actions — slides 22–29

Services use request–response communication. A client can submit a request asynchronously with call_async(); waiting for its future is a separate step. Never use a blocking service call inside a callback in this introductory single-threaded example.

## Create the interface

Set REPO to the absolute location of your clone. These commands assume the earlier lessons have created test2_py_pkg.

```bash
export REPO="$HOME/ROS2-Foundation"
source /opt/ros/humble/setup.bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_cmake restaurant_interfaces
mkdir -p restaurant_interfaces/srv
cp "$REPO/lesson05_services/TakeOrder.srv" restaurant_interfaces/srv/
cp "$REPO/lesson05_services/CMakeLists.txt" restaurant_interfaces/
cp "$REPO/lesson05_services/package.xml" restaurant_interfaces/
```

TakeOrder.srv contains string item_name and int32 quantity in the request, then --- followed by bool accepted and string message in the response.

The lesson05 package.xml is ONLY for restaurant_interfaces, not the Python package.

## Install the lecture nodes

```bash
cp "$REPO/lesson05_services/restaurant_server.py" ~/ros2_ws/src/test2_py_pkg/test2_py_pkg/
cp "$REPO/lesson05_services/restaurant_client.py" ~/ros2_ws/src/test2_py_pkg/test2_py_pkg/
cp "$REPO/lesson05_services/setup.py" ~/ros2_ws/src/test2_py_pkg/
```

In test2_py_pkg/package.xml retain the ament_python build type and add dependencies if absent:

```xml
<exec_depend>rclpy</exec_depend>
<exec_depend>std_msgs</exec_depend>
<depend>restaurant_interfaces</depend>
<exec_depend>launch</exec_depend>
<exec_depend>launch_ros</exec_depend>
```

```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install --packages-up-to test2_py_pkg
source install/setup.bash
ros2 interface show restaurant_interfaces/srv/TakeOrder
ros2 run test2_py_pkg restaurant_server
```

In separately sourced terminals start chef BEFORE sending requests, then run:

```bash
ros2 run test2_py_pkg order_client burger 2
ros2 service call /take_order restaurant_interfaces/srv/TakeOrder "{item_name: burger, quantity: 2}"
```

Accepted orders are published on /orders for the chef. Unknown items and quantities outside 1..max_quantity are rejected without publication. The lecture menu is burger and salad. The restaurant_client executable remains a compatibility alias; use order_client in new materials.

## Actions

For long-running work needing feedback and cancellation, use an action rather than stretching a short service callback. An action definition contains goal, result and feedback sections separated by ---:

```text
# CookOrder.action
string item_name
---
bool done
---
float32 percent_complete
```

Actions are conceptual in this workshop, not a required implementation. Follow the official Humble action tutorial for an extension: https://docs.ros.org/en/humble/Tutorials/Intermediate/Writing-an-Action-Server-Client/Py.html
