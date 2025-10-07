import sys
input = lambda: sys.stdin.readline().rstrip()

string = input()

only_plus = string.split('-')
# print(only_plus)

tmp_answer = []

for plus in only_plus:
    to_plus = plus.split('+')
    tmp_answer.append(sum(list(map(int, to_plus))))

answer = tmp_answer[0]
for tmp in tmp_answer[1:]:
    answer -= tmp

print(answer)