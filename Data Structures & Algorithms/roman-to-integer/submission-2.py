class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }

        res = 0
        skip = False

        for i in range(len(s)):
            if skip:
                skip = False
                continue
            if i != len(s) - 1 and mapping[s[i]] < mapping[s[i + 1]]:
                skip = True
                res += mapping[s[i + 1]] - mapping[s[i]]
            else:
                res += mapping[s[i]]
        return res
        


        