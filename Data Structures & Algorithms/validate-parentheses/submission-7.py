class Solution:
    def isValid(self, s: str) -> bool:

        map = {')':'(', '}':'{', ']':'['}
        if len(s) < 2:
            return False
        stack = []

        for i in s:
    
            if i not in map:
                stack.append(i)
            else:
                if stack:
                    last = stack.pop()
                    if last != map[i]:
                        stack.append(last)
                        stack.append(i)
                else:
                    stack.append(i)
        return False if stack else True



        