class Solution:
    def isValid(self, s: str) -> bool:
        my_list = []
        for i in s:
            if i == '(':
                my_list.append(i)

            elif i == '[':
                my_list.append(i)

            elif i == '{':
                my_list.append(i)

            elif i == ')' and my_list and my_list[-1] == '(':
                my_list.pop()

            elif i == ']' and my_list and my_list[-1] == '[':
                my_list.pop()

            elif i == '}' and my_list and my_list[-1] == '{':
                my_list.pop()

            else:
                return False

        return not my_list

result = Solution().isValid('()[]')
print(result)