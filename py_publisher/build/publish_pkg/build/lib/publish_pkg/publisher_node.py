#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random


                    
class PublisherNode(Node): 
    def __init__(self):
        super().__init__("publisher_node") 

        self.publisher_ = self.create_publisher(Int32, "slider_topic", 10)
        self.timer_ = self.create_timer(0.5, self.publish_num)
        self.get_logger().info("Publisher has been started.")


    def publish_num(self):
        random_int = random.randint(1, 100)
        msg = Int32()
        msg.data = random_int
        self.publisher_.publish(msg)





def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode() 
    rclpy.spin(node)
    node.cap.release() 
    rclpy.shutdown()


if __name__ == "__main__":
    main()
