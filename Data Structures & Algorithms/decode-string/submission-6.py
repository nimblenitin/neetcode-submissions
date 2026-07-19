class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == "]":
                char = ""
                while stack and stack[-1] != "[":
                    char = stack.pop() + char
                stack.pop()
                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                stack.append(char * int(digit))
            else:
                stack.append(s[i])
        return "".join(stack)
            