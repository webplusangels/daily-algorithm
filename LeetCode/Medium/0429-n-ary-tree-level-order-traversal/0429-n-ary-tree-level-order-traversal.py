from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # level별로 node들을 리스트에 넣어 출력
        # deque로 앞에 넣어놓고 하나씩 pop?
        answer = []
        if not root:
            return []
        tree = deque([root])
        while tree:
            tmp = []
            for _ in range(len(tree)):
                node = tree.popleft()
                tmp.append(node.val)
                tree.extend(node.children)
            answer.append(tmp)
        
        return answer