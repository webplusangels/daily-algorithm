def solution(cap, n, deliveries, pickups):
    """
    Args:
        cap: 트럭에 실을 수 있는 택배의 최대 개수
        n: 배달할 집의 개수
        deliveries: 각 집에 배달할 택배 개수
        pickups: 각 집에서 수거할 택배 개수
        
    Returns:
        트럭 하나로 배달과 수거를 마치고 돌아올 수 있는 최소 이동 거리
    """
    # 아마 투 포인터 (먼 곳에서 시작)
    to_d = to_p = n - 1
    distance = 0
    
    while to_d >= 0 or to_p >= 0:
        # 택배 대상
        while to_d >= 0 and not deliveries[to_d]:
            to_d -= 1
        
        go_with = back_with = cap
        
        stopped_d = to_d
        for i in range(to_d, -1, -1):
            tmp = min(deliveries[i], go_with)
            go_with -= tmp
            deliveries[i] -= tmp
            if not go_with:
                stopped_d = to_d
                break
        
        # 픽업 대상
        while to_p >= 0 and not pickups[to_p]:
            to_p -= 1
        
        stopped_p = to_p
        for i in range(to_p, -1, -1):
            tmp = min(pickups[i], back_with)
            back_with -= tmp
            pickups[i] -= tmp
            if not back_with:
                stopped_p = to_p
                break

        # 목적지는?
        where = max(stopped_d, stopped_p)
        
        # 왕복 거리 추가
        distance += where + 1
        
        to_d, to_p = stopped_d, stopped_p
        
        # print(f"{deliveries=}")
        # print(f"{pickups=}")
        # print(f"{to_d=} {to_p=} {distance=}")
        
    return 2*distance