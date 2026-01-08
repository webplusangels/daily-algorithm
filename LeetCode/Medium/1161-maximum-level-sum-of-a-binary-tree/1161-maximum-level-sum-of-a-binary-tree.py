from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        sums = []
        while dq:
            s = 0
            for _ in range(len(dq)):
                node = dq.popleft()
                s += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            sums.append(s)
        
        print(sums)
        idx = sums.index(max(sums)) + 1
        return idx