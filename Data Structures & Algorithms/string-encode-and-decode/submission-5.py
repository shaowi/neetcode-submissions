class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) > 0:
            nums = [",".join([str(ord(c)) for c in s]) for s in strs]
            return 't' + "|".join(nums) 
        return ""

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        nums = s[1:].split("|")
        return ["".join([chr(int(d)) if d else '' for d in num.split(',')]) for num in nums]  
