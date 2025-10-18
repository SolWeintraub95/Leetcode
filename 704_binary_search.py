class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)
        index = len(nums) // 2
        # мы проходим по массиву покуда не найдём индекс элемента равного таргету
        while nums[index] != target:
            if nums[index] > target:
                r = index
            elif nums[index] < target:
                l = index
            index = l + ((r - l) // 2)
            if r-l == 0 or (r-l == 1 and index != 0) or len(nums) == 1:
                return -1
        return index

result = Solution().search([-1], 2)
print(result)