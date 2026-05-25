class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #each boat can carry limnit
        #carry atmost 2 people provided the sum of the weifht of those people is at most limit

        newPeople = sorted(people)

        left = 0
        right = len(people) - 1
        count = 0

        while left <= right:
            if newPeople[left] + newPeople[right] <= limit:
                count += 1
                left += 1
                right -= 1
            else:
                count +=1
                right -=1  
        
        return count