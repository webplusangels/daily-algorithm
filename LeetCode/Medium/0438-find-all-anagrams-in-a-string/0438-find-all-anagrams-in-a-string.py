from collections import defaultdict, Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 슬라이딩 윈도우?
        len_p = len(p)
        answer = []

        p_cnt = Counter(p)
        s_cnt = Counter(s[0:len_p])

        for ss in s_cnt.keys():
            if ss in p_cnt:
                p_cnt[ss] -= s_cnt[ss]

        for i in range(len(s) - len_p+1):
            if all([v == 0 for v in p_cnt.values()]):
                answer.append(i)

            if s[i] in p_cnt:
                p_cnt[s[i]] += 1
            
            if i+len_p < len(s) and s[i+len_p] in p_cnt:
                p_cnt[s[i+len_p]] -= 1
            
            # print(f"{p_cnt=}")

        return answer