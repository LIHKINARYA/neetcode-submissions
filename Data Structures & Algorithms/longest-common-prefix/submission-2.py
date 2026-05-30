class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        lcp = 0
        min_len = min([len(s) for s in strs])
        
        for i in range(min_len):
            current_char = strs[0][i]
            for s in strs:
                if s[i] != current_char:
                    print(lcp)
                    return strs[0][:lcp]
            lcp += 1
        return strs[0][:lcp]