class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #basically we will merge any overlapping
        n = len(intervals)
        intervals.sort() #nlogn
        result = []
        temp = [intervals[0][0],intervals[0][1]]

        for i in range(1, n):  # Start from index 1
            if temp[1] >= intervals[i][0]:  # There's overlap
                temp = [temp[0], max(temp[1], intervals[i][1])]  # Merge
            else:  # No overlap
                result.append(temp)  # Add previous merged interval
                temp = [intervals[i][0], intervals[i][1]]  # Start new interval
        result.append(temp)
        return result





