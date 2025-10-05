def solution(numbers, hand):
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1)
    }
    left, right = (1, 4, 7), (3, 6, 9)
    current = {'left': [3, 0], 'right': [3, 2]}
    
    def pick_hand(num):
        nonlocal keypad, current, left, right, hand
        
        if num in left:
            current['left'] = keypad[num]
            return 'L'
        
        elif num in right:
            current['right'] = keypad[num]
            return 'R'
        
        else:
            padnum = keypad[num]
            d_l = abs(padnum[0] - current['left'][0]) + abs(padnum[1] - current['left'][1])
            d_r = abs(padnum[0] - current['right'][0]) + abs(padnum[1] - current['right'][1])
            
            if d_l == d_r:
                picked = hand
            elif d_l < d_r:
                picked = 'left'
            elif d_l > d_r:
                picked = 'right'
                
            current[picked] = keypad[num]
            return 'L' if picked == 'left' else 'R'
        
    result = ''
    for number in numbers:
        # print(current, number)
        result += pick_hand(number)
    
    return result