class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_cnt = Counter(s1)
        s2_substr_cnt = Counter(s2[:len(s1)])
        l = 0

        for r in range(len(s1), len(s2)):
            if s1_cnt == s2_substr_cnt:
                return True
            s2_substr_cnt[s2[l]] = max(0, s2_substr_cnt[s2[l]] - 1)
            s2_substr_cnt[s2[r]] = s2_substr_cnt.get(s2[r], 0) + 1
            l += 1

        return s1_cnt == s2_substr_cnt 