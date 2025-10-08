class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in d:
                return [d[b],i]
            d[a] = i
result = Solution().twoSum([3, 4, 5], 6)
print(result)