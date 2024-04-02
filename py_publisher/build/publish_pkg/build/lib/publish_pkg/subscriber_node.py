#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SubscriberNode(Node): 
    def __init__(self):
        super().__init__("shapes") 
        self.subscriber_ = self.create_subscription(
            String, "slider_topic", self.callback_triangle, 10)
        self.get_logger().info("Infos are getting received.")

    def callback_triangle(self, msg):
        self.get_logger().info("num: " + msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
