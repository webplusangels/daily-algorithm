class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        l = len(arr)
        
        def find_to_swap(arr):
            tmp = arr[-1]
            for i in range(len(arr)-2, -1, -1):
                if tmp < arr[i]:
                    return i
                tmp = arr[i]    
            else:
                return

        swap = find_to_swap(arr)
        if swap is not None:
            tmp = -1
            tmp_i = -1
            for i in range(swap+1, l):
                if tmp < arr[i] and arr[i] < arr[swap]:
                    tmp_i = i
                    tmp = arr[i]
            
            arr[swap], arr[tmp_i] = arr[tmp_i], arr[swap]
            return arr
        else:
            return arr