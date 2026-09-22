import re
class Solution:
    def cleanString(self, input_string):
        # Replace non-alphanumeric characters with '_'
        result = re.sub(r'[^a-zA-Z0-9]+', '', input_string)
        # Remove leading or trailing underscores
        result = result.strip('_')
        # Convert to lowercase
        return result.lower()
        
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = self.cleanString(s)
        l, r = 0, len(cleaned_s) - 1
        
        while l < r:
            if cleaned_s[l] != cleaned_s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        