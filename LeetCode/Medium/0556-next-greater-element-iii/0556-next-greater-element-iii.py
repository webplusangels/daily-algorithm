class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_list = [num for num in str(n)]
        to_c = [n_list[-1], len(n_list) - 1]
        from_c = [None, None]
        for i in range(len(n_list)-2, -1, -1):
            if to_c[0] > n_list[i]:
                from_c[0], from_c[1] = n_list[i], i
                break
            elif to_c[0] == n_list[i]:
                continue
            else:
                to_c[0], to_c[1] = n_list[i], i
                
        if from_c[0] is None:
            return -1
        
        mx = float('inf')
        mx_i = -1
        for i in range(from_c[1]+1, len(n_list)):
            if from_c[0] < n_list[i] and int(n_list[i]) < mx:
                mx = int(n_list[i])
                mx_i = i
        
        n_list[from_c[1]], n_list[mx_i] = n_list[mx_i], n_list[from_c[1]]
        sorted_list = sorted(n_list[from_c[1]+1:])
        answer = n_list[:from_c[1]+1] + sorted_list
        return int(''.join(answer))