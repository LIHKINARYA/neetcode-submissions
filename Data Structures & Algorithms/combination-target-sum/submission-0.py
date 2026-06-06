class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        
        def dfs(start_index: int, temp: List[int], remaining: int):
            if remaining == 0:
                result.append(temp.copy())
                return
            
            for i in range(start_index, len(nums)):
                num = nums[i]
                if remaining - num >= 0:
                    temp.append(num)
                    dfs(i, temp, remaining - num)  # Use same i to allow repeats
                    temp.pop()  # Backtrack
        
        dfs(0, [], target)
        return result
        