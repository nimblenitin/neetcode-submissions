class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digToChar = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}
        
        def backtrack(i, substr):
            if len(substr) == len(digits):
                res.append(substr)
                return
            
            for c in digToChar[digits[i]]:
                backtrack(i + 1, substr + c)
        
        if digits:
            backtrack(0, "")
        return res
