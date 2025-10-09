class Node:
    def __init__(self, num):
        self.state = 'O'
        self.num = num
        self.next = None
        self.prev = None

def solution(n, k, cmd):
    del_stack = []
    table = [Node(i) for i in range(n)]
    
    for node in table:
        if node.num != 0:
            node.prev = table[node.num-1]
        
        if node.num != n-1:
            node.next = table[node.num+1]
            
    p_node = table[k]
    for cc in cmd:
        c = cc.split()
        i = 0
        
        if c[0] == 'D':
            for _ in range(int(c[1])):
                p_node = p_node.next
        
        elif c[0] == 'U':
            for _ in range(int(c[1])):
                p_node = p_node.prev
        
        elif c[0] == 'C':
            p_node.state = 'X'
            del_stack.append(p_node)
            if p_node.next and p_node.prev:
                p_node.prev.next = p_node.next
                p_node.next.prev = p_node.prev
                p_node = p_node.next
            elif not p_node.next:
                p_node.prev.next = None
                p_node = p_node.prev
            elif not p_node.prev:
                p_node.next.prev = None
                p_node = p_node.next
            
        elif c[0] == 'Z':
            recover = del_stack.pop()
            recover.state = 'O'
            if recover.next and recover.prev:
                recover.prev.next = recover
                recover.next.prev = recover
            elif not recover.next:
                recover.prev.next = recover
            elif not recover.prev:
                recover.next.prev = recover
    
        # print([t.state for t in table])
        # print(cc ,p_node.num)
    
    return ''.join([t.state for t in table])