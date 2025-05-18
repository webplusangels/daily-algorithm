import sys
input = sys.stdin.readline

def largest_rec(n, h_list):
    stack = []
    max_area = 0
    # [index, height]
    for i, height in enumerate(h_list):
        cur_index = i
        while stack and stack[-1][1] > height:
            s_i, s_h = stack.pop()
            width = i - s_i
            max_area = max(max_area, width*s_h)
            # pop한 막대의 width 만큼 왼쪽으로 확장
            cur_index = s_i
            
        stack.append([cur_index, height])
    
    # 스택에 남은 막대를 오른쪽 끝까지 확장
    for s_i, s_h in stack:
        max_area = max(max_area, (n-s_i)*s_h)
    
    return max_area

while True:
    inputs = input().strip()
    if '0' == inputs:
        break
    num_list = list(map(int, inputs.split()))    
    print(largest_rec(num_list[0], num_list[1:]))