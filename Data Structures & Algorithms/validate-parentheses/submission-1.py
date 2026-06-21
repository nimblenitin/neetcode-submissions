class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}": "{", ")": "(", "]": "["}
        stack = []
        for i in range(len(s)):
            if stack and s[i] in closeToOpen:
                if stack[-1] == closeToOpen[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False