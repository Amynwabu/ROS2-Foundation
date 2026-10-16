# Lesson 06: Launch, parameters and debugging — slides 30–36

Complete lesson05 first. Set REPO to your clone path. Install launch files through setup.py data_files, not CMakeLists.txt: test2_py_pkg is an ament_python package. The CMakeLists.txt snippet in this lesson is only a contrast for ament_cmake packages.

```bash
export REPO="$HOME/ROS2-Foundation"
mkdir -p ~/ros2_ws/src/test2_py_pkg/launch
cp "$REPO/lesson06_launch_files/restaurant.launch.py" ~/ros2_ws/src/test2_py_pkg/launch/
cp "$REPO/lesson06_launch_files/setup.py" ~/ros2_ws/src/test2_py_pkg/
source /opt/ros/humble/setup.bash
cd ~/ros2_ws
colcon build --symlink-install --packages-up-to test2_py_pkg
source install/setup.bash
ros2 launch test2_py_pkg restaurant.launch.py
```

The launch starts chef and restaurant_server, setting max_quantity to 10. Do not run the earlier periodic waiter publisher at the same time: this lesson's orders come from accepted service requests. The old restaurant_system.launch.py filename is retained as a compatibility example with the same two nodes.

In separately sourced terminals:

```bash
ros2 node list
ros2 run test2_py_pkg order_client burger 2
ros2 param get /restaurant_server max_quantity
ros2 param set /restaurant_server max_quantity 8
ros2 run test2_py_pkg order_client burger 9
```

The first order should be accepted and logged by the chef. After lowering the limit to 8, quantity 9 should be rejected without publication. The server reads the parameter inside each request callback so runtime changes take effect.

## QoS exercise — slide 21

The lecture publisher and subscriber both use depth 10 with their default reliable/volatile policies. Inspect their actual endpoint settings:

```bash
ros2 topic info /orders --verbose
```

For an isolated mismatch demonstration, run these commands in two terminals with the same sourced environment:

```bash
ros2 topic pub /qos_demo std_msgs/msg/String "{data: hello}" --rate 1 --qos-reliability best_effort
ros2 topic echo /qos_demo std_msgs/msg/String --qos-reliability reliable
```

Expect incompatible reliability and no received samples. Stop echo and repeat it with --qos-reliability best_effort; messages should arrive. Compatibility, not exact equality of every setting, is required. Keep reliable delivery for the restaurant exercise; use a sensor-data profile where losing old measurements is preferable to waiting for retransmission.

## Debugging and verification

```bash
ros2 topic echo /orders
ros2 topic info /orders --verbose
ros2 service list
ros2 service type /take_order
ros2 service call /take_order restaurant_interfaces/srv/TakeOrder "{item_name: salad, quantity: 1}"
rqt_graph
ros2 doctor
```

Start echo and chef before sending a one-shot order: volatile topics do not replay old samples. There is no 1 Hz stream in this service-driven system; use topic hz with the earlier periodic waiter example instead. Accepted requests should produce one order message; rejected requests should produce none.

If a package is missing, source the overlay in that terminal. If an executable is missing, check console_scripts and rebuild. If messages are missing, compare topic names, message types, QoS, ROS_DOMAIN_ID and network configuration. Stop duplicate servers before testing.

Runtime verification on ROS 2 Humble remains required; these examples are not a claim of an executed integration test.
