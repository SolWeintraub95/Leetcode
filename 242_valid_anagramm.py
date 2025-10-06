class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list= list(s)
        t_list= list(t)
        enum=0
        for i in range(len(s)):
            if s[i] in t_list:
                s_list[i] = 0
                t_list[t_list.index(s[i])] = 0
                print(t_list[t_list.index(s[i])])
        for i in range(len(s)):
            if s_list[i] == 0 and t_list[i] == 0:
                enum+=1

        if enum == len(s):
            return True
        else:
            return False



result = Solution().isAnagram('anagram','nagaram')
print(result)