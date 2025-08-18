import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ns = [input() for _ in range(N)]

def sorting(x):
    def digitsum():
        answer = 0
        for s in x:    
            if s.isdigit():
                answer += int(s)
        return answer
    
    return (len(x), digitsum(), x)

ns.sort(key=sorting)

print(*ns, sep='\n')