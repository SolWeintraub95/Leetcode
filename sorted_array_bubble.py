class Solution:
    def sortedArrayBubble(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            isSorted = True
            for k in range(len(nums) - i - 1):
                if nums[k] > nums[k + 1]:
                    nums[k], nums[k + 1] = nums[k + 1], nums[k]
                    isSorted = False
        # print(nums)
            if isSorted:
                break

        return nums


result = Solution().sortedArrayBubble([3, 2, 1, 200, 4, -1, 0])
print(result)
