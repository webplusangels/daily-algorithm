import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, i, x, y):
        self.i = i
        self.x = x
        self.y = y
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node):
        self.root = node

    def insert(self, node):
        cur = self.root
        
        while True:
            if node.x < cur.x:
                if cur.left is None:
                    cur.left = node
                    break
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    break
                else:
                    cur = cur.right
                    
def solution(nodeinfo):
    # 전위순회 루트 왼 오
    # 후위순회 왼 오 루트
    
    nodes = []
    for i, node in enumerate(nodeinfo):
        nodes.append(Node(i+1, node[0], node[1]))
    
    nodes.sort(key=lambda x: (-x.y, x.x))
    
    tree = Tree(nodes[0])
    for i in range(1, len(nodes)):
        tree.insert(nodes[i])
    
    preOrder = []
    def preorder(node):
        if node is None:
            return
        
        preOrder.append(node.i)
        preorder(node.left)
        preorder(node.right)
    
    postOrder = []
    def postorder(node):
        if node is None:
            return 
        
        postorder(node.left)
        postorder(node.right)
        postOrder.append(node.i)
    
    preorder(tree.root)
    postorder(tree.root)
    
    return [preOrder, postOrder]