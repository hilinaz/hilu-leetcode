"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        current =[]
        if root:
            current.append(root)
        ans=[]
        while current:
            next_node = []
            for node in current:
                for child in node.children:
                    if child:
                        next_node.append(child)


            ans.append([c.val for c in current])
            current = next_node[:]
        return ans 
    
            

            



        
        