from itertools import islice, cycle

def solution(m, musicinfos):
    musics = []
    sharps = {'A#': 'H', 'B#': 'I', 'C#': 'J', 'D#': 'K', 'E#': 'L', 'F#': 'M', 'G#': 'N',}
    
    def replce(strings):
        for k in sharps.keys():
            strings = strings.replace(k, sharps[k])
        return strings
    
    m = replce(m)
    
    for i, music in enumerate(musicinfos):
        infos = music.split(',')
        
        # 재생 시간
        time0, time1 = infos[0].split(':'), infos[1].split(':')
        t_diff = (int(time1[0])*60 + int(time1[1])) - (int(time0[0])*60 + int(time0[1]))
        
        # 멜로디 저장
        melody = replce(infos[3])
        played = ''.join(list(islice(cycle(melody), t_diff)))
        
        # 확인
        if len(m) <= len(played):
            if m in played:
                # 음악 정보 저장
                musics.append([t_diff, played, infos[2], i])
    
    if not musics:
        return '(None)'
    musics.sort(key=lambda x: (-x[0], x[3]))
    return musics[0][2]        
        