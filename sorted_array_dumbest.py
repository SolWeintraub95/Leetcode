class Solution:
    def searchMin(self, nums: list[int]):
        min = None
        for i in range(len(nums)):
            if min is None or nums[i] < min:
                min = nums[i]
    def sortedArrayDumbest(self, nums: list[int]) -> list[int]:
        SortArr = ()
        min = None
        while nums:
            Solution().searchMin(nums)


        #Поиск индекса минимума можно выделить в отдельную функцию, по нему можно будет попать элемент, потом добавить его в новый список, повторять пока изначальный список не опустеет
        #Длина масива будет отличаться, поэтому итерироваться по ней нельзя, всё поплывёт нахуй












