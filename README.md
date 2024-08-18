# Connector module

Download the package `connect` and place it in the `src` directory of your ROS workspace. Now run: ``ros2 launch connector connector_launch.py`` which will run the code `connect_read.py` which will find the models in the current gazebo world which starts with `connect_` and publishes the position (xyz) in the topic `connector_pos_list`.

To apply force on connector models, we can use the ignition command: `ign topic -t "/world/<WORLD_NAME>/wrench" -m ignition.msgs.EntityWrench -p "entity: {name: 'MODEL_NAME::LINK_NAME', type: LINK}, wrench: {force: {x: <Fx>, y: <Fy>, z: <Fz>}, torque: {x: 0.0, y: 0.0, z: 0.0}}"`. So, I made a node which uses this command to apply force on the connector models. The codes are in `code` directory of this package.
