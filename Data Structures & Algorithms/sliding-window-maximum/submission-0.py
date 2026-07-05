class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = deque()          # stores indices, values in decreasing order
        result = []

        for i, val in enumerate(nums):
            # Remove indices with value <= current val from back
            while dq and nums[dq[-1]] <= val:
                dq.pop()
            dq.append(i)
            
            # Remove indices that are out of window
            if dq[0] <= i - k:
                dq.popleft()
            
            # If window is complete, record the max
            if i >= k - 1:
                result.append(nums[dq[0]])
                
        return result