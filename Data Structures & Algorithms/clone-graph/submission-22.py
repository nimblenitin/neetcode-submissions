"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        orgToCopy = {}

        def dfs(no):
            if not no:
                return
            
            if no in orgToCopy:
                return orgToCopy[no]
            
            copy = Node(no.val)
            orgToCopy[no] = copy 
            for nei in no.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        return dfs(node)