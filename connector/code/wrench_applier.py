import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Wrench, Vector3

class ForcePublisher(Node):
    def __init__(self):
        super().__init__('force_publisher')
        self.publisher = self.create_publisher(Wrench, '/apply_wrench', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Wrench()
        msg.force = Vector3(x=10.0, y=0.0, z=0.0)
        self.publisher.publish(msg)
        self.get_logger().info('Publishing Wrench: "%s"' % msg)

def main(args=None):
    rclpy.init(args=args)
    node = ForcePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

