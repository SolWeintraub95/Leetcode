class Solution:
    def max(self, nums: list[int]) -> int:
        max = -2**31-1
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
        return max

    def thirdMax(self, nums: list[int]) -> int:
        max=max2=max3 = -2**31-1
        min = 2**31-1

        for i in range(len(nums)):
            if nums[i] > max:
                max = max2 = nums[i]
            if nums[i] < max:
                max2 = nums[i]
        print(max,max2)
        #print(max,max2,max3)

#result = Solution().thirdMax(3,1,2)
result = Solution().thirdMax([1,2,3,4])
#print(result)