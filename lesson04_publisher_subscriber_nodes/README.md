# Publisher & Subscriber Nodes



## Real-World Analogy: Restaurant Order System

```
Waiter (Publisher)              Topic (/orders)              Chef (Subscriber)
    |                                                              |
    +---> announces order "Order #1: Burger" --->
    |                                                    listens & receives
    +---> announces order "Order #2: Burger" --->
    |                                                    starts cooking
    +---> announces order "Order #3: Burger" --->
```

## Key Concepts

### Publisher Node (Waiter)
- **Role**: Sends messages to a topic
- **Characteristics**:
  - Doesn't care who receives the message
  - Publishes at regular intervals (using timers)
  - Asynchronous - doesn't wait for subscribers
  - Can have multiple publishers on same topic

### Subscriber Node (Chef)
- **Role**: Receives messages from a topic
- **Characteristics**:
  - Listens passively for new messages
  - Uses callback functions to process messages
  - Can have multiple subscribers on same topic
  - Asynchronous - processes messages as they arrive

### Communication Pattern
- **Asynchronous**: Publisher doesn't wait for subscriber
- **Decoupled**: Nodes don't need to know about each other
- **Many-to-Many**: Multiple publishers and subscribers
- **Continuous**: Ideal for streaming data (sensors, cameras)

## Implementation Guide

### Step 1: Publisher Node (waiter.py)

```
Navigate to: cd ~/ros2_ws/src/test2_py_pkg/test2_py_pkg

Create file: waiter.py
```

### Step 2: Subscriber Node (chef.py)

```
Navigate to: cd ~/ros2_ws/src/test2_py_pkg/test2_py_pkg

Create file: chef.py
```

## Building and Running

### Step 1: Navigate to your workspace
```bash
cd ~/ros2_ws
```

### Step 2: Source the environment
```bash
source /opt/ros/humble/setup.bash
```

### Step 3: Build your package
```bash
colcon build --packages-select test2_py_pkg
source install/setup.bash
```

### Step 4: Run the Publisher (Terminal 1)
```bash
ros2 run test2_py_pkg waiter
```

Expected output:
```
[INFO] [waiter]: Waiter node started!
[INFO] [waiter]: Announcing: Order #1: Burger
[INFO] [waiter]: Announcing: Order #2: Burger
[INFO] [waiter]: Announcing: Order #3: Burger
...
```

Press `Ctrl+C` to stop; the node shuts down quietly.

### Step 5: Run the Subscriber (Terminal 2)
```bash
ros2 run test2_py_pkg chef
```

Expected output:
```
[INFO] [chef]: Chef node started! Listening for orders...
[INFO] [chef]: Received order: Order #1: Burger
[INFO] [chef]: Starting to cook...
[INFO] [chef]: Received order: Order #2: Burger
[INFO] [chef]: Starting to cook...
...
```

## Debugging Topic Communication

### List all active topics
```bash
ros2 topic list
```

Output:
```
/orders
/parameter_events
/rosout
```

### Echo topic messages in real-time
```bash
ros2 topic echo /orders
```

Output:
```
data: 'Order #1: Burger'
---
data: 'Order #2: Burger'
---
data: 'Order #3: Burger'
---
```

### Get topic information
```bash
ros2 topic info /orders
```

Output:
```
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1
```

### Get topic statistics
```bash
ros2 topic hz /orders
```

Output:
```
average rate: 1.000
	min: 1.001s max: 1.001s std dev: 0.000s window: 3
```

## Key Takeaways

✓ Publishers send messages without knowing if anyone is listening
✓ Subscribers listen passively and process messages asynchronously
✓ Multiple publishers and subscribers can use the same topic
✓ ROS2 automatically creates topics when first pub/sub is created
✓ Use command-line tools to debug topic communication

## Common Issues and Solutions

### Issue: No messages being received
**Solution**: 
- Check that both nodes are running
- Verify topic names match (case-sensitive)
- Use `ros2 topic list` to confirm topic exists

### Issue: Messages lagging or delayed
**Solution**:
- Check system resources (CPU, memory)
- Verify network connectivity (for remote robots)
- Check message queue size in publisher

### Issue: Node crashes immediately
**Solution**:
- Check for import errors
- Verify package is built and sourced
- Check node name doesn't conflict with existing nodes

## Next Steps

- Lesson 05: ROS2 Services (Request-Response pattern)
- Lesson 06: Launch Files (Start multiple nodes with one command)
- Lesson 07: Smart Restaurant System (Complete project)

## References

- [ROS2 Publisher Subscriber Documentation](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)
- [ROS2 Nodes Documentation](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)
