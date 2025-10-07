from collections import deque

def solution(places):
    SIZE = 5
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    
    def check(place):
        for i in range(SIZE):
            for j in range(SIZE):
                if place[i][j] == 'P':
                    q = [[(i, j), 0]]
                    vis = set([(i, j)])
                    while q:
                        coor, cnt = q.pop()
                        for n in range(4):
                            x, y = coor[0]+dx[n], coor[1]+dy[n]
                            if 0 <= x < SIZE and 0 <= y < SIZE and cnt < 2 and (x, y) not in vis: 
                                if place[x][y] == 'X': 
                                    continue;
                                elif place[x][y] == 'P': 
                                    return False;
                                elif place[x][y] == 'O':
                                    q.append([(x, y), cnt+1])
        else:
            return True
        
    result = []
    for place in places:
        result.append(int(check(place)))
        
    return result