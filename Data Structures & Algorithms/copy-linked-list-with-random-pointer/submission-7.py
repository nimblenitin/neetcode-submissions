"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}

        node = head
        while node:
            copy = Node(node.val)
            oldToNew[node] = copy
            node = node.next
        node = head
        while node:
            copy = oldToNew[node]
            nxt = node.next
            random = node.random
            copy.next = oldToNew[nxt]
            copy.random = oldToNew[random]
            node = node.next
        return oldToNew[head]

