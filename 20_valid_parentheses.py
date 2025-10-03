class Solution:
    def isValid(self, s: str) -> bool:
        brackets=0
        curly=0
        square=0
        check=0
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        else:
            for i in s:
                if i == ')' and (s[s.index(i)-1]=='{' or s[s.index(i)-1] =='['):
                    check +=1
                    #print(s[s.index(i)+1])
                    return False

                elif i == '}' and (s[s.index(i)-1]=='(' or s[s.index(i)-1] =='['):
                    check += 1
                    #print(s[s.index(i) + 1])
                    return False

                elif i == ']' and (s[s.index(i)-1]=='{' or s[s.index(i)-1] =='('):
                    check += 1
                    #print(s[s.index(i) + 1])
                    return False

                elif i == '(':
                    brackets+=1

                elif i== ')' :
                    brackets-=1
                    if brackets < 0:
                        return False

                elif i== '{':
                    curly+=1

                elif i== '}':
                    curly-=1
                    if curly < 0:
                        return False

                elif i== '[':
                    square+=1

                else:
                    square-=1
                    if square < 0:
                        return False

            if brackets != 0 or curly != 0 or square != 0 or check != 0:
                return False
            return True

result=Solution().isValid('(())()')
print(result)
