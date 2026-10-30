class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                cS = ""
                while stack and stack[-1] != "[":
                    cS = stack.pop() + cS
                stack.pop()
                digits = ""
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                
                stack.append(cS * int(digits))
            else:
                stack.append(c)
        return "".join(stack)
