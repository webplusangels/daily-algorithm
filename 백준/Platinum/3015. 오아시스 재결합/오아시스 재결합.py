import sys
input = sys.stdin.readline

N = int(input())
line = []

for _ in range(N):
    line.append(int(input()))
    
stack = []
answer = 0

for i in range(N):
    target = line[i]
    count = 1
    # (높이 - target, 사람 수 - count)
    
    # stack에서 현재 높이보다 작은 사람을 처리
    while stack and stack[-1][0] < target:
        s_height, s_count = stack.pop()
        answer += s_count
        
    # stack이 비었는지와, 높이가 같거나 큰 사람 확인 
    if not stack:
        stack.append((target, count))
    else:
        if stack[-1][0] == target:
            # 같은 높이 사람들의 쌍을 추가
            answer += stack[-1][1]
            count += stack[-1][1]
            stack.pop()
            
            # 그래도 stack에 남아있다면 한 쌍을 더 추가
            if stack:
                answer += 1
    
            stack.append((target, count))
        
        # 현재 높이보다 큰 사람
        else:
            # 내가 그 사람을 봄
            answer += 1
            stack.append((target, count))
            
print(answer)