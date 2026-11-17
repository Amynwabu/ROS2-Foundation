# Lesson 02: ROS2 Packages and Nodes

## Learning Objectives

After completing this lesson, you should be able to:

- Understand what ROS2 packages are and their role in organizing ROS2 projects
- Create and structure a new ROS2 Python package
- Create a simple ROS2 node and run it
- Understand the basic node lifecycle: initialization, spinning, and shutdown
- Comprehend the relationship between packages, nodes, and the workspace

## Key Concepts

### What is a ROS2 Package?

A **package** is a container that holds everything your ROS2 program needs:
- Source code (scripts and source files)
- Dependency information
- Configuration files
- Launch files
- Unit tests

Packages provide a standardized way to organize and share ROS2 code.

### What is a ROS2 Node?

A **node** is a single, specialized process (program) that performs one specific task.

**Real-World Analogy - Restaurant:**
- **Node**: One specific staff member (Chef, Waiter, Manager)
- **Package**: The restaurant itself (contains all staff, equipment, recipes)
- **Graph**: How they communicate with each other

**Key Characteristics:**
- **Independence**: If one node crashes, others continue running
- **Specialization**: Each node handles one specific task
- **Communication**: Nodes communicate via topics, services, and actions

## Creating a ROS2 Package

### Step 1: Create a New Package

```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python test2_py_pkg
cd ~/ros2_ws
colcon build --packages-select test2_py_pkg
source install/setup.bash
```

### Step 2: Verify Package Creation

```bash
ls src/test2_py_pkg
ros2 pkg list  # List all packages
```

## Package Structure

After creating a package, you'll see the following structure:

```
test2_py_pkg/
├── package.xml          # Package metadata and dependencies
├── setup.py             # Entry points for executables
├── setup.cfg            # Installation configuration
├── test2_py_pkg/        # Source directory for Python nodes
│   └── __init__.py      # Python package marker
├── test/                # Unit tests
│   └── test_*.py        # Test files
└── resource/            # Package marker
    └── test2_py_pkg
```

### Key Files Explained

**package.xml**: Package metadata and dependencies
```xml
<?xml version="1.0"?>
<?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="3">
  <name>test2_py_pkg</name>
  <version>0.0.1</version>
  <description>My first ROS2 package</description>
  <maintainer email="your.email@example.com">Your Name</maintainer>
  <license>Apache License 2.0</license>
  <depend>rclpy</depend>
  <depend>std_msgs</depend>
</package>
```

**setup.py**: Defines entry points for executables
```python
from setuptools import find_packages, setup

package_name = 'test2_py_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='My first ROS2 package',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'my_first_node=test2_py_pkg.mynode:main',
        ],
    },
)
```

## Creating Your First Node

### What is a Node?

A node is a Python program that:
1. Imports ROS2 libraries
2. Defines a class inheriting from `Node`
3. Initializes itself with a name
4. Implements callbacks or timers for tasks
5. Runs in a loop (spins) to process events

### Node Lifecycle

1. **Initialization**: `rclpy.init()` - Sets up ROS2 infrastructure
2. **Node Creation**: Create an instance of your Node class
3. **Spinning**: `rclpy.spin()` - Keeps node running and processes callbacks
4. **Shutdown**: `rclpy.shutdown()` - Cleanup on exit

### Creating MyFirstNode (mynode.py)

Step 1: Create the Python File
```
Navigate to: cd ~/ros2_ws/src/test2_py_pkg/test2_py_pkg/

Create a new file: mynode.py

```

The complete code is in this folder: `lesson02_packages_nodes/mynode.py` (a matching `setup.py` is alongside it).


## Registering Your Node as an Entry Point

For ROS2 to find and run your node, you must register it in `setup.py`.

1. Open `setup.py`
2. Find the `entry_points` section
3. Add your node to `console_scripts`:

```python
entry_points={
    'console_scripts': [
        'my_first_node=test2_py_pkg.mynode:main',
    ],
},
```

**Format**: `'executable_name=package_name.module_name:function_name'`

## Building and Running Your Node

### Step 1: Build the Workspace

```bash
cd ~/ros2_ws
colcon build --packages-select test2_py_pkg
```

### Step 2: Source the Install Space

```bash
source install/setup.bash
```

⚠️ **Important**: Source the workspace in EVERY new terminal before running nodes!

### Step 3: Run Your Node

```bash
ros2 run test2_py_pkg my_first_node
```

### Expected Output

```
[INFO] [1234567890.123456789] [my_first_node]: Hello from My First Node!
[INFO] [1234567890.223456789] [my_first_node]: Counter: 1
[INFO] [1234567890.323456789] [my_first_node]: Counter: 2
[INFO] [1234567890.423456789] [my_first_node]: Counter: 3
...
```

### Stopping the Node

Press `Ctrl+C` to stop the node gracefully.

## Essential ROS2 Commands

### Package Management

```bash
# List all packages
ros2 pkg list

# Get information about a package
ros2 pkg prefix test2_py_pkg

# Create a new package
ros2 pkg create --build-type ament_python my_package
```

### Node Management

```bash
# List all running nodes
ros2 node list

# Get information about a node
ros2 node info /my_first_node

# Run a node
ros2 run package_name node_name
```

### Build Commands

```bash
# Build entire workspace
colcon build

# Build specific package
colcon build --packages-select test2_py_pkg

# Build with detailed output
colcon build --symlink-install --event-handlers console_direct+
```

## Understanding the Workspace Structure

```
ros2_ws/
├── src/                    # Source code directory
│   ├── test2_py_pkg/       # Your package
│   │   ├── test2_py_pkg/   # Python package
│   │   │   ├── __init__.py
│   │   │   └── mynode.py   # Your node
│   │   ├── setup.py        # Entry points
│   │   ├── setup.cfg
│   │   └── package.xml     # Dependencies
│   └── ... (other packages)
├── build/                  # Compiled binaries (generated)
├── install/                # Installed packages (generated)
├── log/                    # Build logs (generated)
└── .colcon_defaults        # Build configuration
```

**Important Directories**:
- **src/**: Where you write your code
- **build/**: Intermediate build files
- **install/**: Final installed executables and libraries
- **log/**: Build and execution logs

## Common Issues and Debugging

### Issue: "ros2 command not found"

```bash
# Solution: Source the ROS2 installation
source /opt/ros/humble/setup.bash

# Or add to ~/.bashrc for automatic activation
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### Issue: "Package not found"

```bash
# Solution: Build and source your workspace
cd ~/ros2_ws
colcon build --packages-select test2_py_pkg
source install/setup.bash
```

### Issue: Node not found in ros2 run

Check that:
1. The package is built: `colcon build --packages-select test2_py_pkg`
2. Workspace is sourced: `source install/setup.bash`
3. Entry point is registered in `setup.py`
4. Node file exists and is executable

### Debugging Node Output

```bash
# Run with verbose logging
ros2 run test2_py_pkg my_first_node --ros-args --log-level DEBUG

# List all nodes and their topics
ros2 node list
ros2 node info /my_first_node
```

## Practice Exercise

### Create a Counter Node

1. Create a new file: `src/test2_py_pkg/test2_py_pkg/counter_node.py`
2. Implement a node that:
   - Increments a counter every 2 seconds
   - Logs messages like "Counter: 1", "Counter: 2", etc.
   - Counts to 10 and then stops
3. Register it in `setup.py` as `'counter=test2_py_pkg.counter_node:main'`
4. Build and run it

## Summary

- **Packages** organize ROS2 code and dependencies
- **Nodes** are individual processes performing specific tasks
- Packages contain nodes, configuration files, and dependencies
- Nodes communicate through topics, services, and actions
- The ROS2 workspace (src → build → install) standardizes development
- Always source your workspace before running nodes
- Entry points in `setup.py` register executable nodes

## Next Lesson

In the next lesson, we'll explore **ROS2 Topics** and implement the **Publisher-Subscriber pattern** with practical examples like the Waiter and Chef nodes.
