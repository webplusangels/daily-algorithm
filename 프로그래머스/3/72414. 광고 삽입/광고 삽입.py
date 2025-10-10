def solution(play_time, adv_time, logs):
    """ 
    Args:
        play_time: 영상 총 재생 시간
        adv_time: 광고 재생 시간
        logs: 사용자들의 재생 기록
    
    Returns:
        누적 재생 시간이 가장 많이 나오는 곳의 시작 시간 (가장 빠른)
    """
    def to_sec(time):
        """
        Args:
            time: 시간 스트링
    
        Returns:
            초 단위로 변환한 시간
        """
        tmp = time.split(':')
        sec = int(tmp[0])*60*60 + int(tmp[1])*60 + int(tmp[2])
        
        return sec
    
    # 전부 초 단위로 통일
    play_sec = to_sec(play_time)
    adv_sec = to_sec(adv_time)
    adv_range = play_sec - adv_sec
    
    # 변화량
    timeline = [0]*(play_sec+1)
    for log in logs:
        start, end = log.split('-')
        start_s, end_s = to_sec(start), to_sec(end)
        timeline[start_s] += 1
        timeline[end_s] -= 1
        
    for i in range(1, play_sec+1):
        timeline[i] += timeline[i-1]
        
    for i in range(1, play_sec+1):
        timeline[i] += timeline[i-1]
    
    # [0][0][1][0][1][0][-1][-1]
    # [0][0][1][1][2][2][1][0]
    #  0  1  2  3  4  5  6  7
    # 2초에 view+1 4초에 view+1 6초에 -1 7초에 -1
    # [0][0][1][2][4][6][7][7][7][7]
    # 광고가 4초짜리면 i=3 
    
    # 슬라이딩 윈도우        
    max_view = 0
    max_start = 0
    
    max_view = timeline[adv_sec-1]
    for i in range(adv_sec, play_sec+1):
        view = timeline[i] - timeline[i-adv_sec]
        if max_view < view:
            max_view = view
            max_start = i - adv_sec + 1
            
    m, s = divmod(max_start, 60)
    h, m = divmod(m, 60)
    
    # print(f"{h:02}:{m:02}:{s:02}")
    return f"{h:02}:{m:02}:{s:02}"