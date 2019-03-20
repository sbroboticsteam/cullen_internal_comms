import json
import time
import numpy as np
from Node import Node

node = Node("test_node.json")


while True:    
    data = np.array([2, 3, 1, 0])
    node.send_nparray("inputs", data, copy=False)
    print("Message Sent: ")
    print(data)
    data = node.recv_nparray("inputs")
    print("Message Received: ")
    print(data)
