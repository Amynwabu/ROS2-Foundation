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

## Run it in the browser (no installation)

**GitHub Codespaces:** on the repository page choose Code, then Codespaces, then Create codespace on main. The first build takes a few minutes. Then:

```bash
echo $ROS_DISTRO        # should print: humble
ls ~/ros2_ws/src        # empty workspace, ready for lesson 01
```

- The terminal in the browser is all you need for lessons 01-07.
- For graphical tools such as `rqt_graph`, open the forwarded port 6080 (Ports tab) and use the password `ros2`.
- Stop the codespace when you finish; idle time counts against the free monthly allowance.
- Teachers: make this repository a template so each student gets their own copy.

**Windows without Codespaces:** run `wsl --install -d Ubuntu-22.04` in PowerShell, then install `ros-humble-desktop` with apt as in the official ROS 2 Humble guide.

**VS Code with Docker:** open the folder and choose Reopen in Container (uses `.devcontainer/`).

## Build and troubleshoot

Build from ~/ros2_ws, never src. Source /opt/ros/humble/setup.bash and the workspace overlay in every terminal. After creating the interface and lecture packages, use:

```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install --packages-up-to test2_py_pkg
source install/setup.bash
```

If a build after switching between plain and `--symlink-install` fails with a missing-file error, rebuild, or delete that package's `build/` and `install/` folders and build again. Check entry points for 'No executable found'; check topic type, name and QoS for missing messages. See lesson06_launch_files for verification commands.

The lesson 01-07 instructions were run end to end on ROS 2 Humble (RoboStack build, Python 3.11) on 17 November 2026: build, run, topics, services, launch, parameters, QoS exercise and the lesson 07 success test. Please still repeat them once on Ubuntu 22.04 with the apt Humble packages before teaching, and run `rosdep install` as shown above (not part of that test).

## Contributing and licence

Open an issue or pull request for feedback. See LICENSE for the repository licence.
