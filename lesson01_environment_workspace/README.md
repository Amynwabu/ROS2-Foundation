# Lesson 01: Environment & Workspace

This lesson covers ROS2 environment setup and workspace creation.

## Learning Objectives

- Verify ROS2 Humble installation
- Understand ROS2 workspace structure
- Create and configure a ROS2 workspace
- Source the workspace correctly

## Prerequisites

- Ubuntu 22.04 installed
- ROS2 Humble installed

## Step 1: Check ROS2 Installation

Verify your ROS2 installation is working:

```bash
# Check the ROS2 distribution (should print: humble)
echo $ROS_DISTRO

# Check available ROS2 commands
ros2 --help

# List installed ROS2 packages
ros2 pkg list
```

## Step 2: Create ROS2 Workspace

Create a workspace directory structure:

```bash
# Navigate to home directory
cd ~

# Create workspace with src folder
mkdir -p ~/ros2_ws/src

# Navigate to workspace
cd ~/ros2_ws
```

## Step 3: Build the Workspace

Build your empty workspace:

```bash
# Build the workspace
colcon build

# You should see install, build, and log directories created
```

## Step 4: Source the Workspace

Source the workspace to use it:

```bash
# Source the workspace
source ~/ros2_ws/install/setup.bash

# Add to .bashrc for automatic sourcing (optional)
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
```

## Your workspace structure

```
ros2_ws/                   # Your workspace root
├── src/                    # Where all your source code lives
│   └── test2_py_pkg/       # Your package (contains mynode.py, setup.py, etc.)
├── build/                  # Temporary files during compilation (auto-generated)
├── install/                # Final binaries and executables go here (auto-generated)
└── log/                    # Build logs for debugging (auto-generated)
 ```

## Verification

Verify your workspace is properly set up:

```bash
# Check ROS2 environment variables (ROS_DISTRO should be humble)
echo $ROS_DISTRO
echo $AMENT_PREFIX_PATH
```

## Troubleshooting

**Issue**: `colcon: command not found`
**Solution**: Install colcon
```bash
sudo apt install python3-colcon-common-extensions
```

**Issue**: Permission denied
**Solution**: Check directory permissions
```bash
ls -la ~/ros2_ws
```

## Next Steps

Now that your workspace is set up, proceed to Lesson 02 to create your first ROS2 package!
