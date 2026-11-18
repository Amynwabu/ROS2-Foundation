#!/usr/bin/env bash
# Runs once when the dev container / Codespace is created.
set -uo pipefail

sudo apt-get update
sudo apt-get install -y python3-pip python3-colcon-common-extensions python3-rosdep python3-argcomplete

# rosdep: init may already have been done in the base image
sudo rosdep init || true
rosdep update || echo "rosdep update failed (offline?) - run it later"

# Every new terminal gets ROS 2 sourced (once)
LINE='source /opt/ros/humble/setup.bash'
grep -qxF "$LINE" ~/.bashrc || echo "$LINE" >> ~/.bashrc

# Workspace used by the lessons (lesson 01)
mkdir -p ~/ros2_ws/src
