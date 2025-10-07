class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}

        #Ищем уникальные символы в изначальной строке и добавляем их в словарь
        # При каждой встрече символа в изначальной строке добавляем к значению словаря +1
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch]+= 1

        #При каждой встрече символа в конечной строке отнимаем от значения словаря -1
        for ch in t:
            if ch in d:
                d[ch]-= 1

        #Условие, где если все значения в словаре равны 0, т.е. число встреч букв одинаково в обоих строках, то возвращаем true, иначе false
        return all(value == 0 for value in d.values())




result = Solution().isAnagram('rat','car')
print(result)