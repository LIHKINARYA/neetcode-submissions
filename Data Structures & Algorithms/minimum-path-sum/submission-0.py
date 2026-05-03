class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        #we create a dp of (m x n)
        
        dp = grid
        
        for i in range(m - 1,-1,-1):
            for j in range(n - 1,-1,-1):
                if i + 1 < m and j + 1 < n:
                    dp[i][j] += min(dp[i + 1][j],dp[i][j + 1])
                elif i + 1 < m:
                    dp[i][j] += dp[i + 1][j]
                elif j + 1 < n:
                    dp[i][j] += dp[i][j + 1]

        return dp[0][0]
        