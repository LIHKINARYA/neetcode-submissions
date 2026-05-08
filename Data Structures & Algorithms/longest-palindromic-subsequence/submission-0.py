class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #basically we will do the same now only with the reverse word

        dp = [[0 for i in range(len(s)  + 1)] for i in range(len(s) + 1)]
        pal = s[::-1]

        for i in range(len(s) - 1,-1,-1):
            for j in range(len(s) - 1,-1,-1):
                if s[i] == pal[j]:
                    dp[i][j] = 1 + dp[i+ 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]

        