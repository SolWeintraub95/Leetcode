class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            d[s[i]] = 1
            d[s[i]]+= 1
            print(d)






result = Solution().isAnagram('anagram','nagaram')
print(result)