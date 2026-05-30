class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashtable = dict()

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashtable:
                return [hashtable[compliment],i]
            hashtable[nums[i]] = i
        return []

        