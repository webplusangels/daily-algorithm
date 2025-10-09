from collections import defaultdict
import heapq

def solution(info, edges):
    tree = defaultdict(set)
    for frm, to in edges:
        tree[frm].add(to)
        
    # print(tree) {0: [1, 8], 1: [2, 4], 8: [7, 9], 9: [10, 11], 4: [3, 6], 6: [5]})
    # 0의 최대값은 1 -> 1의 최대값은 2 8의 최대값은 1 -> 
    # 7의 최대값은 3 9의 최대값은 3 1의 최대값도 3으로 업데이트
    # 노드에 도달했을 시점의 최대값을 구해야 함. 업데이트의 기준은 뭐지?
    # 그럼 순회를 여러 번 해야 하나?
    # 트리를 dfs를 해서 가장 위의 트리에는 최대값을 줘야 함
    m = 0
    def dfs(sheep, wolf, next_nodes):
        nonlocal m
        # print(sheep, wolf, next_nodes, m)
        
        if sheep > m:
            m = sheep
        
        for node in next_nodes:            
            if info[node] == 0:
                sheep += 1
                nxt_nods = (next_nodes - {node}) | tree[node]
                dfs(sheep, wolf, nxt_nods)
                sheep -= 1
                
            elif sheep-1 > wolf:
                wolf += 1
                nxt_nods = (next_nodes - {node}) | tree[node]
                dfs(sheep, wolf, nxt_nods)
                wolf -= 1
                
    dfs(1, 0, tree[0])
    
    return m