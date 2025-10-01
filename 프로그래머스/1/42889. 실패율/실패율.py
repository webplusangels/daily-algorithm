def solution(N, stages):
    from collections import Counter
    counts = Counter(stages)
    acc = counts.get(N+1, 0)
    ratio = {}
    for i in range(N, 0, -1):
        # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        not_cleared = counts.get(i, 0)
        # 스테이지에 도달한 플레이어 수
        acc += not_cleared
        if acc:
            ratio[i] = not_cleared/acc
        else:
            ratio[i] = 0

    std = sorted(ratio.items(), key=lambda x: (-x[1], x[0]))
    return [x[0] for x in std]