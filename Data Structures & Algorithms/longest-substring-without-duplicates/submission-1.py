class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        temp = defaultdict(int)
        l = 0

        for r in range(len(s)):
            temp[s[r]] +=1
            while temp[s[r]] > 1:
                temp[s[l]] -=1
                l +=1
                            
            res = max(res,r - l)
        return res + 1
            


        