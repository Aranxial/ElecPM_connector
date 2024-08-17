# Connector module

Download the package `connect` and place it in the `src` directory of your ROS workspace. Now run: ``ros2 launch connector connector_launch.py`` which will run the code `connect_read.py` which will find the models in the current gazebo world which starts with `connect_` and publishes the position (xyz) in the topic `connector_pos_list`.

I also tried to implement force on models in gazebo using some plugins, but cant actually get it working. The codes are in `code` directory of this package.
