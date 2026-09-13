class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = defaultdict(list) 

        for s in strs:
            sorted_s = "".join(sorted([c for c in s]))
            grps[sorted_s].append(s)
        
        return list(grps.values())
        