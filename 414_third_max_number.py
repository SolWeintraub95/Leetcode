class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        #Костыль
        max=max2=max3 = -2**31-1
        min = nums[0]
        #Запускаем счётчик по количеству элементов в листе и стандартное сравнение что каждый элемент массива меньше max
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
        #Запускаем счётчик по количеству переменных в листе и стандартное сравнение что каждый элемент массива больше min
        for i in range(len(nums)):
            if nums[i] < min:
                min = nums[i]

        #Запускаем тот же счётчик. max2 должен быть строго меньше max, больше минимального числа int
        for i in range(len(nums)):
            if nums[i] > max2 and nums[i] < max:
                max2=nums[i]


        # Запускаем тот же счётчик. max3 должен быть (строго?) меньше max2, больше минимального числа int
        for i in range(len(nums)):
            if nums[i] > max3 and nums[i] < max2:
                max3=nums[i]

        #Костыли для решения [1,2], [1,1,2] и [1,1,1] соответственно
        if len(nums)<=2 or min == max2 or min==max:
            return max
        return max3
result = Solution().thirdMax([3,2,1])
print(result)