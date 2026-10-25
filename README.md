# ROS Noetic — Publish/Subscribe Exercises

An introductory ROS 1 / ROS Noetic workspace exploring how independent nodes communicate through topics. The project contains a `catkin` package with several Python nodes and a launch file.

## What's inside

```text
messaging in ros/
└── algo_baru/
    ├── CMakeLists.txt
    ├── package.xml
    ├── kominfo.launch
    └── src/
        ├── budi01_gaming.py
        ├── smartguys_provider_node.py
        └── xs_provider_node.py
```

The launch configuration starts the three Python nodes together.

## Prerequisites

A compatible **ROS 1 Noetic** installation, typically Ubuntu 20.04, with `catkin` and Python 3. ROS 1 Noetic is an end-of-life ROS distribution, so use a suitable isolated learning environment.

## Build and explore

Place the package into a catkin workspace:

```bash
mkdir -p ~/catkin_ws/src
cp -r "messaging in ros/algo_baru" ~/catkin_ws/src/
cd ~/catkin_ws
catkin_make
source devel/setup.bash
roslaunch algo_baru kominfo.launch
```

The source folder names include spaces, so keep shell paths quoted. Ensure the Python node scripts are executable and their interpreter paths match your environment.

## Learning outcomes

ROS package structure, launching multiple nodes, topic messaging, and observing node communication in a distributed robot software environment.

*Educational sample, not a maintained ROS production package.*
