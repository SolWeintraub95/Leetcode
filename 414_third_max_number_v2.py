class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        max1 = nums[0]
        max2 = max3 = None
        for i in range(len(nums)):
            if nums[i] > max1:
                max3 = max2
                max2 = max1
                max1 = nums[i]
            if nums[i] < max1 and (max2 is None or nums[i] > max2):
                max3 = max2
                max2 = nums[i]
            if max2 is not None and nums[i] < max2 and (max3 is None or nums[i] > max3):
                max3 = nums[i]
            print(max1,max2,max3)
        if max3 is not None:
            return max3
        else:
            return max1



        # Запускаем тот же счётчик. max3 должен быть (строго?) меньше max2, больше минимального числа int
        '''for i in range(len(nums)):
            if nums[i] > max3 and nums[i] < max2:
                max3=nums[i]'''

        #кейсы которые стоит помнить: [1,2], [1,1,2], [1,1,1]


result = Solution().thirdMax([1,2,3,3,20])
#print(result)