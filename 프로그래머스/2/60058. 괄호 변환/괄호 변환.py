def solution(p):
    def split_str(p):
        # 균형잡힌 괄호 문자열이 목표
        dic = {'(': 0, ')': 0}
        for i in range(len(p)):
            dic[p[i]] += 1
        
            if dic['('] == dic[')']:
                return p[:i+1], p[i+1:]
    
    def is_right(p):
        # 올바른 괄호 문자열인지?
        stack = []
        for i in range(len(p)):
            if p[i] == '(':
                stack.append(p[i])
            else:
                if not stack:
                    return False
                else:
                    stack.pop()
        return not stack
        # if not stack:
        #     return True
    
    change = {'(': ')', ')': '('}
    
    def func(v):
        if v == '':
            return ''
        
        u, v = split_str(v)
        # print(f'{u=} {v=}')
        if not is_right(u):
            v = '(' + func(v) + ')'
            u = [change[s] for s in u[1:len(u)-1]]
            return v + ''.join(u)
        
        return u + func(v)
    
    return func(p)