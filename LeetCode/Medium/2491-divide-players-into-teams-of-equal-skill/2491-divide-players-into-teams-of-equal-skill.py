class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = sum(skill)
        l = len(skill)
        num_teams = l // 2
        
        if s % num_teams != 0:
            return -1
        
        team_p = s // (len(skill) // 2)
        skill.sort()
        
        answer = 0
        for i in range(l // 2):
            if skill[i] + skill[-1-i] != team_p:
                return -1
            answer += skill[i]*skill[-1-i]
        
        return answer