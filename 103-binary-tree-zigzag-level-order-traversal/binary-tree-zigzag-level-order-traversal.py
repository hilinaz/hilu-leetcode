# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        que = deque()
        que.append(root)
        level = 0
        ans = []
        if not root:
            return []
        while que:
            path = []
            for i in range(len(que)):
                node = que.popleft()
                if node:
                    path.append(node.val)
 
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
        
            if level % 2 != 0:
                path.reverse()

            ans.append(path)
            level += 1

        return ans