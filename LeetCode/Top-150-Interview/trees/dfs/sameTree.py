# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        return self.dfs(p, q)
    
    def dfs(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        if q.val != p.val:
            return False  

        return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)      