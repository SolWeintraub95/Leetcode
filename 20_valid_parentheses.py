class Solution:
    def isValid(self, s: str) -> bool:
        brackets=0
        curly=0
        square=0
        check=0
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False

        for index,i in enumerate(s):
            print(index,i)
            if i == ')' and ((s[index-1])=='{' or (s[index-1])=='['):
                check +=1
                print(1)
                return False

            elif i == '}' and ((s[index-1])=='(' or (s[index-1])=='['):
                check += 1
                print(2)
                return False

            elif i == ']' and ((s[index-1])=='{' or (s[index-1])=='('):
                check += 1
                print(3)
                return False

            elif i == '(':
                brackets+=1
                print(4)

            elif i== ')' :
                brackets-=1
                print(5)
                if brackets < 0:
                    return False

            elif i== '{':
                curly+=1
                print(6)

            elif i== '}':
                curly-=1
                print(7)
                if curly < 0:
                    return False

            elif i== '[':
                square+=1
                print(8)

            elif i== ']':
                square-=1
                print(9)
                if square < 0:
                    return False

        print(brackets,curly,square, check)
        if brackets != 0 or curly != 0 or square != 0 or check != 0:
            return False
        return True

result=Solution().isValid('[([]])')
print(result)
