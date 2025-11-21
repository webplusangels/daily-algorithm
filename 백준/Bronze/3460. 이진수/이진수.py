def solution(n):
    binary_n = bin(n)[2:][::-1]
    ones = []
    for i, char in enumerate(binary_n):
        if char == '1':
            ones.append(i)

    return ones

T = int(input())
for _ in range(T):
    N = int(input())
    print(*solution(N))