# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        result = []
        flag = True

        while queue:
            level_size = len(queue)
            nodes = []

            for i in range(level_size):
                curr = queue.popleft()
                nodes.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            if not flag:
                nodes.reverse()

            result.append(nodes)
            flag = not flag

        return result 