class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # (n, m)은 각 꽃의 개수를 뜻한다
        # 합이 홀수인 조합을 구하면 됨
        cnt = 0
        for i in range(1, n+1):
            if i % 2:
                # 홀수일 때 모든 짝수
                cnt += m // 2
                # print(f"{i=}, {cnt=}")
            else:
                # 짝수일 때는 모든 홀수
                cnt += (m + 1) // 2
                # print(f"{i=}, {cnt=}")

        return cnt