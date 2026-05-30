class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        temp = defaultdict(int)
        index_counter = 0

        for i in range(len(strs)):
            res = ''.join(sorted(strs[i]))
            if res not in temp:
                temp[res] = index_counter
                index_counter +=1
        
        result = [[] for _ in range(len(temp))]

        for i in strs:
            result[temp[''.join(sorted(i))]].append(i)
        return result