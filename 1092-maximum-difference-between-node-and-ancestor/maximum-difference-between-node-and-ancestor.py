# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        def helper (node ,mini,maxi):
            if node==None:
                return maxi-mini
            maxi=max(maxi,node.val)
            mini=min(mini,node.val)
            left=helper(node.left,mini,maxi)
            right= helper(node.right,mini,maxi)
            return(max(left,right))
            
        return helper(root,float('inf'),float('-inf'))
       
        