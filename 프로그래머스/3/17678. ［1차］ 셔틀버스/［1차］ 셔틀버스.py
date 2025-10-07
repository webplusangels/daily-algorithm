from collections import deque

def solution(n, t, m, timetable):
    # timetable 전처리
    times = []
    for time in timetable:
        hour, minute = map(int, time.split(':'))
        minutes = 60*hour + minute
        times.append(minutes)
    times.sort(reverse=True)
    
    buses = [9*60+n*t for n in range(n)]
    last_one = 0
    last_bus = False
    for bus in buses:
        i = 0
        while times and times[-1] <= bus and i < m:
            last_one = times.pop()
            i += 1
        if i == m:
            last_bus = False
        else:
            last_bus = True
    
    # print(last_one)
    # print(last_bus)
    # 적어도 막차에 탄 마지막 사람들보다 빨리와야 함
    # last_one이 0이거나 last_bus가 가능하면 막차에 타면 되고
    
    if last_bus:
        h, m = divmod(buses[-1], 60)
        return f'{h:02}:{m:02}'
    else:
        h, m = divmod(last_one-1, 60)
        return f'{h:02}:{m:02}'