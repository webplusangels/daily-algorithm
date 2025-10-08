def solution(key, lock):
    lock_size = len(lock)
    key_size = len(key)
    
    lock_hole = set()
    for i in range(lock_size):
        for j in range(lock_size):
            if lock[i][j] == 0:
                lock_hole.add((i, j))
    len_hole = len(lock_hole)
    if not len_hole:
        return True
    
    # 1,0->2,1 0,1-> 1,2 구멍을 다 메우고 hole이 아닌 곳에 put이 존재하지 않는다면 성공
    # hole_x - put_x = m, hole_y - put_y = n -> m, n만큼 평행이동 시킴
    # put만 확인해도 됨 -> 구멍 메우는지, 엉뚱한 곳을 채우지 않는지
    # 4번 회전시켜서 확인 -> 4*len(key_put)
    def rotate(key):
        rotated_put = [set() for _ in range(4)]
        for i in range(key_size):
            for j in range(key_size):
                if key[i][j] != 1:
                    continue
                    
                rotated_put[0].add((i, j))
                rotated_put[1].add((j, key_size-i-1))
                rotated_put[2].add((key_size-i-1, key_size-j-1))
                rotated_put[3].add((key_size-j-1, i))
                
        return rotated_put

    r_put = rotate(key)
    for keys in r_put: # 4개
        for hole in lock_hole:
            for k in keys: 
                # key 하나 씩 대보는 중
                m = hole[0] - k[0]
                n = hole[1] - k[1]
                cnt = len_hole # 구멍을 다 채울 수 있는가?
                for k_ in keys: 
                    where = (k_[0]+m, k_[1]+n)
                    if 0 <= where[0] < lock_size and 0 <= where[1] < lock_size:
                        if where in lock_hole:
                            # print(f'{where=} {hole=} {k=} {keys=}')
                            cnt -= 1
                        else:
                            # print(f'{where=} {hole=} {k=} {keys=} break!')
                            break
                    # else:
                        # print(f'{where=} {hole=} {k=} {keys=} not in')
                else:
                    if cnt == 0:
                        return True
    
    return False
                    