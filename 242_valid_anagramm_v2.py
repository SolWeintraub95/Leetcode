class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}

        for ch in s:
            if ch not in d:
                d[ch] = 0

        for ch in s:
            d[ch]+= 1

        for ch in t:
            if ch in d:
                d[ch]-= 1

        if all(value == 0 for value in d.values()):
            return True
        else:
            return False

        #print(d)



        '''for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]]+= 1
            print(d)1'''





result = Solution().isAnagram('anagram','nagaram')
print(result)