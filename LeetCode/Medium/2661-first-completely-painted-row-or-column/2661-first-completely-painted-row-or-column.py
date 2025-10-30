class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # 딕셔너리 활용
        coor_dict = {}

        n, m = len(mat), len(mat[0])

        for i in range(n):
            for j in range(m):
                coor_dict[mat[i][j]] = (i, j)
        
        is_painted = [0]*(n+m+1)
        for i in range(len(arr)):
            x, y = coor_dict[arr[i]]
            is_painted[x] += 1
            is_painted[n+y] += 1
            
            # print(is_painted)

            if is_painted[x] == m or is_painted[n+y] == n:
                return i
            