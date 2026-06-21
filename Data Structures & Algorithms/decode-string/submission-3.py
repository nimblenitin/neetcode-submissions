class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            substr = ""
            if s[i] == "]" and stack:
                while stack[-1] != "[" and stack:
                    substr = stack.pop() + substr
                stack.pop()
                digits = ""
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                stack.append(substr * int(digits))
            else:
                stack.append(s[i])
        return "".join(stack)

