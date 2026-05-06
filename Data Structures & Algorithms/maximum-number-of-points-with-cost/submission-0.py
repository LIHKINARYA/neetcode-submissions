class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points or not points[0]:
            return 0
        
        dp = points[0][:]

        r = len(points)
        c = len(points[0])

        for i in range(1,r):
            new_dp = [0] * c
            
            #left to right pass
            left_max = [0] * c
            left_max[0] = dp[0]
            for j in range(1,c):
                left_max[j] = max(left_max[j - 1] - 1,dp[j])
            
            #right to left pass
            right_max = [0] * c
            right_max [c - 1] = dp[c - 1]
            for j in range(c - 2, -1,-1):
                right_max[j] = max(right_max[j + 1] - 1, dp[j])
            
            #combine both passes for current row
            for j in range(c):
                new_dp[j] = points[i][j] + max(left_max[j], right_max[j])
            
            dp = new_dp
        return max(dp)
            
                 