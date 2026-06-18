class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        L = n + m - 1  
        
        word = [None] * L
        forced = [False] * L
        
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    if word[pos] is not None and word[pos] != str2[j]:
                        return ""
                    word[pos] = str2[j]
                    forced[pos] = True
        
        free = [False] * L
        for i in range(L):
            if word[i] is None:
                word[i] = 'a'
                free[i] = True
        
        def interval_equals(i: int) -> bool:
            for j in range(m):
                if word[i + j] != str2[j]:
                    return False
            return True
        
        for i in range(n):
            if str1[i] == 'F':
                if interval_equals(i):
                    fixed = False
                    for j in range(m - 1, -1, -1):
                        pos = i + j
                        if free[pos]:
                            word[pos] = 'b'
                            free[pos] = False  
                            fixed = True
                            break
                    if not fixed:
                        return ""
        
        return "".join(word)