class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = 1
            else:
                d[s[i]]+= 1
            print(d)1





result = Solution().isAnagram('anagram','nagaram')
print(result)