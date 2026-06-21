class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def remove(self, node):
        pre, nex = node.prev, node.next
        pre.next = nex
        nex.prev = pre
    
    def insert(self, node):
        rightPre = self.right.prev
        rightPre.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = rightPre

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        while len(self.cache) > self.cap:
            nodeToRemove = self.left.next
            third = self.left.next.next
            self.left.next = third
            third.prev = self.left
            del self.cache[nodeToRemove.key]
        
