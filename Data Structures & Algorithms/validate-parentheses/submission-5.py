class Solution:
    def isValid(self, s: str) -> bool:

        map = {')':'(', '}':'{', ']':'['}
        if len(s) < 2:
            return False
        stack = []

        for i in s:
            if i in map:  # closing bracket
                if not stack or stack.pop() != map[i]:
                    return False
            else:  # opening bracket
                stack.append(i)
        return not stack



        