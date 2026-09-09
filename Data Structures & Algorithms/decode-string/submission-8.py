class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == "]":
                char = ""
                while stack and stack[-1] != "[":
                    char = stack.pop() + char
                
                stack.pop()

                digits = ""
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                
                stack.append(char * int(digits))
            else:
                stack.append(s[i])
        return "".join(stack)
