def solution(record):
    users = {}
    answer = []
    for r in record:
        cmd = r.split()
        if cmd[0] == 'Enter' or cmd[0] == 'Change':
            users[cmd[1]] = cmd[2]
    
    for r in record:
        cmd = r.split()
        if cmd[0] == 'Enter':
            answer.append(f'{users[cmd[1]]}님이 들어왔습니다.')
        elif cmd[0] == 'Leave':
            answer.append(f'{users[cmd[1]]}님이 나갔습니다.')
            
    return answer