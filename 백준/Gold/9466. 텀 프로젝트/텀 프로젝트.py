from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())

def bfs(n, students):
    stud_dict = {n+1:students[n] for n in range(n)}
    # 0, 1의 상태
    vis = [0 for _ in range(n+1)]
    teamed = set()
    for key in stud_dict.keys():
        # print(f"{key=} {vis=}")
        if vis[key] == 0:
            temp_set = set([key])
            updated_key = stud_dict[key]
            while updated_key not in temp_set:
                if vis[updated_key]:
                    break
                temp_set.add(updated_key)
                updated_key = stud_dict[updated_key]

            if key == updated_key:
                teamed.update(temp_set)
            else:
                # print(temp_set)
                temp_set_ = set([updated_key])
                updated_key = stud_dict[updated_key]
                while updated_key not in temp_set_:
                    if vis[updated_key]:
                        break
                    temp_set_.add(updated_key)
                    updated_key = stud_dict[updated_key]
                else:
                    teamed.update(temp_set_)
            
            for i in temp_set:
                vis[i] = 1    
            # print(f"{teamed=}")
    print(n - len(teamed))
    

for _ in range(T):
    n = int(input())
    students = list(map(int, input().split()))
    bfs(n, students)
    