class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j=0
        for i in range(len(nums)):
            while nums[j] == 0 or j <= i:
                j+=1
                if j == len(nums):
                    return
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]


xs = [1,2,3,0,4]
Solution().moveZeroes(xs)
print(xs)