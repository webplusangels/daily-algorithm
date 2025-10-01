def solution(n, k):
    if k != 10:
        target = ''
        while n > 0:
            n, left = divmod(n, k)
            target = str(left) + target
    else:
        target = str(n)
    
    def is_prime(x):
        p_num = int(x**0.5)
        for i in range(2, p_num+1):
            if x % i == 0:
                return False
        else:
            return True
        
    nums = target.split('0')
    cnt = 0
    for num in nums:
        if num and num != '1':
            if is_prime(int(num)):
                cnt += 1
    
    return cnt