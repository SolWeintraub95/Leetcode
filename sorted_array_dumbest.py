class Solution:
    def searchMin(self, nums: list[int]):
        min = None
        min_i = None
        for i in range(len(nums)):
            if min is None or nums[i] < min:
                min = nums[i]
                min_i = i
        return min_i
    def sortedArrayDumbest(self, nums: list[int]) -> list[int]:
        sorted_arr = []
        while nums:
            min_i = self.searchMin(nums)
            sorted_arr.append(nums.pop(min_i))
        return sorted_arr

result = Solution().sortedArrayDumbest([1, 20, 3, 3, 21])
print(result)


        #Поиск индекса минимума можно выделить в отдельную функцию, по нему можно будет попать элемент, потом добавить его в новый список, повторять пока изначальный список не опустеет
        #Длина масива будет отличаться, поэтому итерироваться по ней нельзя, всё поплывёт нахуй












