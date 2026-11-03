class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"]": "[", "}": "{", ")": "("}

        for c in s:
            if c in closeToOpen and stack:
                if stack and stack[-1] != closeToOpen[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return True if not stack else False