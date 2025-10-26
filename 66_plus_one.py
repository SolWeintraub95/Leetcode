class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        k = len(digits)
        sum = 0
        for i in range(k):
            sum = sum + digits[k - i - 1] * 10 ** i
            digits.pop()
        sum += 1
        i = 0
        while k+1 > i:
            tmp = sum % 10
            digits.insert(0, tmp)
            sum = sum // 10
            k -= 1
        if digits[0] == 0:
            digits.pop(0)
        return digits

result = Solution().plusOne([4,3,2,1])
print(result)
