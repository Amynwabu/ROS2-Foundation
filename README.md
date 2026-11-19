# ROS2 Foundation - Teaching Materials

Teaching materials: Target environment: ROS 2 Humble on Ubuntu 22.04, with Python and Linux terminal familiarity.

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

## Install on a Linux server or virtual machine (step by step)

Use **Ubuntu 22.04 LTS (Jammy), 64-bit**. ROS 2 Humble's apt packages are built for this release. Give the machine at least 2 CPU cores, 4 GB RAM (8 GB for graphical tools) and 20 GB disk. This works the same on a cloud server (AWS, Azure, DigitalOcean), a VirtualBox/VMware/Hyper-V VM, or a WSL2 Ubuntu 22.04 install.

**1. Update the system and set the locale**

```bash
sudo apt update && sudo apt install -y locales software-properties-common curl git
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

**2. Enable the Ubuntu Universe repository**

```bash
sudo add-apt-repository -y universe
```

**3. Add the ROS 2 apt repository**

```bash
sudo apt update && sudo apt install -y curl
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo $VERSION_CODENAME)_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb
```

If that fails, follow the current instructions in the [official ROS 2 Humble install guide](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html), which is the authority for this step.

**4. Install ROS 2 Humble and the build tools**

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y ros-humble-desktop python3-colcon-common-extensions python3-rosdep python3-argcomplete python3-pip
```

On a headless server with no screen, `ros-humble-ros-base` is smaller, but then `rqt_graph` is not available.

**5. Source ROS in every terminal**

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

**6. Initialise rosdep**

```bash
sudo rosdep init
rosdep update
```

If `rosdep init` says the file already exists, carry on.

**7. Create the workspace and get the lessons**

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/Amynwabu/ROS2-Foundation.git
```

Follow the lesson folders to copy or create packages in `~/ros2_ws/src`, then build from `~/ros2_ws` as shown under "Build and troubleshoot".

**8. Check the install**

```bash
echo $ROS_DISTRO                 # humble
ros2 run demo_nodes_cpp talker   # terminal 1: prints "Publishing: 'Hello World: 1'"
ros2 run demo_nodes_py listener  # terminal 2: prints "I heard: [Hello World: 1]"
```

Stop each with Ctrl+C. If `ros2: command not found`, run `source /opt/ros/humble/setup.bash` and check step 5.

**9. (Optional) Graphical tools on a server with no desktop**

```bash
sudo apt install -y xfce4 xfce4-goodies tigervnc-standalone-vnc-server
vncserver -localhost yes -geometry 1600x900
```

Then connect with an SSH tunnel (`ssh -L 5901:localhost:5901 user@server`) and a VNC viewer on `localhost:5901`. Alternatively, use the Codespace option above, which already provides a browser desktop. Do not expose the VNC port to the internet.

**Several students on one server:** create one Linux user per student (`sudo adduser name`), and have each student run steps 5 to 7 in their own account. Set `export ROS_DOMAIN_ID=<unique number 0-101>` in each student's `~/.bashrc` so that their nodes do not see each other's topics.

**Newer Ubuntu releases:** Humble is not packaged for Ubuntu 24.04. Use 22.04, or run the Docker route below, which works on any Linux host:

```bash
docker run -it --rm osrf/ros:humble-desktop-full bash
```

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
