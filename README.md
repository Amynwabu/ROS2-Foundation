# ROS2 Foundation - Teaching Materials

Teaching materials for MSc Applied AI students at Cranfield University. Target environment: ROS 2 Humble on Ubuntu 22.04, with Python and Linux terminal familiarity.

## Start here

```bash
git clone https://github.com/Amynwabu/ROS2-Foundation.git
source /opt/ros/humble/setup.bash
mkdir -p ~/ros2_ws/src
```

The lesson folders contain teaching snippets, not a single workspace to build recursively. Follow each lesson's instructions to create packages in ~/ros2_ws/src. Do not copy all lesson directories into src: several files are alternative versions of the same package configuration.

The existing ros2_ws.zip is a legacy snapshot and has NOT been synchronised or verified against ROS2v2.pptx. Use the source-based lesson instructions instead.

## Slide-to-lesson map

| Slides | Material |
| --- | --- |
| 5–10: environment, workspaces, packages | lesson01_environment_workspace; lesson02_packages_nodes |
| 11–14: nodes | lesson02_packages_nodes |
| 15–21: topics and QoS | lesson03_topics_publish_subscribe; lesson04_publisher_subscriber_nodes; lesson06_launch_files/README.md for QoS exercise |
| 22–29: services and actions | lesson05_services |
| 30–36: parameters, launch, debugging | lesson06_launch_files |
| 37: assignment | lesson07_smart_restaurant_system |

Use TEACHING_SCRIPT.md as supplementary introductory narration; the lesson05–07 instructions take precedence for service names, launch and assessment.

## Build and troubleshoot

Build from ~/ros2_ws, never src. Source /opt/ros/humble/setup.bash and the workspace overlay in every terminal. After creating the interface and lecture packages, use:

```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install --packages-up-to test2_py_pkg
source install/setup.bash
```

Check entry points for 'No executable found'; check topic type, name and QoS for missing messages. See lesson06_launch_files for verification commands.

These changes have not been runtime-tested in ROS 2. Complete the verification exercises on a Humble installation before teaching.

## Contributing and licence

Open an issue or pull request for feedback. See LICENSE for the repository licence.
