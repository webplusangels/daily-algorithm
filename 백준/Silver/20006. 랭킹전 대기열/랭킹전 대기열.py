import sys
input = lambda: sys.stdin.readline().rstrip()

p, m = map(int, input().split())
players = [input().split() for _ in range(p)]

matches = []
matches_info = []
for player in players:
    level, name = int(player[0]), player[1]
    if not matches:
        matches.append([level, 1])
        matches_info.append([(level, name)])

    else:
        for i, match in enumerate(matches):
            limit, now = match
            if now >= m:
                continue
            if limit-10 <= level <= limit+10:
                matches[i][1] += 1
                matches_info[i].append((level, name))
                break
        else: # 방이 없다면
            matches.append([level, 1])
            matches_info.append([(level, name)])

for i in range(len(matches)):
    matches_info[i].sort(key=lambda x: x[1])
    if matches[i][1] < m:
        print("Waiting!")
        for info in matches_info[i]:
            print(*info)
    else:
        print("Started!")
        for info in matches_info[i]:
            print(*info)