class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = i = 0
        #Если мы в итоговой строке встречаем символ из первой - удаляем его из листа и продолжаем идти по массиву t
        if not s:
            return True
        while j < len(t):
            if s[i] == t[j]:
                i+=1
                if i == len(s):
                    return True

            j+=1
        return False

result = Solution().isSubsequence('b', 'c')
print(result)