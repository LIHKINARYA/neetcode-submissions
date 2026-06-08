class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            # Check if needle matches starting at position i
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1