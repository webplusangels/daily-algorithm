def solution(fees, records):
    import math
    
    times = {} # 주차장
    cal_time = {} # 시간 계산
    car_num = [] # 번호대로 정렬하기 위함

    for record in records:
        rcd = record.split()
        rcd[1] = int(rcd[1])
        
        # 1. 시간을 구한다 - 순회
        hour, minute = map(int, rcd[0].split(":"))
        if rcd[2] == 'IN':
            times[rcd[1]] = (hour, minute)
        else:
            h_in, m_in = times[rcd[1]]
            del times[rcd[1]]
            
            if m_in > minute:
                minute += 60
                hour -= 1
            cal_mins = 60 * (hour - h_in) + minute - m_in
            
            if cal_time.get(rcd[1]):
                cal_time[rcd[1]] += cal_mins
            else:
                cal_time[rcd[1]] = cal_mins
                car_num.append(rcd[1])
    
    if times:
        for time in times:
            h_in, m_in = times[time]
            cal_mins = 60 * (23 - h_in) + 59 - m_in

            if cal_time.get(time):
                cal_time[time] += cal_mins
            else:
                cal_time[time] = cal_mins
                car_num.append(time)
        
    # 2. fees에 맞게 요금을 정산
    car_num.sort()
    answer = []
    for n in car_num:
        additional = cal_time[n] - fees[0]
        if additional > 0:
            added_fee = math.ceil(additional / fees[2])
            result = fees[1] + (added_fee)*fees[3]
        else:
            result = fees[1]
        answer.append(result)
        
    # 3. answer 리스트 반환
    return answer