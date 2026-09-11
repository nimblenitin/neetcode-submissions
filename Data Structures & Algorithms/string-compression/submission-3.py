class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        i = k = 0
        
        while i < n:
            chars[k] = chars[i]
            k += 1

            j = i + 1

            while j < n and chars[i] == chars[j]:
                j += 1
            
            if j - i > 1:
                for d in str(j - i):
                    chars[k] = d
                    k += 1
            
            i = j
        return k
            

