class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 0, 'V': 0, 'X':0, 'L': 0, 'C': 0, 'D': 0, 'M': 0}
        output = 0
        lst = list(s)
        print (lst)
        #если предыдущее и предыдущее -1 меньше следующего - то отнимаем от текущего элемента массива предыдущий (1 или 2 раза)
        '''for i in range(lst):
            if 'IV' in s:
                output-= 1

            elif 'IIV' in s:
                output -= 2
            elif 'IX' in s:
                output -= 1
            elif 'IIX' in s:
                output -= 2
            elif 'XL' in s:
                output -= 10
            elif 'XXL' in s:
                output -= 20
            elif 'XC' in s:
                output -= 10
            elif 'XXC' in s:
                output -= 20
            elif 'CD' in s:
                output -= 100
            elif 'CCD' in s:
                output -= 200
            elif 'CM' in s:
                output -= 100
            elif 'CCM' in s:
                output -= 200'''
        print(output)
        print(len(s))
        for ch in s:
            d[ch]+=1

        output = d['I']*1 + d['V']*5 + d['X']*10 + d['L']*50 + d['C']*100 + d['D']*500 + d['M']* 1000
        return output

result = Solution().romanToInt('MCMXCIV')
print(result)