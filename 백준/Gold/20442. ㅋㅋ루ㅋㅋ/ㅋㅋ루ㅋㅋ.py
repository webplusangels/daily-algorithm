import sys
input = lambda: sys.stdin.readline().rstrip()

# R로만 이루어진 문자열 -> ㅋㅋ루ㅋㅋ
# ㅋㅋ루ㅋㅋ 양 끝에 K를 하나씩 붙인 문자열 -> ㅋㅋ루ㅋㅋ
string = input()
r_k_counts = []
total_k = 0

for s in string:
    if s == 'K':
        total_k += 1
    elif s == 'R':
        r_k_counts.append(total_k)

if not r_k_counts:
    print(0)
    exit()

left = 0
right = len(r_k_counts) - 1
max_len = 0

while left <= right:
    r_num = right - left + 1
    
    lk = r_k_counts[left]
    rk = total_k - r_k_counts[right]
    
    # 길이 공식
    current_len = r_num + 2 * min(lk, rk)
    max_len = max(max_len, current_len)
    
    if lk < rk:
        left += 1
    else:
        right -= 1

print(max_len)