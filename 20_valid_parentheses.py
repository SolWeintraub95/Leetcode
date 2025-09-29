class Solution:
    def isValid(self, s: str) -> bool:
        '''
        У нас есть только 3 вида открывающих скобок
        Хочется обойтись без цикла и просто наебашить if'ы но это пиздец тяжело перебором хуярить
        Есть идея использовать цикл while почему-то, хз почему просто наитие
        Можно сделать 1 переменную и смотреть положительная она или отрицательная (оптимизация, чтобы не делать 6 переменных, а сделать 3 под каждый тип скобки
        '''

        opened=0
        closed=0
        for i in s:
            if i == '(':
                opened+=1

            elif i== ')':
                closed+=1
                if closed > opened:
                    return False


        if opened > closed:
            return False
        return True
result=Solution().isValid('(())()')
print(result)
