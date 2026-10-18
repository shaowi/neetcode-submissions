class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        n = len(s)
        window = {} 
        targetCnt = {} 
        res_idx = [-1, -1]
        res_len = float('inf') 

        for c in t:
            targetCnt[c] = 1 + targetCnt.get(c, 0)

        has = 0
        need = len(targetCnt)
        for r in range(n):
            c = s[r]
            window[c] = 1 + window.get(c, 0) 

            if c in targetCnt and window[c] == targetCnt[c]:
                has += 1
            
            while has == need:
                if r - l + 1 < res_len:
                    res_idx = [l, r]
                    res_len = r - l + 1
                window[s[l]] -= 1 
                if s[l] in targetCnt and window[s[l]] < targetCnt[s[l]]:
                    has -= 1
                l += 1
                
        l, r = res_idx
        return s[l: r + 1] if res_len != float('inf') else "" 